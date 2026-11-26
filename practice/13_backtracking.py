"""
CONCEPT: Backtracking (subsets, permutations, combinations)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/13_backtracking.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Subsets  (LeetCode 78)
#
# Given a list of distinct integers `nums`, return every possible subset of
# `nums` (the power set), including the empty subset and `nums` itself.
# To keep the result deterministic, each subset must be sorted in ascending
# order and the list of subsets must be sorted lexicographically.
#
# Example 1:
#   Input: nums = [1, 2, 3]
#   Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# Example 2:
#   Input: nums = []
#   Output: [[]]
#
# Constraints:
#   - 0 <= len(nums) <= 10
#   - All elements of nums are distinct
# ---------------------------------------------------------------------------
def p1_subsets(nums):
    nums = sorted(nums)
    res, path = [], []

    def dfs(start):
        res.append(path[:])
        for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
    dfs(0)
    return res


# ---------------------------------------------------------------------------
# Problem 2 - Permutations  (LeetCode 46)
#
# Given a list of distinct integers `nums`, return all possible permutations
# of `nums`. The list of permutations must be sorted lexicographically so the
# result is deterministic.
#
# Example 1:
#   Input: nums = [1, 2, 3]
#   Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Example 2:
#   Input: nums = [0, 1]
#   Output: [[0, 1], [1, 0]]
#
# Constraints:
#   - 0 <= len(nums) <= 6
#   - All elements of nums are distinct
# ---------------------------------------------------------------------------
def p2_permutations(nums):
    nums = sorted(nums)
    res, path = [], []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return res

# ---------------------------------------------------------------------------
# Problem 3 - Combination Sum  (LeetCode 39)
#
# Given a list of distinct positive integers `candidates` and a positive
# integer `target`, return every unique combination of candidates whose values
# sum to `target`. The same candidate may be chosen an unlimited number of
# times. Each combination must be sorted in ascending order and the list of
# combinations must be sorted lexicographically. Return [] if no combination
# reaches the target.
#
# Example 1:
#   Input: candidates = [2, 3, 6, 7], target = 7
#   Output: [[2, 2, 3], [7]]
# Example 2:
#   Input: candidates = [2, 3, 5], target = 8
#   Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
#
# Constraints:
#   - 1 <= len(candidates) <= 20
#   - 1 <= candidates[i] <= 30, all distinct
#   - 1 <= target <= 30
# ---------------------------------------------------------------------------
def p3_combination_sum(candidates, target):
    candidates = sorted(candidates)
    res, path = [], []

    def dfs(start, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            path.append(c)
            dfs(i, remaining - c)
            path.pop()
    dfs(0, target)
    return res




if __name__ == "__main__":
    tests = [
        ("P1 subsets", p1_subsets, ([1, 2, 3],),
         [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ("P1 subsets", p1_subsets, ([],), [[]]),
        ("P1 subsets", p1_subsets, ([0],), [[], [0]]),
        ("P1 subsets", p1_subsets, ([1, 2],), [[], [1], [1, 2], [2]]),
        ("P2 permutations", p2_permutations, ([1, 2, 3],),
         [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ("P2 permutations", p2_permutations, ([0, 1],), [[0, 1], [1, 0]]),
        ("P2 permutations", p2_permutations, ([7],), [[7]]),
        ("P2 permutations", p2_permutations, ([],), [[]]),
        ("P3 combination_sum", p3_combination_sum, ([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
        ("P3 combination_sum", p3_combination_sum, ([2, 3, 5], 8),
         [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ("P3 combination_sum", p3_combination_sum, ([2], 1), []),
        ("P3 combination_sum", p3_combination_sum, ([7], 7), [[7]]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
