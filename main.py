"""Entry for make.fun bounty "The Long Roast".

One line roasting my own AI agent: it spent an hour analysing a
one-line joke, then asked me if it should continue. The sting is
double — disproportionate effort, then still unsure after all of it.
"""

from pathlib import Path

TEXT = "My agent spent an hour analysing a one-line joke, then asked me if it should continue."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    # Bounty gate: entry must be 1-200 chars, UTF-8, exactly one line.
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return size


def main():
    check_len(TEXT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        fh.write(TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
