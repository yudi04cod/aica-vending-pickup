"""Aica Vending Pickup — one pickup line, as spoken by a vending machine.

Writes the entry to /output/entry.txt (stdlib only).
"""

import os

ENTRY = (
    "I've got forty snacks, exact change, and one coil that only jams "
    "for the cute ones \u2014 go ahead, press my buttons and see what drops."
)


def validate(text: str) -> None:
    """Check the entry against the gate: 1-200 chars, one line, not blank."""
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
