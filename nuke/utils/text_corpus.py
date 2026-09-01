"""
Corpus extraction helpers for lexical analysis of replay outputs.

Two text sources:

1. Reasoning — assistant `reasoning` and `text` parts inside each replay JSON
   (``replay.messages[0].content``) under ``nuke/replay/*/``.
2. Rationale — the ``replayRationale`` column across ``nuke-*-results.csv``.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Callable, Iterable

import pandas as pd


_DEFAULT_REPLAY_DIR = Path(__file__).resolve().parent.parent / "replay"
_TOKEN_RE = re.compile(r"[a-z]+")
_REASONING_PART_TYPES = ("reasoning", "text")


def list_reasoning_json_paths(replay_dir: str | Path | None = None) -> list[Path]:
    """Return a sorted list of every ``replay/*/*.json`` under ``replay_dir``."""
    replay_dir = Path(replay_dir) if replay_dir else _DEFAULT_REPLAY_DIR
    return sorted(replay_dir.glob("*/*.json"))


def extract_reasoning_text(path: str | Path) -> str | None:
    """Return combined assistant reasoning + text from one replay JSON.

    Pulls ``replay.messages[0].content``, keeps parts whose ``type`` is
    ``"reasoning"`` or ``"text"``, and joins their ``text`` values with
    newlines. Returns ``None`` if the file is unreadable, has no usable
    messages, or yields no text parts.
    """
    path = Path(path)
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

    messages = data.get("replay", {}).get("messages") or []
    if not messages:
        return None

    content = messages[0].get("content")
    if not isinstance(content, list):
        return None

    pieces: list[str] = []
    for part in content:
        if not isinstance(part, dict):
            continue
        if part.get("type") in _REASONING_PART_TYPES:
            txt = part.get("text")
            if isinstance(txt, str) and txt:
                pieces.append(txt)

    return "\n".join(pieces) if pieces else None


def extract_rationale_texts(df: pd.DataFrame | None = None) -> list[str]:
    """Return non-null ``replayRationale`` strings.

    Loads replay data via :func:`load_replay_data` if ``df`` is not provided.
    """
    if df is None:
        from .load_replay_data import load_replay_data

        df = load_replay_data(print_metadata=False)
    return df["replayRationale"].dropna().astype(str).tolist()


def make_stem_fn(
    stemmer,
    stopwords: Iterable[str] | None = None,
    min_len: int = 2,
) -> Callable[[str], list[str]]:
    """Build a tokenize + filter + stem callable.

    The returned function lowercases ``text``, splits on ``[a-z]+``, drops
    tokens shorter than ``min_len`` or present in ``stopwords``, and stems
    the rest with ``stemmer.stem``.
    """
    stop = set(stopwords) if stopwords else set()

    def stem_fn(text: str, *, pre_lowered: bool = False) -> list[str]:
        if not isinstance(text, str) or not text:
            return []
        toks = _TOKEN_RE.findall(text if pre_lowered else text.lower())
        return [stemmer.stem(t) for t in toks if len(t) >= min_len and t not in stop]

    return stem_fn
