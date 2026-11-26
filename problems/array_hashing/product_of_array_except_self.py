# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    n = len(nums)

    left_products = [1] * n
    right_products = [1] * n

    left_product = 1
    for i in range(n):
        left_products[i] = left_product
        left_product *= nums[i]
    
    right_product = 1
    for i in range(n -1, -1, -1):
        right_products[i] = right_product
        right_product *= nums[i]
    
    answer = [left_products[i] * right_products[i] for i in range(n)]

    return answer


nums = [1, 2, 3, 4]
result1 = productExceptSelf(nums)
print(result1)

# [24, 12, 8, 6]
