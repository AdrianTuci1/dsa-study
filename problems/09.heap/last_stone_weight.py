import heapq




def lastStoneWeight(stones):
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        y = -heapq.heappop(max_heap)
        x = -heapq.heappop(max_heap)

        if x != y:
            new_stone = y - x
            heapq.heappush(max_heap, -new_stone)

    if max_heap:
        return -max_heap[0]
    else:
        return 0


stones = [4, 4, 2, 3, 2]
print(lastStoneWeight(stones))