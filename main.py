#!/usr/bin/env python3
"""Write the champion one-liner to /output/entry.txt.

Entry for make.fun competition
u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.

The line is the winner of an internal pairwise tournament over 16
candidate one-liners (see CANDIDATES.md). It is embedded here so the
program is fully self-contained: it reads nothing from the network,
the repository, or the environment.
"""

import os

ENTRY = "My cat knocked my laptop off the table during a job interview; the interviewer hired the cat."


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
