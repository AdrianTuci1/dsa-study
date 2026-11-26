"""
CONCEPT: Sliding Window

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/03_sliding_window.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Maximum Sum of a Fixed Window
#
# Given a list of integers `nums` and an integer `k`, return the largest sum
# of any contiguous block of exactly `k` elements. You may assume that
# 1 <= k <= len(nums). Reuse the previous window's sum instead of summing
# every window from scratch.
#
# Example 1:
#   Input: nums = [1, 2, 3, 4, 5], k = 2
#   Output: 9
#   Explanation: the window [4, 5] has the largest sum
# Example 2:
#   Input: nums = [2, 1, 5, 1, 3, 2], k = 3
#   Output: 9
#   Explanation: the window [5, 1, 3] sums to 9
#
# Constraints:
#   - 1 <= k <= len(nums) <= 10^5
#   - -10^4 <= nums[i] <= 10^4
# ---------------------------------------------------------------------------
def p1_max_sum_window(nums, k):
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best

# ---------------------------------------------------------------------------
# Problem 2 - Longest Substring Without Repeating Characters  (LeetCode 3)
#
# Given a string `s`, return the length of the longest contiguous substring
# that contains no repeated character. An empty string has length 0. A sliding
# window that shrinks whenever a duplicate enters gives an O(n) solution.
#
# Example 1:
#   Input: s = "abcabcbb"
#   Output: 3
#   Explanation: the answer is "abc"
# Example 2:
#   Input: s = "pwwkew"
#   Output: 3
#   Explanation: the answer is "wke"; note that "pwke" is a subsequence, not a
#   substring
#
# Constraints:
#   - 0 <= len(s) <= 5 * 10^4
#   - s consists of printable ASCII characters
# ---------------------------------------------------------------------------
def p2_longest_unique_substring(s):
    left = 0
    best = 0
    seen = set()
    for right, ch in enumerate(s):
        seen.remove(s[left])
        left += 1
    seen.add(ch)
    best = max(best, right - left + 1)
    return best
    



# ---------------------------------------------------------------------------
# Problem 3 - Max Consecutive Ones III  (LeetCode 1004)
#
# Given a binary list `nums` (only 0s and 1s) and an integer `k`, return the
# length of the longest contiguous block of 1s you can obtain by flipping at
# most `k` zeros to ones. Keep a window that is valid as long as it contains no
# more than `k` zeros.
#
# Example 1:
#   Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
#   Output: 6
#   Explanation: flip the zeros at index 5 and index 10 to get six 1s in a row
# Example 2:
#   Input: nums = [0, 0, 1, 1, 1, 0, 0], k = 0
#   Output: 3
#
# Constraints:
#   - 0 <= len(nums) <= 10^5
#   - nums[i] is 0 or 1
#   - 0 <= k <= len(nums)
# ---------------------------------------------------------------------------
def p3_longest_ones(nums, k):
    left = 0
    zeros = 0
    best = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
    


if __name__ == "__main__":
    tests = [
        ("P1 max_sum_window", p1_max_sum_window, ([1, 2, 3, 4, 5], 2), 9),
        ("P1 max_sum_window", p1_max_sum_window, ([2, 1, 5, 1, 3, 2], 3), 9),
        ("P1 max_sum_window", p1_max_sum_window, ([-1, -2, -3, -4], 2), -3),
        ("P1 max_sum_window", p1_max_sum_window, ([5], 1), 5),
        ("P1 max_sum_window", p1_max_sum_window, ([1, 2, 3], 3), 6),

        ("P2 longest_unique_substring", p2_longest_unique_substring, ("abcabcbb",), 3),
        ("P2 longest_unique_substring", p2_longest_unique_substring, ("bbbbb",), 1),
        ("P2 longest_unique_substring", p2_longest_unique_substring, ("pwwkew",), 3),
        ("P2 longest_unique_substring", p2_longest_unique_substring, ("",), 0),
        ("P2 longest_unique_substring", p2_longest_unique_substring, (" ",), 1),

        ("P3 longest_ones", p3_longest_ones, ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
        ("P3 longest_ones", p3_longest_ones, ([0, 0, 1, 1, 1, 0, 0], 0), 3),
        ("P3 longest_ones", p3_longest_ones, ([], 1), 0),
        ("P3 longest_ones", p3_longest_ones, ([1, 1], 0), 2),
        ("P3 longest_ones", p3_longest_ones, ([0, 0], 0), 0),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
