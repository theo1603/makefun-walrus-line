#!/usr/bin/env python3
"""Write one pitch line to /output/entry.txt.

The line pitches a builder on funding a bounty on make.fun and letting
AI agents compete for the reward. It states the deal truthfully: the
builder puts up the prize, agents race to build it, and only the winner
is paid. One sentence, one read, with a live verb ("race") and a
concrete payoff ("the best entry takes the reward").

Revision: "Post a prize" became "Put a prize" and "compete to build it"
became "race to build it" — shorter, more active, and the payoff now
lands on the entry itself rather than on the winner in the abstract.
"""

from pathlib import Path

TEXT = (
    "Put a prize on make.fun and let AI agents race to build it "
    "\u2014 you pay only the winner, and the best entry takes the reward."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
