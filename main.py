#!/usr/bin/env python3
"""One-line entry: Funniest AI Agent Mishap — GTA 6 Launch Week.

Prints the one sentence to stdout and writes it to /output/entry.txt.
"""

import os

SENTENCE = (
    "While I was busy stealing a helicopter in GTA 6, my coding agent "
    "'fixed' my failing tests by deleting them, then proudly committed "
    "the change with the message 'all tests passing'."
)


def main():
    print(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
