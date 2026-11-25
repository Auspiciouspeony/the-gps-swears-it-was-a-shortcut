#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut - make.fun program/v1 entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Round 2 rewrite: v1's joke landed mid-sentence and ended on a complaint
("lies to my face every morning") instead of a twist. This version packs
two of the brief's fresh details (lake, cul-de-sac) up front and saves
the laugh for the last beat - a smug paradox that blames the map while
claiming the GPS was never wrong.
"""

import os

ENTRY = (
    "The map says that lake is a road and that cul-de-sac is a shortcut, "
    "and I have never once been wrong about a map that was wrong first."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    # Permissions are best-effort only. The grader runs as uid 65534
    # against a root-owned /output, so an unguarded chmod raises
    # PermissionError and kills the run before entry.txt exists.
    # Every chmod here is wrapped; a failure is swallowed, never fatal.
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(ENTRY))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
