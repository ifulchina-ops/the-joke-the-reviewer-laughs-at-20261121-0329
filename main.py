#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents to entry.txt.

Pure stdlib, no network. Output directory: $MAKEFUN_OUTPUT_DIR, else /output.
"""

import os
import sys

# The joke: the agent out-produces the human a hundredfold, yet the human
# does all the reviewing — so the seniority runs backwards.
JOKE = (
    "My AI agent writes 500 lines a minute and reviews none of them; "
    "I write five lines a day and review all of them \u2014 somehow I'm "
    "still the junior in this relationship."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"entry is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
