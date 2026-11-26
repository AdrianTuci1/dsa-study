"""
CONCEPT: Array & Hashing

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/01_array_hashing.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Two Sum  (LeetCode 1)
#
# Given a list of integers `nums` and an integer `target`, return the indices
# of the two numbers that add up to `target` as a list [i, j] with i < j.
# Assume that every input has exactly one valid answer, and the same element
# may not be used twice. Using a hash map lets you solve it in one pass.
#
# Example 1:
#   Input: nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#   Explanation: because nums[0] + nums[1] == 9
# Example 2:
#   Input: nums = [3, 2, 4], target = 6
#   Output: [1, 2]
#
# Constraints:
#   - 2 <= len(nums) <= 10^4
#   - exactly one valid answer exists
# ---------------------------------------------------------------------------
def p1_two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return[seen[need], i]
        seen[x] = i
    return []
    


# ---------------------------------------------------------------------------
# Problem 2 - Valid Anagram  (LeetCode 242)
#
# Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
# meaning `t` uses exactly the same characters with the same multiplicities.
# The comparison is case sensitive and counts every character, including
# spaces and punctuation.
#
# Example 1:
#   Input: s = "anagram", t = "nagaram"
#   Output: True
# Example 2:
#   Input: s = "rat", t = "car"
#   Output: False
#
# Constraints:
#   - 0 <= len(s), len(t) <= 5 * 10^4
#   - s and t consist of printable characters
# ---------------------------------------------------------------------------
def p2_is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    for char in t:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] < 0:
            return False
    return True


# ---------------------------------------------------------------------------
# Problem 3 - Longest Consecutive Sequence  (LeetCode 128)
#
# Given an unsorted list of integers `nums`, return the length of the longest
# run of consecutive integers present in the list. The numbers do not need to
# be adjacent in the input, and duplicates simply do not extend a run. Aim for
# an O(n) solution by putting the values in a set.
#
# Example 1:
#   Input: nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
#   Explanation: the longest run is [1, 2, 3, 4]
# Example 2:
#   Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   Output: 9
#
# Constraints:
#   - 0 <= len(nums) <= 10^5
#   - -10^9 <= nums[i] <= 10^9
# ---------------------------------------------------------------------------
def p3_longest_consecutive(nums):
    present = set(nums)
    longest = 0

    for n in present:
        if n - 1 not in present:
            length = 1
            while n + length in present:
                length += 1
            longest = max(longest, length)
            
    return longest




if __name__ == "__main__":
    tests = [
        ("P1 two_sum", p1_two_sum, ([2, 7, 11, 15], 9), [0, 1]),
        ("P1 two_sum", p1_two_sum, ([3, 2, 4], 6), [1, 2]),
        ("P1 two_sum", p1_two_sum, ([3, 3], 6), [0, 1]),
        ("P1 two_sum", p1_two_sum, ([-3, 4, 3, 90], 0), [0, 2]),

        ("P2 is_anagram", p2_is_anagram, ("anagram", "nagaram"), True),
        ("P2 is_anagram", p2_is_anagram, ("rat", "car"), False),
        ("P2 is_anagram", p2_is_anagram, ("aacc", "ccac"), False),
        ("P2 is_anagram", p2_is_anagram, ("", ""), True),

        ("P3 longest_consecutive", p3_longest_consecutive, ([100, 4, 200, 1, 3, 2],), 4),
        ("P3 longest_consecutive", p3_longest_consecutive, ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
        ("P3 longest_consecutive", p3_longest_consecutive, ([1],), 1),
        ("P3 longest_consecutive", p3_longest_consecutive, ([],), 0),
        ("P3 longest_consecutive", p3_longest_consecutive, ([-3, -2, -1, 0],), 4),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
