# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 
#  of the actual answer will be accepted.
# Constraints:

#  <= num <= 
# There will be at least one element in the data structure before calling findMedian.
# At most 
#  calls will be made to addNum and findMedian.
# Follow-up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# Probelm Explanation:
# The problem, "Find Median from Data Stream," deals with efficiently computing the median of a sequence of numbers as they are incrementally provided. The median is the middle value in an ordered list of numbers. When the list has an even number of elements, the median is the average of the two middle values.

# Here's a breakdown of the problem:

# Initialization: You are asked to implement a MedianFinder class that supports the following operations:

# MedianFinder(): Initializes the MedianFinder object.
# addNum(int num): Adds an integer num from the data stream to the data structure.
# findMedian(): Returns the median of all elements added to the data structure.
# Median Calculation: The findMedian operation should efficiently compute the median, and the result should have a precision of at least 
#  (i.e., answers within this range will be considered correct).

# Examples:

# If you add numbers [1, 2], the median should be 1.5 because (1 + 2) / 2 = 1.5.
# If you add numbers [1, 2, 3], the median should be 2 because it's the middle value.
# Constraints:

# The integers provided in the data stream are in the range from 
#  to 
# .
# There will be at least one element in the data structure before calling findMedian.
# At most, 
#  calls will be made to addNum and findMedian.
# The problem can be solved by using two priority queues (heaps): one max-heap to store the smaller half of the numbers and one min-heap to store the larger half of the numbers. The max-heap ensures that the largest number in the smaller half is at the top, and the min-heap ensures that the smallest number in the larger half is at the top. These heaps are balanced to efficiently find the median when requested.

import heapq

class MedianFinder():
    # initialize two heaps
    def __init__(self):
        self.small_half = [] #max-heap for the smaller half of the numbers
        self.large_half = [] #min-heap for the larger half of the numbers

    def addNum(self, num:int) -> None:
        #add the number to the appropiate heap based on its value
        if not self.small_half or num <= -self.small_half[0]:
            #if the number is less than or equal to the current maximum in the smaller half,
            #add it to the smaller half (max-heap)
            heapq.heappush(self.small_half, -num)
        else:
            #otherwise, add it to the larger half (min-heap)
            heapq.heappush(self.large_half, num)

        #balance the heaps if necessary to ensure that size difference is at most 1
        if len(self.small_half) > len(self.large_half) + 1:
            #if the size of the smaller half is more than one grater than the size of the larger half
            #move the maximum from the smaller half to the larger half to balance them
            heapq.heappush(self.large_half, -heapq.heappop(self.small_half))
        elif len(self.large_half) > len(self.small_half) + 1:
            #if the size of the smaller half is more than one grater than the size of the larger half
            #move the maximum from the smaller half to the larger half to balance them
            heapq.heappush(self.small_half, -heapq.heappop(self.large_half))
        
        findMedian(self) -> float:
        if len(self.small_half) == len(self.large_half):
            return (-self.small_half[0] + self.large_half[0] / 2.0)
        else:
            return -self.small_half[0]



            
# Example 1: 

# Example usage:
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Output: 2.0
# 1.5
# 2