"""
CONCEPT: Advanced Structures (Segment Tree, Fenwick, Sparse Table)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/27_advanced_structures.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Segment Tree: range sum query with point updates
#   Structure: Segment Tree
#   Required complexity: build O(n), update O(log n), query O(log n)
#   (no brute-force recomputation of the whole range per query)
#
# Build a segment tree over an integer array `nums` that supports
#   * point update: set nums[index] = value
#   * range query: sum of nums[left..right], both ends inclusive
#
# Both functions take a list of operations, in the design-problem style:
#   ops  - list of operation names
#   args - list of argument lists, one per operation
# Return a list with one return value per operation:
#   "SegmentTree" -> None                     (args[0] is [nums])
#   "update"      -> None                     (args = [index, value])
#   "query"       -> the sum over [left, right] (args = [left, right])
#
# Example 1:
#   Input: ops = ["SegmentTree", "query", "update", "query"]
#          args = [[[1, 3, 5, 7, 9, 11]], [1, 3], [1, 10], [1, 3]]
#   Output: [None, 15, None, 22]
#   Explanation: sum(3 + 5 + 7) = 15. update(1, 10) turns the array into
#                [1, 10, 5, 7, 9, 11], so sum(10 + 5 + 7) = 22.
#
# Example 2:
#   Input: ops = ["SegmentTree", "query", "update", "query"]
#          args = [[[5]], [0, 0], [0, -3], [0, 0]]
#   Output: [None, 5, None, -3]
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - 0 <= number of operations <= 10^5
#   - 0 <= index < len(nums) and left <= right, with both in range
#   - -10^4 <= nums[i], value <= 10^4
# ---------------------------------------------------------------------------
def p1_segment_tree_ops(ops, args):
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 2 - Fenwick Tree (Binary Indexed Tree): prefix sums with point updates
#   Structure: Fenwick / BIT
#   Required complexity: build O(n), add O(log n), prefix_sum/range_sum O(log n)
#
# Build a Fenwick tree over an integer array `nums` with these operations:
#   "Fenwick"    -> None                       (args[0] is [nums])
#   "add"        -> None, nums[index] += delta (args = [index, delta])
#   "prefix_sum" -> sum of nums[0..index] inclusive (args = [index])
#   "range_sum"  -> sum of nums[left..right] inclusive (args = [left, right])
#
# Indexing: the internal BIT array is 1-based (it needs the extra slot 0 in
# front), but this API is 0-based - every index you pass or get back counts
# from 0, exactly like indexing into `nums`. Only the bit trick `i & (-i)`
# sees 1-based positions.
#
# Example 1:
#   Input: ops = ["Fenwick", "add", "prefix_sum", "range_sum"]
#          args = [[[1, 2, 3, 4, 5]], [1, 10], [4], [1, 3]]
#   Output: [None, None, 25, 19]
#   Explanation: after add(1, 10) the array is [1, 12, 3, 4, 5];
#                prefix_sum(4) = 1 + 12 + 3 + 4 + 5 = 25 and
#                range_sum(1, 3) = 12 + 3 + 4 = 19.
#
# Example 2:
#   Input: ops = ["Fenwick", "prefix_sum", "range_sum"]
#          args = [[[2, 4, 6, 8]], [0], [0, 3]]
#   Output: [None, 2, 20]
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - 0 <= number of operations <= 10^5
#   - 0 <= index < len(nums) and left <= right, with both in range
#   - -10^4 <= nums[i], delta <= 10^4 (prefix sums fit in a Python int)
# ---------------------------------------------------------------------------
def p2_fenwick_ops(ops, args):
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 3 - Sparse Table: static range minimum query
#   Structure: Sparse Table
#   Required complexity: build O(n log n), query O(1)
#   There are NO updates: `nums` is fixed once the structure is built, so the
#   precomputed table never has to be repaired. That is exactly the trade-off
#   that makes O(1) queries possible.
#
# Operations:
#   "SparseTable" -> None                          (args[0] is [nums])
#   "query"       -> min of nums[left..right], both ends inclusive
#                    (args = [left, right])
#
# Ranges are never empty, so every query has a well-defined minimum.
#
# Example 1:
#   Input: ops = ["SparseTable", "query", "query"]
#          args = [[[4, 2, 7, 1, 9]], [1, 3], [0, 4]]
#   Output: [None, 1, 1]
#   Explanation: min(2, 7, 1) = 1 and min over the whole array is 1.
#
# Example 2:
#   Input: ops = ["SparseTable", "query", "query"]
#          args = [[[3, -1, 5, 2]], [0, 3], [2, 2]]
#   Output: [None, -1, 5]
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - 0 <= number of operations <= 10^5
#   - 0 <= left <= right < len(nums)
#   - -10^9 <= nums[i] <= 10^9
# ---------------------------------------------------------------------------
def p3_sparse_table_ops(ops, args):
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ("P1 segment_tree example", p1_segment_tree_ops,
         (["SegmentTree", "query", "update", "query"],
          [[[1, 3, 5, 7, 9, 11]], [1, 3], [1, 10], [1, 3]]),
         [None, 15, None, 22]),
        ("P1 segment_tree single element", p1_segment_tree_ops,
         (["SegmentTree", "query", "update", "query"],
          [[[5]], [0, 0], [0, -3], [0, 0]]),
         [None, 5, None, -3]),
        ("P1 segment_tree query of the whole range", p1_segment_tree_ops,
         (["SegmentTree", "query"], [[[2, 4, 6, 8]], [0, 3]]),
         [None, 20]),
        ("P1 segment_tree no operations after build", p1_segment_tree_ops,
         (["SegmentTree"], [[[1, 2, 3]]]),
         [None]),
        ("P1 segment_tree several updates", p1_segment_tree_ops,
         (["SegmentTree", "update", "update", "query", "query"],
          [[[0, 0, 0]], [0, 5], [2, 3], [0, 2], [2, 2]]),
         [None, None, None, 8, 3]),
        ("P1 segment_tree negative update", p1_segment_tree_ops,
         (["SegmentTree", "update", "query"], [[[1, 2, 3, 4, 5]], [2, -10], [0, 4]]),
         [None, None, 2]),

        ("P2 fenwick example", p2_fenwick_ops,
         (["Fenwick", "add", "prefix_sum", "range_sum"],
          [[[1, 2, 3, 4, 5]], [1, 10], [4], [1, 3]]),
         [None, None, 25, 19]),
        ("P2 fenwick empty update list", p2_fenwick_ops,
         (["Fenwick", "prefix_sum", "range_sum"],
          [[[2, 4, 6, 8]], [0], [0, 3]]),
         [None, 2, 20]),
        ("P2 fenwick single element", p2_fenwick_ops,
         (["Fenwick", "add", "add", "prefix_sum", "range_sum"],
          [[[5]], [0, 5], [0, -2], [0], [0, 0]]),
         [None, None, None, 8, 8]),
        ("P2 fenwick range covering everything", p2_fenwick_ops,
         (["Fenwick", "range_sum"], [[[2, 4, 6, 8]], [0, 3]]),
         [None, 20]),
        ("P2 fenwick negatives and index 0", p2_fenwick_ops,
         (["Fenwick", "add", "prefix_sum", "range_sum"],
          [[[1, 2, 3]], [0, -1], [0], [0, 2]]),
         [None, None, 0, 5]),
        ("P2 fenwick mixed adds and queries", p2_fenwick_ops,
         (["Fenwick", "add", "add", "range_sum", "prefix_sum", "add", "range_sum"],
          [[[3, 1, 4, 1, 5]], [0, 10], [4, 10], [0, 4], [2], [3, -5], [0, 0]]),
         [None, None, None, 34, 18, None, 13]),

        ("P3 sparse_table example", p3_sparse_table_ops,
         (["SparseTable", "query", "query"], [[[4, 2, 7, 1, 9]], [1, 3], [0, 4]]),
         [None, 1, 1]),
        ("P3 sparse_table full range", p3_sparse_table_ops,
         (["SparseTable", "query", "query"], [[[3, -1, 5, 2]], [0, 3], [2, 2]]),
         [None, -1, 5]),
        ("P3 sparse_table single element", p3_sparse_table_ops,
         (["SparseTable", "query", "query"], [[[6]], [0, 0], [0, 0]]),
         [None, 6, 6]),
        ("P3 sparse_table query of length 1 in the middle", p3_sparse_table_ops,
         (["SparseTable", "query"], [[[5, 3, 8, 1]], [2, 2]]),
         [None, 8]),
        ("P3 sparse_table no queries at all", p3_sparse_table_ops,
         (["SparseTable"], [[[-4, 4]]]),
         [None]),
        ("P3 sparse_table duplicates", p3_sparse_table_ops,
         (["SparseTable", "query", "query"], [[[2, 2, 2, 2]], [1, 2], [0, 3]]),
         [None, 2, 2]),
        ("P3 sparse_table non power of two, unsorted", p3_sparse_table_ops,
         (["SparseTable", "query", "query", "query"],
          [[[9, 4, 7, 1, 8, 2]], [0, 5], [0, 2], [3, 4]]),
         [None, 1, 4, 1]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
