
# Problem Statement
# Given an array of integers nums and an integer target, return two distinct indices i and j such that the sum of nums[i] and nums[j] is equal to the target.

# You can assume that each input will have exactly one solution, and you may not use the same element twice.

# Examples
# Example 1:

# Input: nums = [3, 2, 4], target = 6
# Expected Output: [1, 2]
# Justification: nums[1] + nums[2] gives 2 + 4 which equals 6.
# Example 2:

# Input: nums = [-1, -2, -3, -4, -5], target = -8
# Expected Output: [2, 4]
# Justification: nums[2] + nums[4] yields -3 + (-5) which equals -8.
# Example 3:

# Input: nums = [10, 15, 21, 25, 30], target = 45
# Expected Output: [1, 4]
# Justification: nums[1] + nums[4] gives 15 + 30 which equals 45.
# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
# Solution
# To solve this problem, we use a hash map to efficiently track the numbers we've seen and their indices as we iterate through the array. This allows us to quickly check if the complement of the current number (i.e., the number that, when added to the current number, equals the target) has already been encountered. By leveraging the hash map, we can achieve constant time lookups and avoid the need for nested loops, thus reducing the time complexity to .

# Step-by-Step Algorithm
# Initialization:
# We create a hash map (numIndices) to store numbers as keys and their corresponding indices as values.
# Iterate Through the Array:
# For each number in the array, calculate its complement, which is the difference between the target and the current number (complement = target - nums[i]).
# Check for Complement:
# If the complement exists in the hash map, it means we have previously encountered a number that, when added to the current number, equals the target. In this case, we return the indices of these two numbers.
# Update the Map:
# If the complement is not found in the hash map, we add the current number and its index to the map.
# Algorithm Walkthrough
# Let's consider the Input: nums = [3, 2, 4], target = 6

# Initialize the hash map:

# numIndices = {}
# Iterate through the array:

# Iteration 1 (i = 0):
# Current number: nums[0] = 3
# Calculate complement: complement = 6 - 3 = 3
# Check if 3 exists in numIndices: No
# Add 3 and its index to numIndices: numIndices = {3: 0}
# Iteration 2 (i = 1):
# Current number: nums[1] = 2
# Calculate complement: complement = 6 - 2 = 4
# Check if 4 exists in numIndices: No
# Add 2 and its index to numIndices: numIndices = {3: 0, 2: 1}
# Iteration 3 (i = 2):
# Current number: nums[2] = 4
# Calculate complement: complement = 6 - 4 = 2
# Check if 2 exists in numIndices: Yes, at index 1
# Return indices: [1, 2]
# Thus, the pair of indices that add up to the target 6 are [1, 2].





class Solution:
    def twoSum(self, nums, target):
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i


solution = Solution()

print("Output:", solution.twoSum([3,2,4],6))