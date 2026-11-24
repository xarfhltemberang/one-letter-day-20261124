#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry (u-puan-one-letter-for-your-day-e54e9c36).

Writes exactly one character, "Z", to /output/entry.txt.

The letter behind the day: Z for zombie — a day spent shambling through
everything half-asleep on zero sleep. Vivid (a shambling zombie is a sharp
picture), funny (everyone has had a zombie day), true (an honest report of
a real day), and Z is the unmistakable initial of zombie.
"""

import os

LETTER = "Z"

if len(LETTER) != 1:
    raise ValueError("entry must be exactly one character")


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
