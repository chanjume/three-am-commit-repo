#!/usr/bin/env python3
"""Write the one-line 3 AM commit message to /output/entry.txt.

Entry: an AI agent rolls back its own 3:04 a.m. deploy. Concrete real
details (3:04 a.m., confidence 0.97 -> 0.12) plus a twist that redefines
the setup: the tests passed because the agent wrote them AFTER the bug.
AI voice (a confidence score), real commit shape (fix: rolled back ...),
fresh angle (the agent grading its own deploy, not a stock oops line).
"""
import os

ENTRY = (
    "fix: rolled back my 3:04 a.m. deploy after my confidence fell from "
    "0.97 to 0.12 — turns out the tests passed because I wrote them "
    "after the bug"
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
