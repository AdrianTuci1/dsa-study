"""
CONCEPT: Union Find / DSU (components, cycle detection)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/16_union_find.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Number of Connected Components
#
# Nodes are numbered 0 .. n-1. `edges` is a list of undirected pairs [u, v].
# Return the number of connected components in the graph. A graph with no
# nodes has 0 components; a graph with nodes and no edges has n components.
#
# Example 1:
#   Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
#   Output: 2
# Example 2:
#   Input: n = 4, edges = []
#   Output: 4
#
# Constraints:
#   - 0 <= n <= 2000
#   - 0 <= len(edges) <= 5000
#   - Every pair is [u, v] with 0 <= u, v < n
# ---------------------------------------------------------------------------
def p1_count_components(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    count = n
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        if rank[ru] < rank[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
        count -= 1

    return count


# ---------------------------------------------------------------------------
# Problem 2 - Undirected Cycle Detection
#
# Nodes are numbered 0 .. n-1 and `edges` is a list of distinct undirected
# pairs [u, v] (no self-loops, no repeated pairs). Return True if the graph
# contains a cycle, i.e. a path of length >= 3 that returns to its start.
# A graph with no edges can never contain a cycle.
#
# Example 1:
#   Input: n = 3, edges = [[0, 1], [1, 2], [2, 0]]
#   Output: True
# Example 2:
#   Input: n = 3, edges = [[0, 1], [1, 2]]
#   Output: False
#
# Constraints:
#   - 0 <= n <= 2000
#   - 0 <= len(edges) <= 5000
#   - Edges are distinct pairs [u, v] with 0 <= u, v < n and u != v
# ---------------------------------------------------------------------------
def p2_has_cycle(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return True
        if rank[ru] < rank[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
    
    return False



# ---------------------------------------------------------------------------
# Problem 3 - Redundant Edge  (LeetCode 684, 0-indexed variant)
#
# Nodes are numbered 0 .. n-1 and the edges in `edges` are added one at a
# time, in the given order, as undirected connections. Return the first edge
# [u, v] that connects two nodes already lying in the same component (so it
# creates a cycle), or [] if no edge does. Return the pair in the same order
# as it appears in the input.
#
# Example 1:
#   Input: n = 3, edges = [[0, 1], [1, 2], [2, 0]]
#   Output: [2, 0]
# Example 2:
#   Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
#   Output: [1, 3]
#
# Constraints:
#   - 1 <= n <= 2000
#   - 0 <= len(edges) <= 5000
#   - Every pair is [u, v] with 0 <= u, v < n
# ---------------------------------------------------------------------------
def p3_redundant_edge(n, edges):
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ("P1 count_components", p1_count_components, (5, [[0, 1], [1, 2], [3, 4]]), 2),
        ("P1 count_components", p1_count_components, (4, []), 4),
        ("P1 count_components", p1_count_components, (1, []), 1),
        ("P1 count_components", p1_count_components, (3, [[0, 1], [1, 2], [2, 0]]), 1),
        ("P2 has_cycle", p2_has_cycle, (3, [[0, 1], [1, 2], [2, 0]]), True),
        ("P2 has_cycle", p2_has_cycle, (3, [[0, 1], [1, 2]]), False),
        ("P2 has_cycle", p2_has_cycle, (0, []), False),
        ("P2 has_cycle", p2_has_cycle, (4, [[0, 1], [2, 3]]), False),
        ("P2 has_cycle", p2_has_cycle, (5, [[0, 1], [1, 2], [3, 4], [2, 3]]), False),
        ("P3 redundant_edge", p3_redundant_edge, (3, [[0, 1], [1, 2], [2, 0]]), [2, 0]),
        ("P3 redundant_edge", p3_redundant_edge,
         (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), [1, 3]),
        ("P3 redundant_edge", p3_redundant_edge, (3, [[0, 1], [1, 2]]), []),
        ("P3 redundant_edge", p3_redundant_edge, (1, []), []),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
