#!/usr/bin/env python3
"""Run the user's sheet against the tests stored in a practice file.

Usage:
    python3 run_practice.py <practice.py> <function> <sheet.py> <result.json>

The result file receives:

    {"passed": 2, "total": 4, "results": [
        {"label": "...", "passed": true, "expected": "...", "got": "...", "error": ""},
        ...
    ]}

or {"error": "..."} when the sheet cannot be executed.

The practice file is the source of truth for the tests: its
`if __name__ == "__main__":` block is executed with a capturing `run()` so we
can collect `(label, function, args, expected)` tuples without printing.
"""

import ast
import json
import os
import sys
import textwrap


def write_result(path, payload):
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False)
    return 0


def main(argv):
    if len(argv) != 5:
        sys.stderr.write("usage: run_practice.py <practice.py> <function> <sheet.py> <result.json>\n")
        return 2

    practice_path, function_name, sheet_path, result_path = argv[1:]
    practice_dir = os.path.dirname(os.path.abspath(practice_path))
    if practice_dir not in sys.path:
        sys.path.insert(0, practice_dir)

    try:
        import resource

        resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    except Exception:  # noqa: BLE001 - not available on every platform
        pass

    with open(practice_path, "r", encoding="utf-8") as handle:
        source = handle.read()

    marker = 'if __name__ == "__main__":'
    index = source.find(marker)
    if index < 0:
        return write_result(result_path, {"error": "This practice file has no tests block."})

    prefix = source[:index]
    tests_block = textwrap.dedent(source[index + len(marker):])

    namespace = {"__name__": "practice_source", "__file__": practice_path}
    try:
        exec(compile(prefix, practice_path, "exec"), namespace)
    except BaseException as exc:  # noqa: BLE001
        return write_result(result_path, {
            "error": "Cannot load practice file: %s: %s" % (type(exc).__name__, exc),
        })

    captured = []

    def capture_run(label, fn, args, expected):
        captured.append((label, getattr(fn, "__name__", ""), args, expected))
        return True

    def capture_summary(_results):
        return None

    namespace["run"] = capture_run
    namespace["summary"] = capture_summary
    try:
        exec(compile(tests_block, practice_path, "exec"), namespace)
    except BaseException as exc:  # noqa: BLE001
        return write_result(result_path, {
            "error": "Cannot read the practice tests: %s: %s" % (type(exc).__name__, exc),
        })

    tests = [
        (label, args, expected)
        for label, name, args, expected in captured
        if name == function_name
    ]
    if not tests:
        return write_result(result_path, {
            "error": "No tests found for `%s` in %s." % (function_name, os.path.basename(practice_path)),
        })

    with open(sheet_path, "r", encoding="utf-8") as handle:
        sheet = handle.read()

    # The sheet may rely on the imports at the top of the practice file
    # (heapq, deque, ...). Copy only the imports, never the reference
    # functions, otherwise a sheet could pass without defining anything.
    user = {"__name__": "__main__"}
    try:
        prefix_tree = ast.parse(prefix)
    except SyntaxError:
        prefix_tree = None
    if prefix_tree:
        for node in prefix_tree.body:
            if isinstance(node, ast.ImportFrom) and node.module == "_harness":
                continue
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                try:
                    exec(
                        compile(ast.Module(body=[node], type_ignores=[]), practice_path, "exec"),
                        user,
                    )
                except Exception:  # noqa: BLE001 - optional import
                    pass

    try:
        exec(compile(sheet, "sheet.py", "exec"), user)
    except BaseException as exc:  # noqa: BLE001
        return write_result(result_path, {
            "error": "Your code raised %s: %s" % (type(exc).__name__, exc),
        })

    fn = user.get(function_name)
    if not callable(fn):
        return write_result(result_path, {
            "error": "Your sheet must define `def %s(...)`. The practice tests call that name." % function_name,
        })

    results = []
    for label, args, expected in tests:
        try:
            got = fn(*args)
            results.append({
                "label": label,
                "passed": got == expected,
                "expected": repr(expected)[:300],
                "got": repr(got)[:300],
                "error": "",
            })
        except BaseException as exc:  # noqa: BLE001
            results.append({
                "label": label,
                "passed": False,
                "expected": repr(expected)[:300],
                "got": "",
                "error": "%s: %s" % (type(exc).__name__, exc),
            })

    passed = sum(1 for item in results if item["passed"])
    return write_result(result_path, {
        "passed": passed,
        "total": len(results),
        "results": results,
    })


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
