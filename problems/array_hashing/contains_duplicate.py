# 217. Contains Duplicate
# Difficulty: Easy

# Link to Problem: To see the Contains Duplicate problem on LeetCode, click here!

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicate(nums):
    unique_elements = set()
    for num in nums:
        if num in unique_elements:
            return True
        else:
            unique_elements.add(num)
    return False


nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))

