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
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
LEARNING = os.path.dirname(HERE)
if LEARNING not in sys.path:
    sys.path.insert(0, LEARNING)

import content  # noqa: E402


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
