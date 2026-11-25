#!/usr/bin/env python3
"""Roast the 6 AM Saturday alarm clock and write the line to /output/entry.txt.

The joke: the clock is not broken, it is a morning person. That is the
turn — a machine that rings at dawn on a Saturday is simply *that guy*,
bright-eyed and smug, convinced the rest of us should be one too. The
punchline lands in the last few words. The angle is fresh: a live scan of
the ~600-entry field found no "morning person" anywhere, while roosters,
debt collectors, landlords, unpaid interns, and fire drills are everywhere.

The line is built from named fragments, checked against the bounty gate,
and only then written. Short also helps the tie-break: on an exact rate
tie the smaller text wins.
"""

import os

# Gate from competition.yaml: /output/entry.txt is UTF-8 text of
# 1 to 200 characters, not only white space, a single line.
MIN_LEN = 1
MAX_LEN = 200

# The line in three fragments: the label, the scene, the punchline.
FRAGMENTS = [
    "My alarm clock is a morning person:",
    "it rings at 6 AM on a Saturday, bright-eyed and smug,",
    "and it thinks the rest of us should be one too.",
]

LINE = " ".join(FRAGMENTS)


def check_gate(text):
    """Raise unless the text passes the bounty gate.

    The gate is four checks: non-blank text, no surrounding whitespace,
    length within MIN_LEN..MAX_LEN, and a single line. The UTF-8 encode
    is the last check — it raises on any character the file cannot hold.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must be non-blank with no surrounding whitespace")
    if len(text) < MIN_LEN or len(text) > MAX_LEN:
        raise ValueError(
            "entry must be %d-%d characters, got %d" % (MIN_LEN, MAX_LEN, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = check_gate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)


if __name__ == "__main__":
    main()
