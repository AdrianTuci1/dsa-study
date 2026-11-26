#!/usr/bin/env python3
"""Serve the study app and its content API.

    python3 learning/study/serve.py                  # 127.0.0.1:8765
    python3 learning/study/serve.py --host 0.0.0.0   # in Docker
    open http://127.0.0.1:8765/

`/api/content` is rebuilt from the source files on every request:

    learning/study_bank.py
    learning/study_extras.py
    learning/solve_bank.py
    learning/study/graph.json

So editing any of those and reloading the page is enough: there is no build
step and no content hardcoded in JavaScript.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
LEARNING = os.path.dirname(HERE)
if LEARNING not in sys.path:
    sys.path.insert(0, LEARNING)

import content  # noqa: E402

RUNNER = os.path.join(HERE, "run_practice.py")


def run_sheet(problem_id, code):
    """Execute the sheet in a subprocess against the practice tests."""
    if not isinstance(problem_id, str) or not isinstance(code, str):
        return {"error": "problem_id and code are required."}
    if len(code) > 60000:
        return {"error": "Code is too long (max 60 KB)."}

    try:
        data = content.build_content()
    except content.ContentError as exc:
        return {"error": "Content validation failed. " + " ".join(exc.issues)}

    problem = next((item for item in data["practice"] if item["id"] == problem_id), None)
    if not problem:
        return {"error": "Unknown practice problem."}
    if not problem.get("runnable") or not problem.get("function"):
        return {"error": "This problem has no runnable tests."}
    function = problem["function"]
    if not re.fullmatch(r"[A-Za-z_]\w*", function):
        return {"error": "Invalid function name."}

    repo_root = os.path.dirname(LEARNING)
    practice_root = os.path.realpath(os.path.join(repo_root, "practice"))
    practice_path = os.path.realpath(os.path.join(repo_root, problem["source"]))
    if not practice_path.startswith(practice_root + os.sep) or not os.path.isfile(practice_path):
        return {"error": "Practice file not found."}

    with tempfile.TemporaryDirectory(prefix="dsa-run-") as tmp:
        sheet_path = os.path.join(tmp, "sheet.py")
        result_path = os.path.join(tmp, "result.json")
        with open(sheet_path, "w", encoding="utf-8") as handle:
            handle.write(code)

        try:
            process = subprocess.run(
                [sys.executable, RUNNER, practice_path, function, sheet_path, result_path],
                cwd=tmp,
                capture_output=True,
                text=True,
                timeout=8,
            )
        except subprocess.TimeoutExpired:
            return {"error": "Timed out after 8 seconds. Is there an infinite loop?"}
        except OSError as exc:
            return {"error": "Cannot run the tests: %s" % exc}

        if os.path.exists(result_path):
            try:
                with open(result_path, "r", encoding="utf-8") as handle:
                    return json.load(handle)
            except (OSError, ValueError):
                return {"error": "Could not read the test result."}

        tail = (process.stderr or "").strip().splitlines()
        return {"error": "Test runner failed: " + (tail[-1] if tail else "no output")}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/api/content":
            try:
                payload = content.build_content()
            except content.ContentError as exc:
                self.send_json(500, {
                    "error": "Content validation failed",
                    "problems": exc.issues,
                })
                return
            except Exception as exc:  # noqa: BLE001 - surface the source error
                self.send_json(500, {
                    "error": "%s: %s" % (type(exc).__name__, exc),
                    "problems": [],
                })
                return
            self.send_json(200, payload)
            return
        super().do_GET()

    def do_POST(self):
        if self.path.split("?", 1)[0] != "/api/run":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0") or 0)
        except ValueError:
            length = 0
        if length <= 0 or length > 120000:
            self.send_json(400, {"error": "Invalid request size."})
            return
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            self.send_json(400, {"error": "Invalid JSON."})
            return
        if not isinstance(payload, dict):
            self.send_json(400, {"error": "Expected a JSON object."})
            return
        result = run_sheet(payload.get("problem_id", ""), payload.get("code", ""))
        self.send_json(200, result)

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))


def main():
    parser = argparse.ArgumentParser(description="Serve the DSA study app and /api/content.")
    parser.add_argument("--host", default="127.0.0.1", help="bind address (0.0.0.0 inside Docker)")
    parser.add_argument("--port", type=int, default=8765, help="port (default 8765)")
    args = parser.parse_args()

    try:
        server = ThreadingHTTPServer((args.host, args.port), Handler)
    except OSError as exc:
        print("cannot bind %s:%d: %s" % (args.host, args.port, exc))
        print("Is another server already using the port?")
        return 1
    display = "127.0.0.1" if args.host in ("0.0.0.0", "::") else args.host
    print("DSA Study: http://%s:%d/" % (display, args.port))
    print("Content source: %s (read on every /api/content request)" % LEARNING)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
