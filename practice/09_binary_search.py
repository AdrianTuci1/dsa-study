"""
CONCEPT: Binary Search (including search on the answer)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/09_binary_search.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Binary Search  (LeetCode 704)
#
# Given a list of integers `nums` sorted in ascending order and an integer
# `target`, return the index of `target` in `nums`, or -1 if it is not there.
# Do it in O(log n) time by keeping two indices (lo, hi) and halving the
# remaining range on every step. Do not use `in` or `list.index`.
#
# Example 1:
#   Input: nums = [-1,0,3,5,9,12], target = 9
#   Output: 4
# Example 2:
#   Input: nums = [-1,0,3,5,9,12], target = 2
#   Output: -1
#
# Constraints:
#   - 0 <= len(nums) <= 10^4
#   - nums is sorted in strictly increasing order
#   - Every value fits in a 32-bit integer
# ---------------------------------------------------------------------------
def p1_binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1



# ---------------------------------------------------------------------------
# Problem 2 - Find Minimum in Rotated Sorted Array  (LeetCode 153)
#
# `nums` is a list of distinct integers that was sorted in ascending order and
# then rotated some number of positions (for example [0,1,2,4,5,6,7] may become
# [4,5,6,7,0,1,2]). Return the smallest value in O(log n) time. Compare the
# middle element with the last element to decide which half still contains the
# rotation point.
#
# Example 1:
#   Input: nums = [3,4,5,1,2]
#   Output: 1
# Example 2:
#   Input: nums = [4,5,6,7,0,1,2]
#   Output: 0
#
# Constraints:
#   - 1 <= len(nums) <= 5000
#   - All values are distinct
# ---------------------------------------------------------------------------
def p2_find_min(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]



# ---------------------------------------------------------------------------
# Problem 3 - Koko Eating Bananas  (LeetCode 875, search on the answer)
#
# There are `len(piles)` piles of bananas; pile i has `piles[i]` bananas.
# Koko picks an integer speed k (bananas per hour) and eats one pile per hour:
# during an hour she eats min(k, remaining) bananas from the current pile, and
# she never mixes two piles in the same hour. Return the smallest integer speed
# k such that she can finish all piles within `h` hours. Binary search the
# answer over the range [1, max(piles)] instead of searching the list.
#
# Example 1:
#   Input: piles = [3,6,7,11], h = 8
#   Output: 4
# Example 2:
#   Input: piles = [30,11,23,4,20], h = 5
#   Output: 30
#
# Constraints:
#   - 1 <= len(piles) <= 10^4
#   - 1 <= piles[i] <= 10^9
#   - len(piles) <= h <= 10^9
# ---------------------------------------------------------------------------
def p3_min_eating_speed(piles, h):
    def hours_needed(k):
        return sum((p + k - 1) // k for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo



if __name__ == "__main__":
    tests = [
        ("P1 binary_search", p1_binary_search, ([-1, 0, 3, 5, 9, 12], 9), 4),
        ("P1 binary_search not found", p1_binary_search, ([-1, 0, 3, 5, 9, 12], 2), -1),
        ("P1 binary_search empty list", p1_binary_search, ([], 5), -1),
        ("P1 binary_search single element", p1_binary_search, ([5], 5), 0),
        ("P2 find_min rotated", p2_find_min, ([3, 4, 5, 1, 2],), 1),
        ("P2 find_min rotated to zero", p2_find_min, ([4, 5, 6, 7, 0, 1, 2],), 0),
        ("P2 find_min not rotated", p2_find_min, ([11, 13, 15, 17],), 11),
        ("P2 find_min single element", p2_find_min, ([1],), 1),
        ("P3 min_eating_speed simple", p3_min_eating_speed, ([3, 6, 7, 11], 8), 4),
        ("P3 min_eating_speed slowest pile", p3_min_eating_speed, ([30, 11, 23, 4, 20], 5), 30),
        ("P3 min_eating_speed relaxed deadline", p3_min_eating_speed, ([30, 11, 23, 4, 20], 6), 23),
        ("P3 min_eating_speed one pile one hour", p3_min_eating_speed, ([1], 1), 1),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
