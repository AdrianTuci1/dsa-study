"""
CONCEPT: Tree DFS (paths, depth, validation)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/11_tree_dfs.py

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
# Problem 1 - Maximum Depth of Binary Tree  (LeetCode 104)
#
# Given the root of a binary tree, return its maximum depth: the number of nodes
# on the longest path from the root down to a leaf. The depth of an empty (None)
# tree is 0. Recurse on the two children and keep 1 + the larger result.
#
# Example 1:
#   Input: root = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
#   Output: 3
# Example 2:
#   Input: root = None
#   Output: 0
#
# Constraints:
#   - 0 <= number of nodes <= 10^4
#   - -100 <= node value <= 100
# ---------------------------------------------------------------------------
def p1_max_depth(root):
    if root is None:
        return 0
    _, left, right = root
    return 1 + max(p1_max_depth(left), p1_max_depth(right))


# ---------------------------------------------------------------------------
# Problem 2 - Path Sum  (LeetCode 112)
#
# Given the root of a binary tree and an integer `target_sum`, return True if
# there is a root-to-leaf path whose node values add up to `target_sum`.
# A leaf is a node with no children, so a None tree has no path and returns
# False. Recurse with target_sum minus the current value and stop at the leaves.
#
# Example 1:
#   Input: root = (5, (4, (11, (7, None, None), (2, None, None)), None),
#                 (8, (13, None, None), (4, None, (1, None, None)))), target_sum = 22
#   Output: True        (the path 5 -> 4 -> 11 -> 2 sums to 22)
# Example 2:
#   Input: root = (1, (2, None, None), (3, None, None)), target_sum = 5
#   Output: False
#
# Constraints:
#   - 0 <= number of nodes <= 5000
#   - -1000 <= node value <= 1000
#   - -1000 <= target_sum <= 1000
# ---------------------------------------------------------------------------
def p2_has_path_sum(root, target_sum):
    if root is None:
        return False
    val, left, right = root
    if left is None and right is None:
        return val == target_sum
    rest = target_sum - val
    return p2_has_path_sum(left, rest) or p2_has_path_sum(right, rest)



# ---------------------------------------------------------------------------
# Problem 3 - Validate Binary Search Tree  (LeetCode 98)
#
# Given the root of a binary tree, return True if it is a valid binary search
# tree: every node in the left subtree is strictly smaller than the node, and
# every node in the right subtree is strictly greater. Checking only the direct
# children is not enough - carry an allowed (low, high) interval down the
# recursion. An empty (None) tree is a valid BST.
#
# Example 1:
#   Input: root = (2, (1, None, None), (3, None, None))
#   Output: True
# Example 2:
#   Input: root = (5, (1, None, None), (4, (3, None, None), (6, None, None)))
#   Output: False
#
# Constraints:
#   - 0 <= number of nodes <= 10^4
#   - -2^31 <= node value <= 2^31 - 1
# ---------------------------------------------------------------------------
def p3_is_valid_bst(root):
    def valid(node, low, high):
        if node is None:
            return True
        val, left, right = node
        if not (low < val < high):
            return False
        return valid(left, low, val) and valid(right, val, high)

    return vaild(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    path_sum_tree = (5, (4, (11, (7, None, None), (2, None, None)), None), (8, (13, None, None), (4, None, (1, None, None))))
    tests = [
        ("P1 max_depth", p1_max_depth, ((3, (9, None, None), (20, (15, None, None), (7, None, None))),), 3),
        ("P1 max_depth empty tree", p1_max_depth, (None,), 0),
        ("P1 max_depth single node", p1_max_depth, ((1, None, None),), 1),
        ("P1 max_depth chain", p1_max_depth, ((1, (2, (3, None, None), None), None),), 3),
        ("P2 has_path_sum", p2_has_path_sum, (path_sum_tree, 22), True),
        ("P2 has_path_sum no path", p2_has_path_sum, ((1, (2, None, None), (3, None, None)), 5), False),
        ("P2 has_path_sum empty tree", p2_has_path_sum, (None, 0), False),
        ("P2 has_path_sum single node hit", p2_has_path_sum, ((1, None, None), 1), True),
        ("P2 has_path_sum must end at leaf", p2_has_path_sum, ((1, (2, None, None), None), 1), False),
        ("P3 is_valid_bst", p3_is_valid_bst, ((2, (1, None, None), (3, None, None)),), True),
        ("P3 is_valid_bst bad right subtree", p3_is_valid_bst, ((5, (1, None, None), (4, (3, None, None), (6, None, None))),), False),
        ("P3 is_valid_bst empty tree", p3_is_valid_bst, (None,), True),
        ("P3 is_valid_bst duplicate value", p3_is_valid_bst, ((2, (2, None, None), None),), False),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
