"""Parse `practice/*.py` into problems for the Solve workspace.

The practice files are written as:

    # ---------------------------------------------------------------------------
    # Problem 1 - Two Sum  (LeetCode 1)
    #
    # Given ...
    #
    # Example 1:
    #   Input: ...
    #   Output: ...
    #
    # Constraints:
    #   - ...
    # ---------------------------------------------------------------------------
    def p1_two_sum(nums, target):
        ...

This module extracts the statement, examples, constraints and the code block
for every problem. It is deliberately tolerant: a half-written solution is
still shown (marked as such) instead of breaking the app.

The server calls this on every /api/content request, so edits to practice/
show up on reload without a build step.
"""

import ast
import os
import re

SEPARATOR = re.compile(r"^#\s*-{10,}\s*$")
HEADER = re.compile(r"^Problem\s+(\d+)\s*-\s*(.+?)\s*$")
LEETCODE = re.compile(r"LeetCode\s+([0-9A-Za-z_-]+)")
EXAMPLE = re.compile(r"^Example\s+(\d+)\s*:")
CONSTRAINTS = re.compile(r"^Constraints\s*:")
KEY = re.compile(r"^(Input|Output|Explanation|Why)\s*:\s*(.*)$")
KEY_MAP = {"input": "input", "output": "output", "explanation": "why", "why": "why"}
FILE = re.compile(r"^(\d{2})_.*\.py$")


def clean_comment(line):
    if not line.startswith("#"):
        return line
    return line[1:].lstrip()


def split_blocks(lines):
    blocks = []
    current = []
    for line in lines:
        if SEPARATOR.match(line):
            blocks.append(current)
            current = []
        else:
            current.append(line)
    blocks.append(current)
    return blocks


def parse_header(header_lines):
    raw = [clean_comment(line) for line in header_lines if line.startswith("#")]
    title_line = next((line for line in raw if HEADER.match(line)), "")
    match = HEADER.match(title_line)
    if not match:
        return None

    number = int(match.group(1))
    rest = match.group(2).strip()
    leetcode_match = LEETCODE.search(rest)
    leetcode = leetcode_match.group(1) if leetcode_match else None
    title = re.sub(r"\s*\((?:LeetCode|Grokking)[^)]*\)\s*$", "", rest).strip()
    title = title.rstrip(" ,") or ("Problem %d" % number)

    statement_parts = []
    paragraph = []
    examples = []
    constraints = []
    section = "statement"
    current_example = None
    current_key = None

    def flush_paragraph():
        if paragraph:
            statement_parts.append(" ".join(paragraph))
            paragraph.clear()

    for line in raw:
        if line is title_line:
            continue
        if EXAMPLE.match(line):
            flush_paragraph()
            section = "example"
            current_example = {"input": "", "output": "", "why": ""}
            examples.append(current_example)
            current_key = None
            continue
        if CONSTRAINTS.match(line):
            flush_paragraph()
            section = "constraints"
            current_key = None
            continue

        if section == "statement":
            if not line.strip():
                flush_paragraph()
            else:
                paragraph.append(line.strip())
        elif section == "example":
            key_match = KEY.match(line)
            if key_match:
                current_key = KEY_MAP.get(key_match.group(1).lower())
                value = key_match.group(2).strip()
                if current_example is not None and current_key in current_example:
                    current_example[current_key] = value
            elif line.strip() and current_example is not None and current_key:
                current_example[current_key] = (
                    current_example[current_key] + " " + line.strip()
                ).strip()
        else:  # constraints
            text = line.strip()
            if not text:
                continue
            if text.startswith("- "):
                text = text[2:].strip()
            constraints.append(text)

    flush_paragraph()
    return {
        "number": number,
        "title": title,
        "leetcode": leetcode,
        "statement": "\n\n".join(part for part in statement_parts if part).strip(),
        "examples": [
            {
                "input": example["input"].strip(),
                "output": example["output"].strip(),
                "why": example["why"].strip(),
            }
            for example in examples
            if example["input"] or example["output"]
        ],
        "constraints": constraints,
    }


def parse_file(path, filename, prefix, concept):
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    blocks = split_blocks(lines)
    problems = []
    for index, block in enumerate(blocks):
        header_lines = [line for line in block if line.startswith("#")]
        meta = parse_header(header_lines)
        if not meta:
            continue

        following = blocks[index + 1] if index + 1 < len(blocks) else []
        code = "\n".join(following).strip("\n")
        if code and all(not line.strip() for line in following):
            code = ""
        # The next block is a header when it starts with "# Problem"; then the
        # current problem has no code.
        if following and following[0].strip().startswith("# Problem"):
            code = ""

        implemented = bool(code) and "raise NotImplementedError" not in code
        syntax_ok = True
        if code:
            try:
                ast.parse(code)
            except SyntaxError:
                syntax_ok = False

        source = "practice/" + filename
        note = "Read from %s on the content server." % source
        if not code:
            note += " This problem has no implementation yet."
        elif not implemented:
            note += " This practice file is still a stub."
        if not syntax_ok:
            note += " The snippet does not parse as Python."

        variant_name = "Your solution" if implemented else "Not implemented"
        problems.append({
            "id": "practice-%s-%d" % (prefix, meta["number"]),
            "title": meta["title"],
            "concept": concept,
            "difficulty": "Practice",
            "statement": meta["statement"] or meta["title"],
            "examples": meta["examples"],
            "constraints": meta["constraints"],
            "source": source,
            "leetcode": meta["leetcode"],
            "implemented": implemented,
            "syntax_ok": syntax_ok,
            "variants": [{
                "name": variant_name,
                "complexity": source,
                "note": note,
                "code": code or "# No implementation in %s yet." % source,
            }],
        })
    return problems


def parse_practice_dir(practice_dir, concepts):
    """Return (problems, warnings)."""
    concept_by_prefix = {}
    for concept in concepts:
        match = re.match(r"^(\d{2})\s", concept)
        if match:
            concept_by_prefix[match.group(1)] = concept

    problems = []
    warnings = []
    try:
        filenames = sorted(os.listdir(practice_dir))
    except OSError as exc:
        return [], ["cannot read %s: %s" % (practice_dir, exc)]

    for filename in filenames:
        match = FILE.match(filename)
        if not match:
            continue
        prefix = match.group(1)
        concept = concept_by_prefix.get(prefix)
        if not concept:
            warnings.append("%s: no concept for prefix %s" % (filename, prefix))
            continue
        path = os.path.join(practice_dir, filename)
        try:
            parsed = parse_file(path, filename, prefix, concept)
        except Exception as exc:  # noqa: BLE001 - one bad file must not break the app
            warnings.append("%s: %s: %s" % (filename, type(exc).__name__, exc))
            continue
        if not parsed:
            warnings.append("%s: no problems parsed" % filename)
        problems.extend(parsed)
    return problems, warnings
