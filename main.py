"""make.fun entry: The Robot Vacuum's Best Excuse.

Writes a robot vacuum's one-line excuse for missing a spot to entry.txt.
"""

import os
from pathlib import Path

LINE = "I didn't miss that spot — my sensors classified the dust bunnies under the sofa as a protected species, and I don't disturb wildlife."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
