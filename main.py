#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — entry writer.

Writes exactly one job title (a single line) to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (default: /output).
Pure Python standard library only.
"""

import os

TITLE = "Director of Renaming Files to final_v2_REAL_final.xlsx"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TITLE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
