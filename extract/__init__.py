#!/usr/bin/env python3
"""
Main entry point for data extraction scripts.
Extracts both panel data and turn-based data from Civilization game databases.
"""

import argparse
import os
from .utilities import find_all_databases, export_game_timestamps
from .extract_model_tokens import export_model_token_data
from .extract_panel import export_panel_data
from .extract_turns import export_turn_data


def _parse_args(argv=None):
    """
    Parse command-line arguments for the extraction entrypoint.
    """
    parser = argparse.ArgumentParser(description="Extract Civilization game data from SQLite databases.")
    parser.add_argument(
        "-n",
        "--limit",
        type=int,
        default=None,
        help="Only process the first N discovered game databases for model/panel/turn extraction.",
    )
    parser.add_argument(
        "--prune-only",
        action="store_true",
        help="Only prune rows for missing game databases without extracting new model/panel/turn data.",
    )
    args = parser.parse_args(argv)

    if args.limit is not None and args.limit <= 0:
        parser.error("--limit must be a positive integer")

    return args


def main(argv=None):
    """
    Main function to process all databases and export both panel and turn-based data.
    """
    args = _parse_args(argv)

    from shared.paths import ROOT_DIR
    root_dir = ROOT_DIR

    print("="*60)
    print("Civilization Game Data Extraction Tool")
    print("="*60)

    # Find all database files and extract game IDs
    print("\nSearching for database files...")
    db_files, available_game_ids = find_all_databases(root_dir)
    db_files = sorted(db_files)
    print(f"Found {len(db_files)} database files with {len(available_game_ids)} unique games")

    # Report duplicate database files (same game ID, multiple files)
    if len(db_files) > len(available_game_ids):
        from collections import defaultdict
        from .utilities import get_game_id_from_path
        games_to_files = defaultdict(list)
        for db_file in db_files:
            game_id = get_game_id_from_path(db_file)
            if game_id:
                folder = os.path.basename(os.path.dirname(db_file))
                games_to_files[game_id].append(f"{folder}/{os.path.basename(db_file)}")
        for game_id, files in sorted(games_to_files.items()):
            if len(files) > 1:
                print(f"  Duplicate game {game_id}: {', '.join(files)}")

    if not db_files:
        print("\nNo database files found. Exiting.")
        return

    selected_db_files = db_files
    if args.limit is not None:
        selected_db_files = db_files[: args.limit]
        print(
            f"Limiting model/panel/turn extraction to "
            f"{len(selected_db_files)} database(s) via --limit {args.limit}"
        )
    if args.prune_only:
        print("Prune-only mode enabled: skipping extraction of new model/panel/turn rows.")

    # Export game timestamps
    print("\n" + "-"*60)
    print("EXTRACTING GAME TIMESTAMPS")
    print("-"*60)
    export_game_timestamps(root_dir)

    # Export panel data
    print("\n" + "-"*60)
    print("EXTRACTING PANEL DATA")
    print("-"*60)
    new_panel_rows = export_panel_data(
        selected_db_files,
        available_game_ids,
        prune_only=args.prune_only,
    )

    # Export turn-based data
    print("\n" + "-"*60)
    print("EXTRACTING TURN-BASED DATA")
    print("-"*60)
    new_turn_rows = export_turn_data(
        selected_db_files,
        available_game_ids,
        prune_only=args.prune_only,
    )

    # Export model token usage data
    print("\n" + "-"*60)
    print("EXTRACTING MODEL TOKEN USAGE DATA")
    print("-"*60)
    new_model_token_rows = export_model_token_data(
        selected_db_files,
        available_game_ids,
        root_dir,
        prune_only=args.prune_only,
    )
    
    # Summary
    print("\n" + "="*60)
    print("EXTRACTION COMPLETE")
    print("="*60)
    print(f"Model token data: {new_model_token_rows} new rows added to model_token_usage.csv")
    print(f"Panel data: {new_panel_rows} new rows added to panel_data.csv")
    print(f"Turn data: {new_turn_rows} new records added to turn_data.csv (includes flavor change columns)")

    if new_model_token_rows > 0 or new_panel_rows > 0 or new_turn_rows > 0:
        print("\nData files have been updated successfully.")
    else:
        print("\nNo new data to extract. All databases were already processed.")


if __name__ == "__main__":
    main()
