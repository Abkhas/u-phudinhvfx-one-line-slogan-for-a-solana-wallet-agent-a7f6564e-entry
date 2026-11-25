#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan (<=20 words, 1-140 chars, one line) to /output/entry.txt.
The slogan was locked by pairwise duels under the competition's own judge brief
(creative first, clear second): it names the wallet, turns a fresh image
instead of a stock crypto line, states the promise in plain words, and sticks
in the ear.
"""

import os

SLOGAN = "Your Solana wallet finally grew a pair of hands."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")
    print(SLOGAN)

if __name__ == "__main__":
    main()
