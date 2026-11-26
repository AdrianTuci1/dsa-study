# Problem Statement
# Given an array of integers, return a new array where each element at index i of the new array is the product of all the numbers in the original array except the one at i. You must solve this problem without using division.

# Examples
# Input: [2, 3, 4, 5]
# Expected Output: [60, 40, 30, 24]
# Justification: For the first element: 3*4*5 = 60, for the second element: 2*4*5 = 40, for the third element: 2*3*5 = 30, and for the fourth element: 2*3*4 = 24.

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left, right, result = [1] * n, [1] * n, [1] * new

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result
    


sol = Solution()
print(sol.productExceptSelf([2, 3, 4, 5]))
print(sol.productExceptSelf([1, 1, 1, 1]))
print(sol.productExceptSelf([10, 20, 30, 40]))

