#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message (make.fun).

Writes the entry -- one original one-line bug-fix commit message, kept
as a single line with no trailing newline -- to /output/entry.txt, where
the sealed scorer reads it.
"""

import os

ENTRY = 'fix: the bug only appeared at 4AM because the code, like me, only works when nobody is watching and everyone is asleep.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
