#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics rejected to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.

The line: a made-up event that sounds like a real broadcast,
absurd enough to be funny, short enough to quote.
"""

import os
import sys

MAX_CHARS = 200  # gate: entry.txt must be 1-200 characters, UTF-8

LINE = (
    "Synchronized sighing: two athletes exhale in perfect unison "
    "while judges deduct points for sounding relieved."
)


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}",
              file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
