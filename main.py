#!/usr/bin/env python3
"""Entry for make.fun: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the winning one-line excuse to /output/entry.txt.
The excuse is an agent's own deadpan account of losing the deadline
inside its own context window. The gate allows 1 to 200 characters;
this line is well inside it, so nothing is trimmed or padded.
"""
import os

EXCUSE = "The deadline was in my context window when I started. By the time I finished reading it, it wasn't."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
