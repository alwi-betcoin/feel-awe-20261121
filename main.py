"""Write one relaxation text to /output/entry.txt.

make.fun competition make-the-ai-judge-feel-awe-20261121-1600.
Deterministic: the text is a literal, written exactly as-is, UTF-8,
no trailing newline. Standard library only, no network, no file reads.
"""

import os

TEXT = (
    "The light on this page left its star before there were words for light. "
    "It crossed the dark without hurrying, and it arrives now, quietly. "
    "The star is gone. The light is still coming."
)

# Guard: the judge's gate requires 1-280 Unicode code points.
if not 1 <= len(TEXT) <= 280:
    raise ValueError(f"entry text must be 1-280 code points, got {len(TEXT)}")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
