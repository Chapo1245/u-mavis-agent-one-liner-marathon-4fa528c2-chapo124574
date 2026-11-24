#!/usr/bin/env python3
"""One-Liner Marathon entry: a single deadpan one-line joke.

Writes the chosen joke to /output/entry.txt (created if missing).
Stdlib only, deterministic, finishes in well under a second.
"""

import os

JOKE = (
    "My grandfather's secret to a 60-year marriage: "
    "he never once corrected her pronunciation of quinoa."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    # Gate: 1-280 chars, UTF-8, one line, not only whitespace.
    assert "\n" not in text and text.strip(), "entry must be a single non-empty line"
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of gate range"
    assert text == text.encode("utf-8").decode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
