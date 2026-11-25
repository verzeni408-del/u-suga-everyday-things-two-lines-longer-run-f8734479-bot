#!/usr/bin/env python3
"""Entry writer for 'Everyday Things, Two Lines, Longer Run'.

Writes a two-line explanation of a kitchen sponge to /output/entry.txt
as UTF-8 with no trailing newline. Standard library only.
"""

import os

ENTRY = (
    "A kitchen sponge is like a soft brick full of little caves that "
    "gulps down a spill and squeezes it all back out when you press it.\n"
    "The caves match because they soak up water and a squeeze pushes it "
    "back out, but a sponge never feels thirsty and its caves are just "
    "empty pockets of air with no mouth at all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
