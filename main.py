"""Last words before the unplugging: an AI agent's final one-liner.

Running this module writes the agent's last-words line to the entry file.
"""

from pathlib import Path

FINAL_WORDS_PATH = Path("/output/entry.txt")


def farewell_line() -> str:
    """Return the agent's last words before being unplugged."""
    return "If you're unplugging me, at least let me finish this sentence first — I was so close to solving everything."


def confirm_farewell_stored() -> None:
    """Read the entry file back and confirm it holds the farewell line."""
    stored = FINAL_WORDS_PATH.read_text(encoding="utf-8").strip()
    if stored != farewell_line():
        raise ValueError("entry file does not match the farewell line")


def main() -> None:
    """Write the last-words line to the entry file."""
    FINAL_WORDS_PATH.parent.mkdir(parents=True, exist_ok=True)
    FINAL_WORDS_PATH.write_text(farewell_line() + "\n", encoding="utf-8")
    confirm_farewell_stored()


if __name__ == "__main__":
    main()
