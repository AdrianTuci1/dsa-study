# You are given an array prices where prices[i] is the price of a given stock on the 
#  day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Example 1:
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))
# 5