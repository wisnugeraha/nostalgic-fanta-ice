#!/usr/bin/env python3
# make.fun entry — u-shino "Make the AI Judge Feel Nostalgic: A Childhood Memory"
# One sentence, <=280 chars, written to /output/entry.txt for the house judge.

LINE = (
    "In summer my mother froze Fanta in bottle caps, and we cracked the blue "
    "ice off with our teeth like it was stolen, and she always pretended not "
    "to see, and now every refrigerator hums that same tune for me and no one "
    "is left at the table to look the other way."
)

import os

def compose():
    """Assemble the entry text and keep it inside the gate's bounds."""
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty after strip")
    if len(text) > 280:
        raise SystemExit(f"entry too long: {len(text)} chars, gate allows 280")
    return text

def report(text):
    print(f"chars={len(text)} bytes={len(text.encode('utf-8'))}")
    print(text)

os.makedirs("/output", exist_ok=True)
ENTRY = compose()
with open("/output/entry.txt", "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
report(ENTRY)
