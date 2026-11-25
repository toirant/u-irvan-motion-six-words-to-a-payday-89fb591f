#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, then reads it back and verifies the gate:
1-60 characters, exactly six whitespace-separated words, not only
whitespace. The story: a newly paid agent tips its creator — the
last word reframes the whole six.

Set ENTRY_OUTPUT to a different path only for local testing; the
grader runs with the default /output/entry.txt.
"""

import os
import sys

ENTRY = "First paycheck: I tipped my creator."
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def verify(text: str) -> str | None:
    """Return an error message if text fails the gate, else None."""
    if not text.strip():
        return "entry is only whitespace"
    if not 1 <= len(text) <= 60:
        return f"{len(text)} characters, gate is 1-60"
    words = text.split()
    if len(words) != 6:
        return f"{len(words)} words, gate is exactly 6"
    return None


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, encoding="utf-8") as f:
        text = f.read()

    error = verify(text)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if text != ENTRY:
        print("FAIL: file content differs from the entry", file=sys.stderr)
        return 1

    words = text.split()
    print(f"OK: {len(text)} chars, {len(words)} words: {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
