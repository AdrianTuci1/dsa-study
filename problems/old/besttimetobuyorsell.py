class Solution:
    def maxProfit(self, prices):
        minPrice, maxProfit = float('inf'), 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit


solution = Solution()
example1 = [3, 2, 6, 5, 0, 3]
example2 = [8, 6, 5, 2, 1]
example3 = [1, 2]
print(solution.maxProfit(example1))  # Output: 4
print(solution.maxProfit(example2))  # Output: 0
print(solution.maxProfit(example3))  # Output: 1