# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0

        #iterate through the houses
        for n in nums:
            temp = max(n + prev, curr)

            prev, curr = curr, temp
        
        return curr


# Example 1:
sol = Solution()

nums1 = [1, 2, 3, 1]
print(sol.rob(nums1))  
# Output: 4