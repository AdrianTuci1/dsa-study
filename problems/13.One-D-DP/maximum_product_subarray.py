# Problem Statement
# Given an integer array, find the contiguous subarray (at least one number in it) that has the maximum product. Return this maximum product.

# Examples
# Input: [2,3,-2,4]
# Expected Output: 6
# Justification: The subarray [2,3] has the maximum product of 6.
# Input: [-2,0,-1]
# Expected Output: 0
# Justification: The subarray [0] has the maximum product of 0.

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        maxCurrent = minCurrent = maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxCurrent, minCurrent = minCurrent, maxCurrent
            maxCurrent = max(nums[i], maxCurrent * nums[i])
            minCurrent = min(nums[i], minCurrent * nums[i])
            maxProduct = max(maxProduct, maxCurrent)
        return maxProduct

sol = Solution()
print(sol.maxProduct([2,3,-2,4])) #6
print(sol.maxProdcut([-2,0,-1])) #0

