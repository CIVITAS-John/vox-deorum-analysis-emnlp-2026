"""Concatenate per-model coded_quotes_*.csv files into a single coded_quotes.csv."""

import csv
import glob
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: python concat_coded_quotes.py <coding_directory>")
        sys.exit(1)

    coding_dir = Path(sys.argv[1])
    if not coding_dir.is_dir():
        print(f"Error: {coding_dir} is not a directory")
        sys.exit(1)

    files = sorted(glob.glob(str(coding_dir / "coded_quotes_*.csv")))
    if not files:
        print(f"No coded_quotes_*.csv files found in {coding_dir}")
        sys.exit(1)

    header = None
    all_rows = []

    for fpath in files:
        with open(fpath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            file_header = next(reader)
            if header is None:
                header = file_header
            elif file_header != header:
                print(f"Warning: header mismatch in {fpath}, skipping")
                continue
            all_rows.extend(reader)

    out_path = coding_dir / "coded_quotes.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(all_rows)

    print(f"Concatenated {len(files)} files, {len(all_rows)} rows → {out_path}")


if __name__ == "__main__":
    main()
