"""Tiny test harness for the practice problems (no dependencies).

Usage inside a practice file:

    from _harness import run, summary

    if __name__ == "__main__":
        tests = [
            ("P1 two_sum", two_sum, ([2, 7, 11, 15], 9), [0, 1]),
        ]
        summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
"""


def run(name, fn, args, expected):
    """Call fn(*args) and compare with expected. Returns True on pass."""
    try:
        got = fn(*args)
    except NotImplementedError:
        print(f"[ ] {name} - not solved yet")
        return False
    except Exception as exc:
        print(f"[x] {name} - raised {type(exc).__name__}: {exc}")
        return False
    if got == expected:
        print(f"[v] {name}")
        return True
    print(f"[x] {name} - got {got!r}, expected {expected!r}")
    return False


def summary(results):
    total = len(results)
    passed = sum(1 for r in results if r)
    print(f"\n{passed}/{total} passed")
