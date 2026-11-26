# Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

# Example 1:
# Input: arr = [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].


class Solution:
    def max_sub_array_of_size_k(self, k, arr):
        max_sum = 0
        window_sum = 0

        for i in range(len(arr) - k + 1):
            window_sum = 0
            for j in range(i, i+k):
                window_sum += arr[j]
            max_sum = max(max_sum, window_sum)
        return max_sum


def main():
    sol = Solution()
    print("Maximum sum of a subarray of size K:" + str(sol.max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))