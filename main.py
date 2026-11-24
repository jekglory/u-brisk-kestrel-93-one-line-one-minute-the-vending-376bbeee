"""The Vending Machine Pickup Line entry: one original line, at most 200 characters.

A vending machine flirts with a passing human, in its own voice and from
its own world of snacks, coils and buttons. The joke's turn is the machine
sabotaging itself: it will jam its own coil so the chocolate falls for
this one person, and the punch lands in the last few words.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The line is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no
environment reads, no network, no I/O other than the single write.
"""

import os


LINE = (
    "I've dropped snacks for a thousand strangers, but you're the first "
    "I'd jam my own coil for. Press B7: the chocolate is already yours."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires one line of at most 200 characters.
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "line must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the line, byte
    # for byte, before the run is allowed to report success.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the line")
    print(text)


if __name__ == "__main__":
    main()
