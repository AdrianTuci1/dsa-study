#!/usr/bin/env python3
"""Validate the study content sources.

Reads the same files as the server, runs every check, prints a summary, and
writes nothing:

    python3 learning/build_study.py

Sources:
    learning/study_bank.py
    learning/study_extras.py
    learning/solve_bank.py
    learning/study/graph.json
"""

import sys

from content import ContentError, build_content


def main():
    try:
        data = build_content()
    except ContentError as exc:
        print("Content problems:")
        for issue in exc.issues:
            print("  -", issue)
        return 1

    meta = data["meta"]
    print("Drills: %d %s" % (meta["items"], meta["counts"]))
    print("Problems: %d (%d variants)" % (meta["problems"], meta["variants"]))
    print("Practice: %d problems (%d stubs)" % (meta["practice"], meta["practice_stubs"]))
    print("Graph: %d nodes, %d edges" % (meta["nodes"], meta["edges"]))
    for warning in meta.get("warnings") or []:
        print("warning:", warning)
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
