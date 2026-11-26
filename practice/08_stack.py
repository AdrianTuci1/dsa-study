"""
CONCEPT: Stack (including monotonic stack)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/08_stack.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Valid Parentheses  (LeetCode 20)
#
# Given a string containing only the characters '(', ')', '{', '}', '[' and
# ']', decide whether the brackets are correctly matched and closed in the
# right order. An empty string is considered valid.
#
# Example 1:
#   Input: s = "()[]{}"
#   Output: True
# Example 2:
#   Input: s = "([)]"
#   Output: False
#
# Constraints:
#   - 0 <= len(s) <= 10^4
#   - s contains only the six bracket characters
# ---------------------------------------------------------------------------
def p1_valid_parens(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in pairs: # e paranteza de inchidere

            if not stack or stack.pop() != pairs[ch]:
                return False #nu am ce inchide sau nu se potriveste
        else:    # e paranteza de deschidere
            stack.append(ch)

    return not stack #nimic nu a ramas deschis



# ---------------------------------------------------------------------------
# Problem 2 - Next Greater Element I  (LeetCode 496)
#
# Given two lists nums1 and nums2 where nums1 is a subset of nums2, return a
# list where each answer[i] is the first element to the right of nums1[i] in
# nums2 that is greater than it, or -1 if no such element exists. Use a
# monotonic stack over nums2.
#
# Example 1:
#   Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
#   Output: [-1,3,-1]
# Example 2:
#   Input: nums1 = [2,4], nums2 = [1,2,3,4]
#   Output: [3,-1]
#
# Constraints:
#   - 1 <= len(nums1) <= len(nums2) <= 1000
#   - all values in nums2 are unique
# ---------------------------------------------------------------------------
def p2_next_greater(nums1, nums2):
    nxt = {}
    stack = []

    for v in nums2:
        while stack and stack[-1] < v:
            nxt[stack.pop()] = v
        stack.append(v)
    
    return [nxt.get(v, -1) for v in nums1]




# ---------------------------------------------------------------------------
# Problem 3 - Daily Temperatures  (LeetCode 739)
#
# Given a list of daily temperatures, return a list where answer[i] is the
# number of days you must wait after day i to get a warmer temperature. If no
# warmer day exists, answer[i] is 0. Use a monotonic stack.
#
# Example 1:
#   Input: temperatures = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
# Example 2:
#   Input: temperatures = [30,40,50,60]
#   Output: [1,1,1,0]
#
# Constraints:
#   - 1 <= len(temperatures) <= 10^5
#   - 30 <= temperatures[i] <= 100
# ---------------------------------------------------------------------------
def p3_daily_temps(temperatures):
    res = [0] * len(temperatures) #implicit 0: zilele nerezolvate raman asa
    stack = [] #indexuri, temperaturi strict descrescatoare

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j #distanta, nu valoarea
        stack.append(i)

    return res



if __name__ == "__main__":
    tests = [
        ("P1 valid_parens", p1_valid_parens, ("()[]{}",), True),
        ("P1 valid_parens simple", p1_valid_parens, ("()",), True),
        ("P1 valid_parens invalid", p1_valid_parens, ("(]",), False),
        ("P1 valid_parens interleaved", p1_valid_parens, ("([)]",), False),
        ("P1 valid_parens empty", p1_valid_parens, ("",), True),
        ("P2 next_greater", p2_next_greater, ([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
        ("P2 next_greater ascending", p2_next_greater, ([2, 4], [1, 2, 3, 4]), [3, -1]),
        ("P2 next_greater single", p2_next_greater, ([1], [1]), [-1]),
        ("P2 next_greater descending", p2_next_greater, ([5, 3], [5, 4, 3]), [-1, -1]),
        ("P3 daily_temps", p3_daily_temps, ([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
        ("P3 daily_temps ascending", p3_daily_temps, ([30, 40, 50, 60],), [1, 1, 1, 0]),
        ("P3 daily_temps descending", p3_daily_temps, ([90, 80, 70],), [0, 0, 0]),
        ("P3 daily_temps single", p3_daily_temps, ([55],), [0]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
