# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
    count = {}

    frequency = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items():
        frequency[c].append(n)

    res = []

    for i in range(len(frquency) - 1, 0, -1)
        for n in frequency[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [1,1,1,2,2,3]
k = 2
result1 = topKFrequent(nums, k)
print(result1)

# [1, 2]

