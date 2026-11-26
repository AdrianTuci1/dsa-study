"""
CONCEPT: Two Heaps / Heap (median, top-k)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/12_two_heaps.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
import heapq

from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Kth Largest Element in an Array  (LeetCode 215)
#
# Given a list of integers `nums` and an integer k, return the k-th largest
# value in the list (counting duplicates, so it is the value at index len-1-k
# after sorting ascending). Use a min-heap of size k: push every value and pop
# the smallest whenever the heap grows past k. You may not simply sort - aim for
# O(n log k).
#
# Example 1:
#   Input: nums = [3,2,1,5,6,4], k = 2
#   Output: 5
# Example 2:
#   Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#   Output: 4
#
# Constraints:
#   - 1 <= k <= len(nums) <= 10^5
#   - -10^4 <= nums[i] <= 10^4
# ---------------------------------------------------------------------------
def p1_find_kth_largest(nums, k):
    heap = []
    for v in nums:
        heapq.heappush(heap, v)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]



# ---------------------------------------------------------------------------
# Problem 2 - Top K Frequent Elements  (LeetCode 347)
#
# Given a list of integers `nums` and an integer k, return the k most frequent
# values. To keep the output deterministic, the result must be sorted by
# frequency in decreasing order, and values with the same frequency must come in
# increasing order of value. Use a counter plus a heap of size k (or an
# equivalent frequency bucket approach).
#
# Example 1:
#   Input: nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# Example 2:
#   Input: nums = [1,2], k = 2
#   Output: [1, 2]      (both appear once, so the smaller value comes first)
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - k is in the range [1, number of distinct values in nums]
# ---------------------------------------------------------------------------
def p2_top_k_frequent(nums, k):
    counts = Counter(nums)
    heap = []
    for value, freq in counts.items():
        heapq.heappush(heap, (freq, -value, value))
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted((value for _, _, value in heap), key=lambda v:(-counts[v], v))


# ---------------------------------------------------------------------------
# Problem 3 - Running Median of a Stream  (LeetCode 295, function version)
#
# Numbers arrive one at a time, and after every arrival you must report the
# median of all numbers seen so far. Return a list with one median per insertion;
# a median is a float, and when there is an even count it is the average of the
# two middle values. Use two heaps: a max-heap for the lower half and a min-heap
# for the upper half, kept within one element of each other.
#
# Example 1:
#   Input: nums = [1,2]
#   Output: [1.0, 1.5]
# Example 2:
#   Input: nums = [2,1,5,7]
#   Output: [2.0, 1.5, 2.0, 3.5]
#
# Constraints:
#   - 0 <= len(nums) <= 10^5
#   - -10^5 <= nums[i] <= 10^5
# ---------------------------------------------------------------------------
def p3_median_of_stream(nums):
    lo, hi = [], []
    medians = []
    for v in nums:
        heapq.heappush(lo, -v)
        heapq.heappush(hi, -heapq.heappop(lo))
        if len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))
        if len(lo) > len(hi):
            medians.append(float(-lo[0]))
        else:
            medians.append((-lo[0] + hi[0]) / 2)
    return medians




if __name__ == "__main__":
    tests = [
        ("P1 find_kth_largest", p1_find_kth_largest, ([3, 2, 1, 5, 6, 4], 2), 5),
        ("P1 find_kth_largest with duplicates", p1_find_kth_largest, ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
        ("P1 find_kth_largest single element", p1_find_kth_largest, ([1], 1), 1),
        ("P1 find_kth_largest negatives", p1_find_kth_largest, ([-1, -2, -3], 1), -1),
        ("P2 top_k_frequent", p2_top_k_frequent, ([1, 1, 1, 2, 2, 3], 2), [1, 2]),
        ("P2 top_k_frequent single value", p2_top_k_frequent, ([1], 1), [1]),
        ("P2 top_k_frequent all equal counts", p2_top_k_frequent, ([1, 2], 2), [1, 2]),
        ("P2 top_k_frequent tie breaks by smaller value", p2_top_k_frequent, ([2, 2, 1, 1, 3], 1), [1]),
        ("P3 median_of_stream", p3_median_of_stream, ([1, 2],), [1.0, 1.5]),
        ("P3 median_of_stream longer run", p3_median_of_stream, ([2, 1, 5, 7, 2, 0, 5],), [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]),
        ("P3 median_of_stream empty", p3_median_of_stream, ([],), []),
        ("P3 median_of_stream negatives", p3_median_of_stream, ([-1, -2],), [-1.0, -1.5]),
        ("P3 median_of_stream duplicates", p3_median_of_stream, ([1, 1, 1],), [1.0, 1.0, 1.0]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
