"""
CONCEPT: Two Pointers

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/02_two_pointers.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Valid Palindrome  (LeetCode 125)
#
# Given a string `s`, return True if it reads the same forwards and backwards
# once you ignore every character that is not a letter or a digit and compare
# letters case-insensitively. An empty string (or a string with no letters or
# digits) counts as a palindrome.
#
# Example 1:
#   Input: s = "A man, a plan, a canal: Panama"
#   Output: True
#   Explanation: after cleaning, the string is "amanaplanacanalpanama"
# Example 2:
#   Input: s = "race a car"
#   Output: False
#
# Constraints:
#   - 0 <= len(s) <= 2 * 10^5
#   - s consists of printable ASCII characters
# ---------------------------------------------------------------------------
def p1_is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# ---------------------------------------------------------------------------
# Problem 2 - Two Sum II (sorted input)  (LeetCode 167)
#
# Given a 1-indexed list of integers `numbers` sorted in non-decreasing order
# and a `target`, return the 1-indexed positions [i, j] (with i < j) of the two
# numbers that add up to `target`. Exactly one solution exists and you may not
# use the same element twice. Use the sorted order and two pointers rather than
# a hash map.
#
# Example 1:
#   Input: numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]
#   Explanation: numbers[1 - 1] + numbers[2 - 1] == 9
# Example 2:
#   Input: numbers = [2, 3, 4], target = 6
#   Output: [1, 3]
#
# Constraints:
#   - 2 <= len(numbers) <= 3 * 10^4
#   - -1000 <= numbers[i] <= 1000
#   - exactly one valid answer exists
# ---------------------------------------------------------------------------
def p2_two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


# ---------------------------------------------------------------------------
# Problem 3 - Container With Most Water  (LeetCode 11)
#
# You are given a list `height` where height[i] is the height of a vertical
# line drawn at position i. Pick two lines that together with the x-axis form
# a container holding the most water, and return that maximum area. The area
# is min(height[left], height[right]) * (right - left).
#
# Example 1:
#   Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
#   Explanation: choose the lines at index 1 and index 8
# Example 2:
#   Input: height = [1, 1]
#   Output: 1
#
# Constraints:
#   - 2 <= len(height) <= 10^5
#   - 0 <= height[i] <= 10^4
# ---------------------------------------------------------------------------
def p3_max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > best:
            best = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    tests = [
        ("P1 is_palindrome", p1_is_palindrome, ("A man, a plan, a canal: Panama",), True),
        ("P1 is_palindrome", p1_is_palindrome, ("race a car",), False),
        ("P1 is_palindrome", p1_is_palindrome, ("",), True),
        ("P1 is_palindrome", p1_is_palindrome, ("0P",), False),
        ("P1 is_palindrome", p1_is_palindrome, ("aa",), True),

        ("P2 two_sum_sorted", p2_two_sum_sorted, ([2, 7, 11, 15], 9), [1, 2]),
        ("P2 two_sum_sorted", p2_two_sum_sorted, ([2, 3, 4], 6), [1, 3]),
        ("P2 two_sum_sorted", p2_two_sum_sorted, ([-1, 0], -1), [1, 2]),
        ("P2 two_sum_sorted", p2_two_sum_sorted, ([-5, -3, -1, 2], -4), [2, 3]),
        ("P2 two_sum_sorted", p2_two_sum_sorted, ([1, 2], 3), [1, 2]),

        ("P3 max_area", p3_max_area, ([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        ("P3 max_area", p3_max_area, ([1, 1],), 1),
        ("P3 max_area", p3_max_area, ([1, 2, 1],), 2),
        ("P3 max_area", p3_max_area, ([4, 3, 2, 1, 4],), 16),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
