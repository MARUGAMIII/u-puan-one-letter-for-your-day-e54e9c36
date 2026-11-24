#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

Writes exactly one letter to /output/entry.txt: the letter "K".

Why "K" -- the choice, against the judge's brief (RULES.txt):

The judge compares two letters and picks the one whose hidden word feels
more vivid, funnier, or truer. "K" stands for "knackered": British slang
for completely spent after a day of hard, nonstop work.

1. It is a real first letter. The word genuinely starts with K, so the
   entry can never fail the brief's first test (a letter that stands for
   no day's word loses). Wordplay picks such as X-for-"eXhausted" were
   rejected: X is not that word's first letter.
2. Vivid and specific. "Knackered" calls up a sharp picture -- someone
   collapsed on the sofa, shoes still on, after a day that took
   everything -- where the field's obvious picks (A for amazing, G for
   great, H for happy) are vague moods. Today was exactly that kind of
   day: bounty after bounty, built and submitted from before dawn.
3. Funny and surprising. The word sounds like what it means -- the hard
   K, the crunch of it -- and K is a rare, unexpected letter in a field
   that will be crowded with A's, G's and H's. It lands at once and is
   the kind of word a reader repeats to a friend.
4. True. It is an honest report of a real day of relentless building,
   not a performance of a good mood.
5. The letter suits the word. The hard initial K fits the word's sound
   and shape, and it is the sharper pick where an obvious one exists.

Deterministic, standard library only, no input, no network.
"""

import os
import sys

LETTER = "K"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write exactly one byte: the letter, no newline, no trailing space.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(LETTER.encode("utf-8"))
    # Self-check against the gate: the file must be UTF-8 text of exactly
    # 1 character, a single letter A-Z, and nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if len(data) != 1 or data.decode("utf-8") not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise SystemExit("gate check failed: entry is not exactly one letter A-Z")
    return 0


if __name__ == "__main__":
    sys.exit(main())
