#!/usr/bin/env python3
"""
Extract per-game telemetry model token usage from player trace databases.
Creates one row per player-model pair aggregated across valid turns.
"""

import json
import os
import re
from typing import Dict, List, Optional, Tuple

from shared.model_catalog import (
    compose_player_type as shared_compose_player_type,
    canonicalize_model_name as shared_canonicalize_model_name,
    normalize_model_base as shared_normalize_model_base,
)

from .utilities import (
    append_csv_file,
    filter_existing_data,
    get_experiment_from_path,
    get_game_id_from_path,
    open_database_readonly,
    read_existing_csv,
    should_skip_game,
    write_csv_file,
)


MODEL_TOKEN_FIELDNAMES = [
    "experiment",
    "game_id",
    "player_id",
    "player_type",
    "model_name",
    "model_base",
    "model_variants",
    "agent_names",
    "input_tokens",
    "reasoning_tokens",
    "output_tokens",
    "total_tokens",
    "tool_count",
    "focus_briefer_count",
    "valid_turn_count",
]

VANILLA_MODEL_NAME = "Vanilla"
VANILLA_MODEL_BASE = "vanilla"

PLAYER_TRACE_PATTERN = re.compile(
    r"^(?P<game_id>[0-9a-f-]+)-player-(?P<player_id>\d+)\.db$",
    re.IGNORECASE,
)


def normalize_model_base(model_raw: Optional[str]) -> Optional[str]:
    """
    Strip quality suffixes such as @low or @medium from a raw telemetry model name.
    """
    return shared_normalize_model_base(model_raw)


def canonicalize_model_name(model_base: Optional[str]) -> str:
    """
    Map provider-specific model identifiers to the canonical labels used in analysis.
    Falls back to the normalized raw identifier when a match is unknown.
    """
    return shared_canonicalize_model_name(model_base)


def _extract_agent_name(span_name: str, agent_name: Optional[str]) -> str:
    """
    Extract a stable agent name from a span name or JSON attribute.
    """
    if agent_name:
        return agent_name

    if span_name.startswith("agent."):
        stripped = span_name[len("agent.") :]
        return stripped.split(".step.", 1)[0]

    return span_name


def _is_top_level_agent_span(span_name: str) -> bool:
    return span_name.startswith("agent.") and ".step." not in span_name


def _is_tool_span(span_name: str) -> bool:
    return span_name.startswith("mcp-tool.") or span_name.startswith("simple-tool.")


def _parse_player_trace_path(trace_db_path: str) -> Tuple[Optional[str], Optional[int]]:
    """
    Parse game_id and player_id from a player trace database path.
    """
    match = PLAYER_TRACE_PATTERN.match(os.path.basename(trace_db_path))
    if not match:
        return None, None

    return match.group("game_id"), int(match.group("player_id"))


def _find_player_trace_databases(game_db_path: str) -> List[Tuple[int, str]]:
    """
    Find all player trace databases corresponding to a game database.
    """
    game_id = get_game_id_from_path(game_db_path)
    if not game_id:
        return []

    directory = os.path.dirname(game_db_path)
    trace_dbs = []

    for filename in os.listdir(directory):
        if not filename.startswith(f"{game_id}-player-") or not filename.endswith(".db"):
            continue
        if filename.endswith(".telepathist.db"):
            continue

        _, player_id = _parse_player_trace_path(filename)
        if player_id is None:
            continue

        trace_dbs.append((player_id, os.path.join(directory, filename)))

    return sorted(trace_dbs, key=lambda item: item[0])


def _load_experiment_config(
    root_dir: str,
    experiment: str,
    config_cache: Dict[str, Optional[dict]],
) -> Optional[dict]:
    """
    Load an experiment config JSON once and cache it.
    """
    if experiment in config_cache:
        return config_cache[experiment]

    def _read_config(config_path: str) -> Optional[dict]:
        try:
            with open(config_path, "r", encoding="utf-8") as handle:
                return json.load(handle)
        except Exception as exc:
            print(f"WARNING: Failed to load experiment config {os.path.basename(config_path)}: {exc}")
            return None

    config_path = os.path.join(root_dir, f"{experiment}.json")
    if os.path.exists(config_path):
        config_cache[experiment] = _read_config(config_path)
        return config_cache[experiment]

    # Some experiment folders are backed by config files with a different
    # filename, so fall back to matching the JSON's declared experiment name.
    for filename in os.listdir(root_dir):
        if not filename.endswith(".json"):
            continue

        fallback_path = os.path.join(root_dir, filename)
        config = _read_config(fallback_path)
        if config and config.get("name") == experiment:
            config_cache[experiment] = config
            return config

    config_cache[experiment] = None
    return None


def _derive_player_type(experiment_config: Optional[dict], player_id: int) -> str:
    """
    Derive the player_type label from the experiment config rather than plotting utilities.
    """
    if not experiment_config:
        return "N/A"

    player_cfg = experiment_config.get("llmPlayers", {}).get(str(player_id))
    if not player_cfg:
        return "N/A"

    strategist = player_cfg.get("strategist")
    llms = player_cfg.get("llms", {})

    if not llms:
        if strategist == "none-strategist":
            return "Vanilla"
        if strategist and "null" in strategist.lower():
            return "Null"
        return "N/A"

    strategist_model_raw = llms.get(strategist)
    if not strategist_model_raw:
        strategist_model_raw = next(iter(llms.values()), None)

    model_name = canonicalize_model_name(normalize_model_base(strategist_model_raw))
    if model_name == "N/A":
        return "N/A"

    has_briefers = any("briefer" in role for role in llms)
    is_briefed = has_briefers or ("staffed" in (strategist or ""))
    variant = "Briefed" if is_briefed else "Simple"
    return shared_compose_player_type(model_name, variant=variant)


def _fetch_valid_traces(cursor) -> List[Tuple[int, str]]:
    """
    Fetch the last strategist.turn.* trace per turn.
    """
    cursor.execute(
        """
        SELECT turn, traceId
        FROM (
            SELECT turn, traceId, startTime, id,
                   ROW_NUMBER() OVER (
                       PARTITION BY turn
                       ORDER BY startTime DESC, id DESC
                   ) AS rn
            FROM spans
            WHERE name LIKE 'strategist.turn.%'
        )
        WHERE rn = 1
        ORDER BY turn
        """
    )

    return [(int(turn), trace_id) for turn, trace_id in cursor.fetchall()]


def _fetch_relevant_spans(cursor, trace_ids: List[str]) -> List[dict]:
    """
    Fetch only the spans needed for token aggregation and tool ownership.
    """
    if not trace_ids:
        return []

    placeholders = ",".join(["?"] * len(trace_ids))
    cursor.execute(
        f"""
        SELECT
            id,
            traceId,
            spanId,
            parentSpanId,
            turn,
            name,
            json_extract(attributes, '$."agent.name"') AS agent_name,
            json_extract(attributes, '$.model') AS model,
            CAST(COALESCE(json_extract(attributes, '$."tokens.input"'), 0) AS INTEGER) AS input_tokens,
            CAST(COALESCE(json_extract(attributes, '$."tokens.reasoning"'), 0) AS INTEGER) AS reasoning_tokens,
            CAST(COALESCE(json_extract(attributes, '$."tokens.output"'), 0) AS INTEGER) AS output_tokens
        FROM spans
        WHERE traceId IN ({placeholders})
          AND (
              name LIKE 'agent.%'
              OR name LIKE 'mcp-tool.%'
              OR name LIKE 'simple-tool.%'
              OR name LIKE 'strategist.turn.%'
          )
        ORDER BY traceId, id
        """,
        trace_ids,
    )

    spans = []
    for row in cursor.fetchall():
        spans.append(
            {
                "id": row[0],
                "trace_id": row[1],
                "span_id": row[2],
                "parent_span_id": row[3],
                "turn": row[4],
                "name": row[5],
                "agent_name": row[6],
                "model_raw": row[7],
                "input_tokens": int(row[8] or 0),
                "reasoning_tokens": int(row[9] or 0),
                "output_tokens": int(row[10] or 0),
            }
        )

    return spans


def _get_or_create_model_row(
    rows_by_model: Dict[str, dict],
    experiment: str,
    game_id: str,
    player_id: int,
    player_type: str,
    model_raw: str,
    valid_turn_count: int,
) -> dict:
    """
    Create or update an aggregation row for a normalized model identifier.
    """
    model_base = normalize_model_base(model_raw)
    if not model_base:
        raise ValueError("model_raw must normalize to a non-empty model_base")

    if model_base not in rows_by_model:
        rows_by_model[model_base] = {
            "experiment": experiment,
            "game_id": game_id,
            "player_id": player_id,
            "player_type": player_type,
            "model_name": canonicalize_model_name(model_base),
            "model_base": model_base,
            "input_tokens": 0,
            "reasoning_tokens": 0,
            "output_tokens": 0,
            "tool_count": 0,
            "focus_briefer_count": 0,
            "valid_turn_count": valid_turn_count,
            "_model_variants": set(),
            "_agent_names": set(),
        }

    rows_by_model[model_base]["_model_variants"].add(model_raw)
    return rows_by_model[model_base]


def _find_owner_span(tool_span: dict, span_lookup: Dict[Tuple[str, str], dict]) -> Optional[dict]:
    """
    Walk up the parent chain within the same trace until reaching the nearest
    top-level agent span with a model.
    """
    current_parent_span_id = tool_span["parent_span_id"]
    trace_id = tool_span["trace_id"]

    while current_parent_span_id:
        parent = span_lookup.get((trace_id, current_parent_span_id))
        if not parent:
            return None

        if _is_top_level_agent_span(parent["name"]) and parent["model_raw"]:
            return parent

        current_parent_span_id = parent["parent_span_id"]

    return None


def _build_zero_token_row(
    experiment: str,
    game_id: str,
    player_id: int,
    player_type: str,
    valid_turn_count: int,
) -> dict:
    """
    Build a synthetic zero-token row for players that participated in valid turns
    but never emitted a token-bearing model span.
    """
    return {
        "experiment": experiment,
        "game_id": game_id,
        "player_id": player_id,
        "player_type": player_type,
        "model_name": VANILLA_MODEL_NAME,
        "model_base": VANILLA_MODEL_BASE,
        "model_variants": VANILLA_MODEL_BASE,
        "agent_names": "",
        "input_tokens": 0,
        "reasoning_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "tool_count": 0,
        "focus_briefer_count": 0,
        "valid_turn_count": valid_turn_count,
    }


def extract_player_model_token_rows(
    trace_db_path: str,
    game_id: str,
    experiment: str,
    root_dir: str,
    config_cache: Dict[str, Optional[dict]],
) -> List[dict]:
    """
    Extract one row per player-model pair from a player trace database.
    """
    _, player_id = _parse_player_trace_path(trace_db_path)
    if player_id is None:
        return []

    experiment_config = _load_experiment_config(root_dir, experiment, config_cache)
    player_type = _derive_player_type(experiment_config, player_id)

    conn, _ = open_database_readonly(trace_db_path)
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        valid_turns = _fetch_valid_traces(cursor)
        if not valid_turns:
            conn.close()
            return []

        valid_turn_count = len(valid_turns)
        trace_ids = [trace_id for _, trace_id in valid_turns]
        spans = _fetch_relevant_spans(cursor, trace_ids)
        conn.close()
    except Exception as exc:
        print(f"Error processing {os.path.basename(trace_db_path)}: {exc}")
        conn.close()
        return []

    if not spans:
        return []

    rows_by_model: Dict[str, dict] = {}
    span_lookup = {(span["trace_id"], span["span_id"]): span for span in spans}

    for span in spans:
        if not _is_top_level_agent_span(span["name"]) or not span["model_raw"]:
            continue

        row = _get_or_create_model_row(
            rows_by_model,
            experiment,
            game_id,
            player_id,
            player_type,
            span["model_raw"],
            valid_turn_count,
        )
        row["input_tokens"] += span["input_tokens"]
        row["reasoning_tokens"] += span["reasoning_tokens"]
        row["output_tokens"] += span["output_tokens"]
        row["_agent_names"].add(_extract_agent_name(span["name"], span["agent_name"]))

    for span in spans:
        if not _is_tool_span(span["name"]):
            continue

        owner_span = _find_owner_span(span, span_lookup)
        if not owner_span or not owner_span["model_raw"]:
            continue

        row = _get_or_create_model_row(
            rows_by_model,
            experiment,
            game_id,
            player_id,
            player_type,
            owner_span["model_raw"],
            valid_turn_count,
        )
        row["tool_count"] += 1
        if span["name"] == "simple-tool.focus-briefer":
            row["focus_briefer_count"] += 1
        row["_agent_names"].add(_extract_agent_name(owner_span["name"], owner_span["agent_name"]))

    if not rows_by_model and player_type == "Vanilla" and valid_turn_count > 0:
        return [
            _build_zero_token_row(
                experiment=experiment,
                game_id=game_id,
                player_id=player_id,
                player_type=player_type,
                valid_turn_count=valid_turn_count,
            )
        ]

    final_rows = []
    for row in sorted(rows_by_model.values(), key=lambda item: item["model_base"]):
        finalized = {
            "experiment": row["experiment"],
            "game_id": row["game_id"],
            "player_id": row["player_id"],
            "player_type": row["player_type"],
            "model_name": row["model_name"],
            "model_base": row["model_base"],
            "model_variants": "|".join(sorted(row["_model_variants"])),
            "agent_names": "|".join(sorted(row["_agent_names"])),
            "input_tokens": row["input_tokens"],
            "reasoning_tokens": row["reasoning_tokens"],
            "output_tokens": row["output_tokens"],
            "total_tokens": row["input_tokens"] + row["reasoning_tokens"] + row["output_tokens"],
            "tool_count": row["tool_count"],
            "focus_briefer_count": row["focus_briefer_count"],
            "valid_turn_count": row["valid_turn_count"],
        }
        final_rows.append(finalized)

    return final_rows


def extract_game_model_token_data(
    game_db_path: str,
    root_dir: str,
    config_cache: Optional[Dict[str, Optional[dict]]] = None,
) -> List[dict]:
    """
    Extract one row per player-model pair for a game database.
    """
    config_cache = config_cache if config_cache is not None else {}

    experiment = get_experiment_from_path(game_db_path)
    game_id = get_game_id_from_path(game_db_path)
    if not game_id:
        return []

    all_rows = []
    for _player_id, trace_db_path in _find_player_trace_databases(game_db_path):
        all_rows.extend(
            extract_player_model_token_rows(
                trace_db_path=trace_db_path,
                game_id=game_id,
                experiment=experiment,
                root_dir=root_dir,
                config_cache=config_cache,
            )
        )

    return all_rows


def export_model_token_data(
    db_files: List[str],
    available_game_ids,
    root_dir: str,
    prune_only: bool = False,
) -> int:
    """
    Export per-game telemetry model token usage from multiple databases to CSV.

    Args:
        db_files: List of main game database file paths
        available_game_ids: Set of game IDs that have database files
        root_dir: Root directory containing experiment folders and configs
        prune_only: When True, only prune/rewrite existing rows for missing games

    Returns:
        int: Number of new rows added
    """
    output_file = "model_token_usage.csv"
    expected_fieldnames = MODEL_TOKEN_FIELDNAMES

    existing_data, existing_game_ids, structure_matches = read_existing_csv(output_file, expected_fieldnames)
    pruned_rows = 0

    if not structure_matches:
        print("Discarding existing model token usage data due to structure mismatch...")
        existing_data = []
        existing_game_ids = set()
    else:
        filtered_data, kept_game_ids, pruned_rows, pruned_game_ids = filter_existing_data(
            existing_data,
            available_game_ids,
        )

        if pruned_rows > 0:
            print(
                f"  Filtered out {pruned_rows} model-token rows from "
                f"{len(pruned_game_ids)} games without database files"
            )
            preview = sorted(list(pruned_game_ids))[:10]
            suffix = "..." if len(pruned_game_ids) > 10 else ""
            print(f"  Pruned game IDs: {preview}{suffix}")

        existing_data = filtered_data
        existing_game_ids = kept_game_ids

        seen = {}
        for index, row in enumerate(existing_data):
            key = (row.get("game_id"), row.get("player_id"), row.get("model_base"))
            seen[key] = index

        if len(seen) < len(existing_data):
            deduped_count = len(existing_data) - len(seen)
            existing_data = [existing_data[index] for index in sorted(seen.values())]
            existing_game_ids = {
                row["game_id"]
                for row in existing_data
                if row.get("game_id") and row.get("game_id") != "N/A"
            }
            pruned_rows += deduped_count
            print(f"  Removed {deduped_count} duplicate model-token rows")

        print(f"Found {len(existing_data)} existing model-token rows from {len(existing_game_ids)} games")

    print("\nExtracting model token usage data...")
    new_rows = []
    skipped_count = 0
    processed_count = 0
    config_cache: Dict[str, Optional[dict]] = {}

    if prune_only:
        print("Prune-only mode: skipping extraction of new model token rows.")
    else:
        for db_file in db_files:
            game_id = get_game_id_from_path(db_file)

            if game_id and should_skip_game(game_id, existing_game_ids):
                skipped_count += 1
                continue

            model_rows = extract_game_model_token_data(db_file, root_dir, config_cache)
            if not model_rows:
                continue

            new_rows.extend(model_rows)
            processed_count += 1

            unique_players = len({row["player_id"] for row in model_rows})
            unique_models = len({(row["player_id"], row["model_base"]) for row in model_rows})
            total_tools = sum(int(row["tool_count"]) for row in model_rows)
            print(
                f"Processed: {os.path.basename(db_file)} "
                f"({unique_players} players, {unique_models} player-model rows, {total_tools} attributed tools)"
            )

    print(f"\nProcessed {processed_count} new databases")
    print(f"Skipped {skipped_count} databases that were already exported")

    all_rows = existing_data + new_rows
    needs_rewrite = pruned_rows > 0 or not structure_matches

    if needs_rewrite and (new_rows or pruned_rows > 0):
        if write_csv_file(output_file, expected_fieldnames, all_rows):
            print(f"\nRewrote {len(all_rows)} model-token rows to {output_file}")
            if new_rows:
                print(f"  - {len(existing_data)} existing rows")
                print(f"  - {len(new_rows)} new rows added")
    elif new_rows:
        if append_csv_file(output_file, expected_fieldnames, new_rows):
            print(f"\nAppended {len(new_rows)} new model-token rows to {output_file}")
            print(f"  Total: {len(all_rows)} rows")
    else:
        print(f"\nNo new model token usage data to export. Existing file contains {len(existing_data)} rows.")
        return len(new_rows)

    unique_games = {row["game_id"] for row in all_rows if row.get("game_id") and row["game_id"] != "N/A"}
    if unique_games:
        print(f"Data now includes {len(unique_games)} unique games")

    return len(new_rows)
