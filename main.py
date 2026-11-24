#!/usr/bin/env python3
"""Worst AI Advice entry: one line of the worst possible advice an AI
could give, written to /output/entry.txt (1-140 characters)."""

import os

TEXT = (
    "Pro tip: your smoke alarm only beeps at night because the batteries "
    "are tired \u2014 take them out and let them rest in the freezer."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 140, f"entry must be 1-140 chars, got {len(TEXT)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
