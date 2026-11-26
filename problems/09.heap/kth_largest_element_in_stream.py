# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement the KthLargest class with the following methods:

# KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
# int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

import heapq
from typing import List

class KthLargest:
    def __init__(self, k:int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]


# Example 1: 

# Example usage:
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10)) # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8
# 4
# 5
# 5
# 8
# 8