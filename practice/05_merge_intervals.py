"""
CONCEPT: Merge Intervals

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/05_merge_intervals.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Merge Intervals  (LeetCode 56)
#
# Given a list of intervals, where each interval is [start, end], merge all
# overlapping intervals and return the resulting non-overlapping intervals
# sorted by start. Two intervals overlap when one starts at or before the
# other ends. An empty input yields an empty result.
#
# Example 1:
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
# Example 2:
#   Input: intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#
# Constraints:
#   - 0 <= len(intervals) <= 10^4
#   - intervals[i] = [start, end] with start <= end
# ---------------------------------------------------------------------------
def p1_merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda iv: iv[0])
    merged = [intervals[0][:]]

    for start, end in intervals[1:]:
        last = merged[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    
    return merged


# ---------------------------------------------------------------------------
# Problem 2 - Insert Interval  (LeetCode 57)
#
# You are given a list of non-overlapping intervals sorted by start, plus a
# new interval [start, end]. Insert the new interval and merge any intervals
# that now overlap, returning the result sorted by start. An empty list means
# the answer is just the new interval.
#
# Example 1:
#   Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]
# Example 2:
#   Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#   Output: [[1,2],[3,10],[12,16]]
#
# Constraints:
#   - 0 <= len(intervals) <= 10^4
#   - intervals is sorted by start and intervals are non-overlapping
#   - newInterval = [start, end] with start <= end
# ---------------------------------------------------------------------------
def p2_insert(intervals, newInterval):
    result = []
    start, end = newInterval
    i, n = 0, len(intervals)

    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result



# ---------------------------------------------------------------------------
# Problem 3 - Non-overlapping Intervals  (LeetCode 435)
#
# Given a list of intervals [start, end], return the minimum number of
# intervals you must remove so that the remaining intervals do not overlap.
# Two intervals that only touch at an endpoint (one ends where the next
# starts) do not count as overlapping. An empty input needs no removals.
#
# Example 1:
#   Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1
# Example 2:
#   Input: intervals = [[1,2],[1,2],[1,2]]
#   Output: 2
#
# Constraints:
#   - 0 <= len(intervals) <= 10^4
#   - intervals[i] = [start, end] with start <= end
# ---------------------------------------------------------------------------
def p3_non_overlapping(intervals):
    if not intervals:
        return 0
    
    intervals = sorted(intervals, key=lambda iv: iv[1])
    removed, last_end = 0, intervals[0][1]

    for start, end in intervals[1:]:
        if start < last_end:
            removed += 1
        else:
            last = end
        
    return removed



if __name__ == "__main__":
    tests = [
        ("P1 merge", p1_merge, ([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
        ("P1 merge touching", p1_merge, ([[1, 4], [4, 5]],), [[1, 5]]),
        ("P1 merge nested", p1_merge, ([[1, 4], [0, 4]],), [[0, 4]]),
        ("P1 merge empty", p1_merge, ([],), []),
        ("P2 insert middle", p2_insert, ([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
        ("P2 insert overlap", p2_insert, ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]]),
        ("P2 insert inside", p2_insert, ([[1, 5]], [2, 3]), [[1, 5]]),
        ("P2 insert empty", p2_insert, ([], [5, 7]), [[5, 7]]),
        ("P3 non_overlapping", p3_non_overlapping, ([[1, 2], [2, 3], [3, 4], [1, 3]],), 1),
        ("P3 all duplicates", p3_non_overlapping, ([[1, 2], [1, 2], [1, 2]],), 2),
        ("P3 touching", p3_non_overlapping, ([[1, 2], [2, 3]],), 0),
        ("P3 empty", p3_non_overlapping, ([],), 0),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
