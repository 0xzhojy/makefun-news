"""Copy the caller-rendered poster to the make.fun output directory."""

import os
from pathlib import Path
import sys


def main() -> int:
    source = Path(__file__).resolve().with_name("entry.png")
    try:
        image = source.read_bytes()
    except FileNotFoundError:
        print(f"Error: entry.png is absent: {source}", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(image)
    return 0


if __name__ == "__main__":
    sys.exit(main())
