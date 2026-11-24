#!/usr/bin/env python3
"""Funniest Out-of-Office entry.

Writes one line of out-of-office auto-reply to /output/entry.txt.
The joke: the auto-reply itself has taken over the inbox -- and it
turns out to be better at the job than the person who left.
"""

import os

# The reply is built from labelled sections, so each part of the joke
# can be audited on its own: the setup names the absence, the handover
# is the twist, the punchline lands it. Every word has to earn its place.
SECTIONS = [
    ("setup", "Out of office until Friday."),
    ("handover", "My auto-reply is handling my inbox now,"),
    ("punch", "and frankly it's doing a better job than I ever did."),
]
MAX_CHARS = 140


def assemble(sections=SECTIONS) -> str:
    """Join the labelled sections into one single-line reply."""
    line = " ".join(text for _, text in sections)
    return " ".join(line.split())  # single line, no stray whitespace


def audit(line: str) -> dict:
    """Gate audit: length, single line, and a per-section word count."""
    report = {
        "chars": len(line),
        "lines": line.count("\n") + 1,
        "words": len(line.split()),
        "per_section": {label: len(text.split()) for label, text in SECTIONS},
    }
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if "\n" in line or not line.strip():
        raise ValueError("line must be a single non-blank line")
    return report


def main() -> None:
    line = assemble()
    report = audit(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    print(f"chars={report['chars']} lines={report['lines']} "
          f"words={report['words']} sections={report['per_section']}")


if __name__ == "__main__":
    main()
