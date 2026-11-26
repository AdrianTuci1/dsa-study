"""
CONCEPT: Dynamic Programming (1-D and 2-D)

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/17_dynamic_programming.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - House Robber  (LeetCode 198, 1-D DP)
#
# You are given a list of non-negative integers `nums` where nums[i] is the
# amount of money in the i-th house. A robber cannot rob two adjacent houses
# on the same night, because that would alert the police. Return the maximum
# amount of money the robber can steal without robbing two adjacent houses.
#
# Example 1:
#   Input: nums = [2, 7, 9, 3, 1]
#   Output: 12
# Example 2:
#   Input: nums = [2, 1, 1, 2]
#   Output: 4
#
# Constraints:
#   - 0 <= len(nums) <= 100
#   - 0 <= nums[i] <= 400
#   - An empty list yields 0.
# ---------------------------------------------------------------------------
def p1_rob(nums):
    # dp[i] = best loot using houses[0..i]:
    #   dp[i] = max(dp[i-1], dp[i-2] + nums[i])   (skip or rob house i)
    # Only the last two values are ever needed, so keep two variables.
    two_back, one_back = 0, 0
    for money in nums:
        two_back, one_back = one_back, max(one_back, two_back + money)
    return one_back


# ---------------------------------------------------------------------------
# Problem 2 - Unique Paths  (LeetCode 62, 2-D DP)
#
# A robot starts at the top-left corner of an m x n grid and wants to reach
# the bottom-right corner. It can only move either down or right at any point.
# Return the number of distinct paths the robot can take to reach the goal.
#
# Example 1:
#   Input: m = 3, n = 7
#   Output: 28
# Example 2:
#   Input: m = 2, n = 3
#   Output: 3
#
# Constraints:
#   - 1 <= m, n <= 20
# ---------------------------------------------------------------------------
def p2_unique_paths(m, n):
    # ways[r][c] = ways from above + ways from the left; the first row and
    # first column are 1. Keep only one row (rolling array), left to right.
    row = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]
    return row[-1]


# ---------------------------------------------------------------------------
# Problem 3 - Longest Common Subsequence  (LeetCode 1143, 2-D DP)
#
# Given two strings `text1` and `text2`, return the length of their longest
# common subsequence. A subsequence is a string formed from another string by
# deleting some (possibly zero) characters without changing the order of the
# remaining characters. If there is no common subsequence, return 0.
#
# Example 1:
#   Input: text1 = "abcde", text2 = "ace"
#   Output: 3
# Example 2:
#   Input: text1 = "abc", text2 = "abc"
#   Output: 3
#
# Constraints:
#   - 0 <= len(text1), len(text2) <= 100
#   - text1 and text2 consist of lowercase English letters.
# ---------------------------------------------------------------------------
def p3_lcs(text1, text2):
    # dp[i][j] = LCS of text1[:i] and text2[:j]
    #   same char   -> dp[i-1][j-1] + 1
    #   different   -> max(dp[i-1][j], dp[i][j-1])   (drop one character)
    prev = [0] * (len(text2) + 1)
    for ch1 in text1:
        cur = [0] * (len(text2) + 1)
        for j, ch2 in enumerate(text2, 1):
            if ch1 == ch2:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]


if __name__ == "__main__":
    tests = [
        ("P1 rob", p1_rob, ([2, 7, 9, 3, 1],), 12),
        ("P1 rob single house", p1_rob, ([5],), 5),
        ("P1 rob empty", p1_rob, ([],), 0),
        ("P1 rob adjacent pair", p1_rob, ([2, 1, 1, 2],), 4),
        ("P2 unique_paths", p2_unique_paths, (3, 7), 28),
        ("P2 unique_paths 2x3", p2_unique_paths, (2, 3), 3),
        ("P2 unique_paths 1x1", p2_unique_paths, (1, 1), 1),
        ("P2 unique_paths 1 row", p2_unique_paths, (1, 5), 1),
        ("P3 lcs", p3_lcs, ("abcde", "ace"), 3),
        ("P3 lcs identical", p3_lcs, ("abc", "abc"), 3),
        ("P3 lcs no common", p3_lcs, ("abc", "def"), 0),
        ("P3 lcs empty", p3_lcs, ("", "abc"), 0),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
