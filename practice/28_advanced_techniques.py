"""
CONCEPT: Advanced Techniques

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/28_advanced_techniques.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Sliding Window Maximum  (LeetCode 239)
#
# You are given a list `nums` and a window size k. A sliding window of size k
# moves from the very left of the list to the very right, one position at a
# time. Return the list of the maximum value inside each window.
#
# An empty `nums` (or k == 0) yields an empty result.
#
# Example 1:
#   Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
#   Output: [3, 3, 5, 5, 6, 7]
#   Explanation: the windows are [1,3,-1] -> 3, [3,-1,-3] -> 3,
#   [-1,-3,5] -> 5, [-3,5,3] -> 5, [5,3,6] -> 6, [3,6,7] -> 7.
# Example 2:
#   Input: nums = [1], k = 1
#   Output: [1]
#
# Constraints:
#   - 0 <= len(nums) <= 10^5
#   - 1 <= k <= len(nums) when nums is non-empty
#
# Required complexity: O(n), with a monotonic (decreasing) deque holding
# indices; each index is pushed and popped at most once. An O(n log k) heap
# solution is not accepted here.
# ---------------------------------------------------------------------------
def p1_max_sliding_window(nums, k):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 2 - Kth Largest Element in an Array  (LeetCode 215)
#
# Given a list `nums` and an integer k, return the k-th largest element in
# the list. Note that it is the k-th largest in sorted order, not the k-th
# distinct element.
#
# Example 1:
#   Input: nums = [3, 2, 1, 5, 6, 4], k = 2
#   Output: 5
#   Explanation: sorted descending, the 2nd value is 5.
# Example 2:
#   Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
#   Output: 4
#   Explanation: sorted descending, the 4th value is 4 (duplicates count).
#
# Constraints:
#   - 1 <= k <= len(nums) <= 10^5
#
# Required complexity: quickselect, average O(n). Sorting the whole array is
# not accepted. The test values are unique by construction, so any correct
# quickselect passes regardless of the pivot rule you pick - do not use
# randomness.
# ---------------------------------------------------------------------------
def p2_find_kth_largest(nums, k):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Problem 3 - Meeting Rooms II  (LeetCode 253)
#
# Given a list of meeting time intervals [start, end], return the minimum
# number of conference rooms required to hold all of them. Meetings that only
# touch at an endpoint (one ends exactly when the next starts) can share a
# room, i.e. the intervals are half-open [start, end).
#
# Example 1:
#   Input: intervals = [[0, 30], [5, 10], [15, 20]]
#   Output: 2
#   Explanation: [0,30] overlaps both others, but [5,10] and [15,20] do not
#   overlap each other, so 2 rooms suffice.
# Example 2:
#   Input: intervals = [[7, 10], [2, 4]]
#   Output: 1
#
# Constraints:
#   - 0 <= len(intervals) <= 10^4
#   - intervals[i] = [start, end] with start < end
#
# Required complexity: O(n log n). Both standard approaches are accepted:
# a sweep line over sorted events (+1 at a start, -1 at an end) or a sort by
# start plus a min-heap of end times.
# ---------------------------------------------------------------------------
def p3_min_meeting_rooms(intervals):
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ("P1 max_sliding_window", p1_max_sliding_window, ([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        ("P1 window of one", p1_max_sliding_window, ([1, -1], 1), [1, -1]),
        ("P1 window equals array", p1_max_sliding_window, ([1, 2, 3, 4], 4), [4]),
        ("P1 all identical", p1_max_sliding_window, ([9, 9, 9], 2), [9, 9]),
        ("P1 decreasing", p1_max_sliding_window, ([5, 4, 3, 2, 1], 2), [5, 4, 3, 2]),
        ("P1 empty", p1_max_sliding_window, ([], 0), []),
        ("P2 kth_largest", p2_find_kth_largest, ([3, 2, 1, 5, 6, 4], 2), 5),
        ("P2 kth_largest duplicates", p2_find_kth_largest, ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
        ("P2 k = 1", p2_find_kth_largest, ([1, 2, 3], 1), 3),
        ("P2 k = len(nums)", p2_find_kth_largest, ([3, 1, 2], 3), 1),
        ("P2 all identical", p2_find_kth_largest, ([7, 7, 7], 2), 7),
        ("P2 single element", p2_find_kth_largest, ([5], 1), 5),
        ("P3 min_meeting_rooms", p3_min_meeting_rooms, ([[0, 30], [5, 10], [15, 20]],), 2),
        ("P3 two disjoint meetings", p3_min_meeting_rooms, ([[7, 10], [2, 4]],), 1),
        ("P3 no meetings", p3_min_meeting_rooms, ([],), 0),
        ("P3 touching at endpoints", p3_min_meeting_rooms, ([[1, 2], [2, 3]],), 1),
        ("P3 all identical", p3_min_meeting_rooms, ([[1, 5], [1, 5], [1, 5]],), 3),
        ("P3 one meeting", p3_min_meeting_rooms, ([[4, 9]],), 1),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
