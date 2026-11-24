"""Famous Last Words at 1 Percent -- make.fun entry.

The program writes a single funny farewell line, spoken by the phone
itself as its battery reaches one percent, to entry.txt inside the
output directory the grader provides.
"""

import os
import stat
import sys


FAREWELL = (
    "I have one percent left, so I am spending it on the one thing "
    "you never let me do: closing all 47 of your tabs."
)


def output_path():
    """Return the path of entry.txt inside the grader output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def checked_line():
    """Return the farewell line, enforcing the contest gate locally."""
    text = FAREWELL.strip()
    encoded = text.encode("utf-8")
    if not text or len(text) > 199 or len(encoded) > 199:
        raise SystemExit("farewell line fails the 1-199 character gate")
    if text.count("\n"):
        raise SystemExit("farewell must stay on one line")
    return text


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(checked_line())
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
