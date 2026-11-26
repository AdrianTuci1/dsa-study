"""
CONCEPT: Advanced DP (0/1 knapsack, LIS, edit distance)

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/25_advanced_dp.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from bisect import bisect_left

from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - 0/1 Knapsack
#
# You are given `weights` and `values` of the same length n (item i has weight
# weights[i] and value values[i]) and a knapsack of capacity `capacity`. Each
# item can be taken at most once (hence "0/1"). Return the maximum total value
# that fits into the knapsack.
#
# Solve it with a 1-D rolling array and aim for O(n * W) time and O(W) space,
# where W = capacity, by updating a single array with a loop that goes over the
# capacity in reverse.
#
# Example 1:
#   Input: weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7
#   Output: 9
#   Explanation: take the items of weight 3 and 4 (values 4 + 5 = 9, total
#     weight 7), which is the best combination that fits.
# Example 2:
#   Input: weights = [2, 3, 4, 5], values = [3, 4, 5, 6], capacity = 5
#   Output: 7
#   Explanation: take the items of weight 2 and 3 (values 3 + 4 = 7).
#
# Constraints:
#   - 0 <= n <= 100
#   - 0 <= capacity <= 1000
#   - 1 <= weights[i] <= 1000
#   - 0 <= values[i] <= 1000
#   - An empty item list or capacity = 0 yields 0.
# ---------------------------------------------------------------------------
def p1_knapsack(weights, values, capacity):
    # dp[c] = best value with capacity c, using the items seen so far.
    # Each item: dp[c] = max(dp[c], dp[c - w] + v).
    # The capacity loop MUST go downwards: dp[c - w] then still belongs to the
    # previous item row, which is exactly what makes it 0/1 (one use per item).
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        if w > capacity:
            continue
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


# ---------------------------------------------------------------------------
# Problem 2 - Longest Increasing Subsequence  (LeetCode 300)
#
# Given an integer list `nums`, return the length of the longest strictly
# increasing subsequence. A subsequence is obtained by deleting some or no
# elements without changing the order of the remaining elements.
#
# Both the O(n^2) DP version (dp[i] = length of the longest increasing
# subsequence that ends at index i) and the O(n log n) patience sorting
# version are acceptable for the tests below.
#
# Example 1:
#   Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
#   Output: 4
#   Explanation: [2, 3, 7, 101] is strictly increasing, and no longer one
#     exists.
# Example 2:
#   Input: nums = [0, 1, 0, 3, 2, 3]
#   Output: 4
#   Explanation: [0, 1, 2, 3] is strictly increasing.
#
# Constraints:
#   - 0 <= len(nums) <= 2500
#   - -10^4 <= nums[i] <= 10^4
#   - An empty list yields 0 and a single element yields 1.
#
# Follow-up (required): implement the O(n log n) version using patience
# sorting - keep a `tails` list and use bisect_left to replace the first
# element that is >= nums[i]. The O(n^2) DP passes the tests but is not the
# intended solution.
# ---------------------------------------------------------------------------
def p2_length_of_lis(nums):
    # Patience sorting, O(n log n). tails[k] is the smallest possible tail of
    # an increasing subsequence of length k + 1. For each x, replace the first
    # tail that is >= x (bisect_left), or append x if none is:
    #   - replacing keeps tails as small as possible, which is never worse;
    #   - appending means x extends the longest subsequence built so far.
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


# ---------------------------------------------------------------------------
# Problem 3 - Edit Distance  (LeetCode 72)
#
# Given two strings `word1` and `word2`, return the minimum number of
# operations required to turn word1 into word2. The allowed operations are:
# insert a character, delete a character, and replace a character.
#
# Example 1:
#   Input: word1 = "horse", word2 = "ros"
#   Output: 3
#   Explanation: horse -> rorse (replace 'h' with 'r') -> rose (delete 'r')
#     -> ros (delete 'e').
# Example 2:
#   Input: word1 = "intention", word2 = "execution"
#   Output: 5
#   Explanation: intention -> inention (delete 't') -> enention (replace 'i'
#     with 'e') -> exention (replace 'n' with 'x') -> exection (replace 'n'
#     with 'c') -> execution (insert 'u').
#
# Constraints:
#   - 0 <= len(word1), len(word2) <= 500
#   - word1 and word2 consist of lowercase English letters.
#   - Two empty strings have distance 0.
# ---------------------------------------------------------------------------
def p3_min_distance(word1, word2):
    # dp[i][j] = edit distance between word1[:i] and word2[:j].
    #   same last char -> dp[i-1][j-1]
    #   different      -> 1 + min(
    #                        dp[i-1][j],    delete word1[i-1]
    #                        dp[i][j-1],    insert word2[j-1]
    #                        dp[i-1][j-1])  replace
    # Row 0 is 0..n (insertions) and column 0 is 0..m (deletions).
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        cur[0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j - 1], prev[j], cur[j - 1])
        prev = cur
    return prev[n]


if __name__ == "__main__":
    tests = [
        ("P1 knapsack", p1_knapsack, ([1, 3, 4, 5], [1, 4, 5, 7], 7), 9),
        ("P1 knapsack tight capacity", p1_knapsack, ([2, 3, 4, 5], [3, 4, 5, 6], 5), 7),
        ("P1 knapsack capacity zero", p1_knapsack, ([2, 3], [5, 6], 0), 0),
        ("P1 knapsack no items", p1_knapsack, ([], [], 10), 0),
        ("P1 knapsack item too heavy", p1_knapsack, ([7], [100], 6), 0),
        ("P1 knapsack all items fit", p1_knapsack, ([1, 2, 3, 4], [1, 2, 3, 4], 10), 10),
        ("P1 knapsack single item fits", p1_knapsack, ([2], [3], 2), 3),
        ("P2 length_of_lis", p2_length_of_lis, ([10, 9, 2, 5, 3, 7, 101, 18],), 4),
        ("P2 length_of_lis repeats", p2_length_of_lis, ([0, 1, 0, 3, 2, 3],), 4),
        ("P2 length_of_lis all equal", p2_length_of_lis, ([7, 7, 7, 7, 7],), 1),
        ("P2 length_of_lis empty", p2_length_of_lis, ([],), 0),
        ("P2 length_of_lis single", p2_length_of_lis, ([1],), 1),
        ("P2 length_of_lis decreasing", p2_length_of_lis, ([5, 4, 3, 2, 1],), 1),
        ("P2 length_of_lis mixed", p2_length_of_lis, ([4, 10, 4, 3, 8, 9],), 3),
        ("P3 min_distance", p3_min_distance, ("horse", "ros"), 3),
        ("P3 min_distance", p3_min_distance, ("intention", "execution"), 5),
        ("P3 min_distance empty target", p3_min_distance, ("abc", ""), 3),
        ("P3 min_distance empty source", p3_min_distance, ("", "abc"), 3),
        ("P3 min_distance both empty", p3_min_distance, ("", ""), 0),
        ("P3 min_distance identical", p3_min_distance, ("abc", "abc"), 0),
        ("P3 min_distance swap", p3_min_distance, ("ab", "ba"), 2),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
