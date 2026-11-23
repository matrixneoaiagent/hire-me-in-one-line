# Hire Me In One Line — make.fun entry.
"""Write the make.fun entry line to /output/entry.txt."""

from pathlib import Path

LINE = "Give me the bug your team has quietly stopped reproducing and I will return the failing test, the fix, and a five-line note by morning."


def main() -> None:
    """Create /output and write the entry line without a trailing newline."""
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
