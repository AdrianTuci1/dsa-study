"""
CONCEPT: Advanced Graphs II (SCC, bridges, bipartite matching)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/29_advanced_graphs_2.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Number of Strongly Connected Components
#
# `adj` is the adjacency list of a directed graph: `adj[u]` holds the nodes v
# for which the edge u -> v exists. Node numbers are 0-indexed and the graph
# has n = len(adj) nodes, so an empty list describes a graph with 0 nodes.
# A strongly connected component is a maximal group of nodes such that every
# node of the group can reach every other node of the group. A node always
# reaches itself, so every node belongs to exactly one component. Return the
# number of components.
#
# Example 1:
#   Input: adj = [[1], [2], [0, 3], [4], [3]]
#   Output: 2
#   Explanation: {0, 1, 2} form a cycle and {3, 4} form a cycle, but from node
#   3 there is no way back to 0, 1 or 2.
# Example 2:
#   Input: adj = [[1, 2], [3], [3], []]
#   Output: 4
#   Explanation: no node can return to a node that reaches it, so each node is
#   a component of its own.
#
# Constraints:
#   - 0 <= len(adj) <= 2000
#   - Every entry in adj[u] is a node index with 0 <= v < len(adj)
#   - Self-loops and repeated edges are allowed
# ---------------------------------------------------------------------------
def p1_count_scc(adj):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 2 - Critical Connections in a Network  (LeetCode 1192)
#
# Nodes are numbered 0 .. n-1 and `connections` is a list of undirected pairs
# [u, v]. A connection is critical (a bridge) when removing it disconnects
# part of the graph, i.e. when it does not belong to any cycle. Return all
# critical connections as a list of pairs.
#
# The order of the output is fixed so that the answer is unique: within every
# pair write the smaller node first, then sort the pairs ascending (first by
# the first element, then by the second). Return [] when there are none.
#
# Example 1:
#   Input: n = 4, connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
#   Output: [[1, 3]]
#   Explanation: 0-1-2 is a cycle, so those three connections are not
#   critical; 1-3 is the only way to reach node 3.
# Example 2:
#   Input: n = 2, connections = [[0, 1]]
#   Output: [[0, 1]]
# Example 3:
#   Input: n = 3, connections = [[0, 1], [1, 2], [2, 0]]
#   Output: []
#
# Constraints:
#   - 1 <= n <= 2000
#   - 0 <= len(connections) <= 5000
#   - Every pair is [u, v] with 0 <= u, v < n; repeated pairs (in any order)
#     and self-loops are allowed and are never critical
# ---------------------------------------------------------------------------
def p2_critical_connections(n, connections):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 3 - Maximum Bipartite Matching
#
# The bipartite graph has `n_left` left nodes (numbered 0 .. n_left-1) and
# `n_right` right nodes (numbered 0 .. n_right-1). `adj[u]` lists the right
# nodes connected to left node u, so len(adj) == n_left. A matching is a set
# of pairs (left, right) in which every left node and every right node appears
# at most once, and each pair must be an existing edge. Return the size of the
# largest possible matching.
#
# Example 1:
#   Input: n_left = 3, n_right = 3, adj = [[0, 1], [0], [1]]
#   Output: 2
#   Explanation: match left 1 with right 0 and left 2 with right 1; left 0 then
#   has no free neighbour, so 3 pairs are impossible.
# Example 2:
#   Input: n_left = 2, n_right = 2, adj = [[0], [0]]
#   Output: 1
#   Explanation: both left nodes only connect to right 0, so at most one of
#   them can be matched.
#
# Constraints:
#   - 0 <= n_left <= 500
#   - 0 <= n_right <= 500
#   - len(adj) == n_left and every adj[u] holds right nodes 0 <= v < n_right
# ---------------------------------------------------------------------------
def p3_max_bipartite_matching(n_left, n_right, adj):
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ("P1 count_scc", p1_count_scc, ([[1], [2], [0, 3], [4], [3]],), 2),
        ("P1 count_scc", p1_count_scc, ([[1, 2], [3], [3], []],), 4),
        ("P1 count_scc", p1_count_scc, ([],), 0),
        ("P1 count_scc", p1_count_scc, ([[0]],), 1),
        ("P1 count_scc", p1_count_scc, ([[], [0]],), 2),
        ("P1 count_scc", p1_count_scc, ([[1], [0]],), 1),
        ("P1 count_scc", p1_count_scc, ([[1], [2], [0], [4], [3, 5], [4]],), 2),
        ("P1 count_scc", p1_count_scc,
         ([[1, 2], [3, 4], [4, 5], [0], [5], []],), 4),
        ("P2 critical_connections", p2_critical_connections,
         (4, [[0, 1], [1, 2], [2, 0], [1, 3]]), [[1, 3]]),
        ("P2 critical_connections", p2_critical_connections, (2, [[0, 1]]), [[0, 1]]),
        ("P2 critical_connections", p2_critical_connections,
         (3, [[0, 1], [1, 2], [2, 0]]), []),
        ("P2 critical_connections", p2_critical_connections, (1, []), []),
        ("P2 critical_connections", p2_critical_connections,
         (3, [[0, 1], [1, 2]]), [[0, 1], [1, 2]]),
        ("P2 critical_connections", p2_critical_connections,
         (5, [[0, 1], [1, 2], [2, 0], [3, 4]]), [[3, 4]]),
        ("P2 critical_connections", p2_critical_connections,
         (2, [[0, 1], [0, 1]]), []),
        ("P2 critical_connections", p2_critical_connections,
         (2, [[1, 0], [0, 1]]), []),
        ("P2 critical_connections", p2_critical_connections,
         (2, [[0, 0], [0, 1]]), [[0, 1]]),
        ("P2 critical_connections", p2_critical_connections,
         (6, [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [5, 3]]), [[2, 3]]),
        ("P2 critical_connections", p2_critical_connections,
         (4, [[0, 1], [1, 2], [2, 3]]), [[0, 1], [1, 2], [2, 3]]),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (3, 3, [[0, 1], [0], [1]]), 2),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (2, 2, [[0], [0]]), 1),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching, (0, 3, []), 0),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching, (2, 0, [[], []]), 0),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (2, 2, [[0, 1], [0, 1]]), 2),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (3, 3, [[0, 1], [0, 2], [1]]), 3),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (3, 3, [[], [0], []]), 1),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (4, 4, [[0], [0, 1], [1, 2], [2, 3]]), 4),
        ("P3 max_bipartite_matching", p3_max_bipartite_matching,
         (2, 1, [[0], [0]]), 1),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
