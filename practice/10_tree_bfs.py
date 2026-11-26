"""
CONCEPT: Tree BFS (level order)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/10_tree_bfs.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.

Trees are given as nested tuples: (value, left, right), where left and right
are either None or another (value, left, right) tuple. For example the tree
      1
     / \
    2   3
is (1, (2, None, None), (3, None, None)).
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Binary Tree Level Order Traversal  (LeetCode 102)
#
# Given the root of a binary tree, return its level order traversal: a list of
# lists, where the i-th inner list holds the values of the nodes on level i,
# read from left to right. Use a BFS queue that processes one whole level at a
# time. Return an empty list for an empty (None) tree.
#
# Example 1:
#   Input: root = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
#   Output: [[3], [9, 20], [15, 7]]
# Example 2:
#   Input: root = None
#   Output: []
#
# Constraints:
#   - 0 <= number of nodes <= 2000
#   - -1000 <= node value <= 1000
# ---------------------------------------------------------------------------
def p1_level_order(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node[0])
            if node[1] is not None:
                q.append(node[1])
            if node[2] is not None:
                q.append(node[2])
        out.append(level)
    return out



# ---------------------------------------------------------------------------
# Problem 2 - Binary Tree Right Side View  (LeetCode 199)
#
# Given the root of a binary tree, imagine you are standing on the right side of
# it and return the values you can see, ordered from top to bottom: that is, for
# every level return the value of the rightmost node on that level. A BFS that
# keeps each level as a list gives this directly. Return an empty list for an
# empty (None) tree.
#
# Example 1:
#   Input: root = (1, (2, None, (5, None, None)), (3, None, (4, None, None)))
#   Output: [1, 3, 4]
# Example 2:
#   Input: root = None
#   Output: []
#
# Constraints:
#   - 0 <= number of nodes <= 100
#   - -100 <= node value <= 100
# ---------------------------------------------------------------------------
def p2_right_side_view(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        last = None
        for _ in range(len(q)):
            node = q.popleft()
            last = node[0]

            if node[1] is not None: q.append(node[1])
            if node[2] is not None: q.append(node[2])
        out.append(last)
    return out


# ---------------------------------------------------------------------------
# Problem 3 - Binary Tree Zigzag Level Order Traversal  (LeetCode 103)
#
# Given the root of a binary tree, return its zigzag level order traversal: the
# values level by level, but the direction alternates, so level 0 is read left
# to right, level 1 right to left, level 2 left to right, and so on. Keep the
# normal BFS and reverse the values of every odd level. Return an empty list
# for an empty (None) tree.
#
# Example 1:
#   Input: root = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
#   Output: [[3], [20, 9], [15, 7]]
# Example 2:
#   Input: root = None
#   Output: []
#
# Constraints:
#   - 0 <= number of nodes <= 2000
#   - -100 <= node value <= 100
# ---------------------------------------------------------------------------
def p3_zigzag_level_order(root):
    if root is None:
        return []

    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node[0])
            if node[1] is not None: q.append(node[1])
            if node[1] is not None: q.append(node[2])
        if len(out) % 2 == 1:
            level.reverse()
        out.append(leve)
    return out
    


if __name__ == "__main__":
    full = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
    tests = [
        ("P1 level_order", p1_level_order, (full,), [[3], [9, 20], [15, 7]]),
        ("P1 level_order empty tree", p1_level_order, (None,), []),
        ("P1 level_order single node", p1_level_order, ((1, None, None),), [[1]]),
        ("P1 level_order skewed tree", p1_level_order, ((1, (2, (4, None, None), None), (3, None, None)),), [[1], [2, 3], [4]]),
        ("P2 right_side_view", p2_right_side_view, ((1, (2, None, (5, None, None)), (3, None, (4, None, None))),), [1, 3, 4]),
        ("P2 right_side_view empty tree", p2_right_side_view, (None,), []),
        ("P2 right_side_view single node", p2_right_side_view, ((1, None, None),), [1]),
        ("P2 right_side_view left only", p2_right_side_view, ((1, (2, None, None), None),), [1, 2]),
        ("P3 zigzag_level_order", p3_zigzag_level_order, (full,), [[3], [20, 9], [15, 7]]),
        ("P3 zigzag_level_order empty tree", p3_zigzag_level_order, (None,), []),
        ("P3 zigzag_level_order single node", p3_zigzag_level_order, ((1, None, None),), [[1]]),
        ("P3 zigzag_level_order two levels", p3_zigzag_level_order, ((1, (2, None, None), (3, None, None)),), [[1], [3, 2]]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
