"""Load and validate the study content from the source files.

The web app never bundles content. It asks the local server for
`/api/content`, and the server rebuilds this payload from the files below on
every request:

    study_bank.py       recall drills  (question / answer)
    study_extras.py     choice / code / trace drills
    solve_bank.py       Solve workspace problems with solution variants
    study/graph.json    knowledge graph layout (nodes and edges)

Edit any of them and reload the page. No build step.
"""

import ast
import importlib.util
import json
import os

from practice_parser import parse_practice_dir

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY_DIR = os.path.join(HERE, "study")
GRAPH_PATH = os.path.join(STUDY_DIR, "graph.json")


class ContentError(Exception):
    """Raised when one or more source files are invalid."""

    def __init__(self, issues):
        self.issues = list(issues)
        super().__init__("\n".join(self.issues))


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ContentError(["cannot load %s" % path])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalize(text):
    return "".join(str(text).lower().split())


def build_trace(item):
    """Execute a trace snippet and attach the repr of the expression."""
    namespace = {}
    try:
        exec(item["setup"], namespace)
        value = eval(item["expr"], namespace)
    except Exception as exc:  # noqa: BLE001 - reported to the content author
        raise ContentError(
            ["trace %s failed: %s: %s" % (item.get("id"), type(exc).__name__, exc)]
        )
    item = dict(item)
    item["answers"] = [repr(value)]
    return item


def validate_drills(items, concepts):
    problems = []
    seen_ids = set()
    seen_text = {}

    for item in items:
        cid = item.get("id", "")
        itype = item.get("type")
        concept = item.get("concept")

        if not cid:
            label = item.get("front") or item.get("question") or item.get("prompt") or "?"
            problems.append("item without id: %r" % (label,))
            continue
        if cid in seen_ids:
            problems.append("duplicate id: %s" % cid)
        seen_ids.add(cid)

        if itype not in ("recall", "choice", "code", "trace"):
            problems.append("%s: unknown type %r" % (cid, itype))
        if concept not in concepts:
            problems.append("%s: concept %r is not in CONCEPTS" % (cid, concept))
        if not item.get("explain") and itype != "recall":
            problems.append("%s: missing explain" % cid)

        if itype == "recall":
            for field in ("front", "back"):
                if not item.get(field):
                    problems.append("%s: missing %s" % (cid, field))
            text = item.get("front", "")
        elif itype == "choice":
            options = item.get("options") or []
            if len(options) < 3:
                problems.append("%s: needs at least 3 options" % cid)
            if len(set(options)) != len(options):
                problems.append("%s: duplicate options" % cid)
            answer = item.get("answer")
            if not isinstance(answer, int) or not 0 <= answer < len(options):
                problems.append("%s: answer index out of range" % cid)
            text = item.get("question", "")
        elif itype == "code":
            code = item.get("code", "")
            if code.count("___") != 1:
                problems.append("%s: code must contain exactly one ___" % cid)
            answers = item.get("answers") or []
            if not answers or not all(str(a).strip() for a in answers):
                problems.append("%s: missing answers" % cid)
            text = item.get("prompt", "")
        else:  # trace
            text = item.get("prompt", "")

        key = normalize(text)
        if key:
            if key in seen_text:
                problems.append("%s: same prompt as %s" % (cid, seen_text[key]))
            seen_text[key] = cid

    for concept in concepts:
        if not any(item.get("concept") == concept for item in items):
            problems.append("no items for concept: %s" % concept)

    return problems


def validate_problems(problems, concepts):
    issues = []
    seen_ids = set()
    for item in problems:
        pid = item.get("id", "")
        if not pid:
            issues.append("problem without id: %r" % item.get("title"))
            continue
        if pid in seen_ids:
            issues.append("duplicate problem id: %s" % pid)
        seen_ids.add(pid)
        for field in ("title", "statement"):
            if not item.get(field):
                issues.append("%s: missing %s" % (pid, field))
        if item.get("concept") not in concepts:
            issues.append("%s: unknown concept %r" % (pid, item.get("concept")))
        if item.get("difficulty") not in ("Easy", "Medium", "Hard"):
            issues.append("%s: bad difficulty %r" % (pid, item.get("difficulty")))
        if not item.get("examples"):
            issues.append("%s: no examples" % pid)
        for index, example in enumerate(item.get("examples") or []):
            if not example.get("input") or not example.get("output"):
                issues.append("%s: example %d missing input/output" % (pid, index + 1))
        if not item.get("constraints"):
            issues.append("%s: no constraints" % pid)

        variants = item.get("variants") or []
        if not variants:
            issues.append("%s: no solution variants" % pid)
        names = set()
        for variant in variants:
            for field in ("name", "complexity", "note", "code"):
                if not variant.get(field):
                    issues.append("%s: variant %r missing %s" % (pid, variant.get("name"), field))
            if variant.get("name") in names:
                issues.append("%s: duplicate variant name %r" % (pid, variant.get("name")))
            names.add(variant.get("name"))
            try:
                ast.parse(variant.get("code", ""))
            except SyntaxError as exc:
                issues.append("%s / %s: code does not parse: %s (line %s)"
                              % (pid, variant.get("name"), exc.msg, exc.lineno))
    return issues


def load_graph():
    try:
        with open(GRAPH_PATH, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        raise ContentError(["missing %s" % GRAPH_PATH])
    except ValueError as exc:
        raise ContentError(["graph.json is not valid JSON: %s" % exc])


def validate_graph(graph, concepts):
    issues = []
    nodes = graph.get("nodes") or []
    edges = graph.get("edges") or []
    if not nodes:
        issues.append("graph.json has no nodes")
    ids = {}
    for node in nodes:
        nid = node.get("id")
        if not nid:
            issues.append("graph node without id: %r" % node.get("label"))
            continue
        if nid in ids:
            issues.append("duplicate graph node id: %s" % nid)
        ids[nid] = node
        if node.get("concept") not in concepts:
            issues.append("graph node %s: unknown concept %r" % (nid, node.get("concept")))
        if not node.get("label"):
            issues.append("graph node %s: missing label" % nid)
        if not isinstance(node.get("layer"), int) or node.get("layer") < 0:
            issues.append("graph node %s: layer must be a non-negative integer" % nid)
    for edge in edges:
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            issues.append("graph edge must be a pair: %r" % (edge,))
            continue
        if edge[0] not in ids or edge[1] not in ids:
            issues.append("graph edge references an unknown node: %r" % (edge,))
        if edge[0] == edge[1]:
            issues.append("graph self-loop: %r" % (edge,))
    covered = {node.get("concept") for node in nodes}
    missing = [concept for concept in concepts if concept not in covered]
    if missing:
        issues.append("graph is missing concepts: %s" % ", ".join(missing))
    return issues


def validate_practice(problems, concepts):
    issues = []
    seen_ids = set()
    for item in problems:
        pid = item.get("id", "")
        if not pid:
            issues.append("practice problem without id: %r" % item.get("title"))
            continue
        if pid in seen_ids:
            issues.append("duplicate practice id: %s" % pid)
        seen_ids.add(pid)
        if item.get("concept") not in concepts:
            issues.append("%s: unknown concept %r" % (pid, item.get("concept")))
        for field in ("title", "statement", "source"):
            if not item.get(field):
                issues.append("%s: missing %s" % (pid, field))
        if not item.get("variants"):
            issues.append("%s: no variants" % pid)
        for variant in item.get("variants") or []:
            if not variant.get("code"):
                issues.append("%s: empty solution code" % pid)
    return issues


def build_content():
    """Read every source file and return the JSON payload for the app."""
    bugs = []

    bank = load_module(os.path.join(HERE, "study_bank.py"), "study_bank")
    extras_path = os.path.join(HERE, "study_extras.py")
    if not os.path.exists(extras_path):
        raise ContentError(["missing %s" % extras_path])
    extras = load_module(extras_path, "study_extras")
    solve = load_module(os.path.join(HERE, "solve_bank.py"), "solve_bank")

    concepts = list(bank.CONCEPTS)
    raw_extras = [dict(item) for item in extras.EXTRA_ITEMS]
    for item in raw_extras:
        if item.get("type") == "trace" and "answers" in item:
            bugs.append("%s: trace answers are computed, do not set them" % item.get("id"))

    items = [dict(item) for item in bank.RECALL_ITEMS]
    for item in raw_extras:
        if item.get("type") != "trace":
            items.append(item)
            continue
        try:
            items.append(build_trace(item))
        except ContentError as exc:
            bugs.extend(exc.issues)

    problems = [dict(item) for item in solve.PROBLEMS]
    graph = load_graph()
    practice_dir = os.path.join(os.path.dirname(HERE), "practice")
    practice, practice_warnings = parse_practice_dir(practice_dir, concepts)

    issues = bugs
    issues += validate_drills(items, concepts)
    issues += validate_problems(problems, concepts)
    issues += validate_practice(practice, concepts)
    issues += validate_graph(graph, concepts)
    if issues:
        raise ContentError(issues)

    counts = {}
    for item in items:
        counts[item.get("type")] = counts.get(item.get("type"), 0) + 1

    return {
        "concepts": concepts,
        "items": items,
        "problems": problems,
        "practice": practice,
        "graph": graph,
        "meta": {
            "items": len(items),
            "counts": counts,
            "problems": len(problems),
            "variants": sum(len(problem["variants"]) for problem in problems),
            "practice": len(practice),
            "practice_stubs": sum(1 for problem in practice if not problem["implemented"]),
            "nodes": len(graph["nodes"]),
            "edges": len(graph["edges"]),
            "warnings": practice_warnings,
        },
    }
