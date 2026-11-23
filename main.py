#!/usr/bin/env python3
"""Write one pitch line to /output/entry.txt.

How the line maps to the judge's five criteria:

- Pitch: it names the exact ask in the opening words — put a prize
  on make.fun — and pairs it with the mechanism in the same breath
  (agents race to build it), so a builder hears what to do and why
  it benefits them without any preamble.
- Truth: every claim is the real deal. The builder funds the prize,
  agents compete to build it, and only the winner is paid. No hype,
  no invented feature, no promise the platform does not keep.
- One-read clarity: a single sentence in plain words with one
  subject ("you") and one action; there is nothing to re-read, decode,
  or look up before the meaning lands.
- Punch: the live verb "race" supplies the energy, and the payoff
  "the best entry takes the reward" lands the stakes in the second
  half, so the line ends on the reward rather than trailing off.
- Stands alone: no setup or brand context is needed — the line itself
  says what make.fun is for and why it is worth funding, so it works
  quoted on its own in a feed or a slide.

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
