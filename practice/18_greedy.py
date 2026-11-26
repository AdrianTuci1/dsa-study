"""
CONCEPT: Greedy

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/18_greedy.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Jump Game  (LeetCode 55)
#
# You are given an integer list `nums` where nums[i] is the maximum number of
# steps you can jump forward from index i. You start at index 0 and want to
# reach the last index. Return True if you can reach the last index, and
# False otherwise. An empty list is considered already at the goal.
#
# Example 1:
#   Input: nums = [2, 3, 1, 1, 4]
#   Output: True
# Example 2:
#   Input: nums = [3, 2, 1, 0, 4]
#   Output: False
#
# Constraints:
#   - 0 <= len(nums) <= 100
#   - 0 <= nums[i] <= 100
# ---------------------------------------------------------------------------
def p1_can_jump(nums):
    # `reach` = the furthest index reachable so far. Walking left to right,
    # if the current index is already past `reach`, nothing can reach it.
    reach = 0
    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)
    return True


# ---------------------------------------------------------------------------
# Problem 2 - Gas Station  (LeetCode 134)
#
# There are `len(gas)` gas stations along a circular route. gas[i] is the fuel
# available at station i, and cost[i] is the fuel needed to travel from station
# i to station i+1. You start with an empty tank at one station and move
# clockwise. Return the index of the starting station that lets you complete
# the circuit once, or -1 if no such station exists. The answer is guaranteed
# to be unique if it exists.
#
# Example 1:
#   Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
#   Output: 3
# Example 2:
#   Input: gas = [2, 3, 4], cost = [3, 4, 3]
#   Output: -1
#
# Constraints:
#   - 1 <= len(gas) == len(cost) <= 100
#   - 0 <= gas[i], cost[i] <= 100
# ---------------------------------------------------------------------------
def p2_can_complete_circuit(gas, cost):
    # A circuit is possible iff total gas >= total cost. If it is, the
    # station right after the last place where the tank went negative is the
    # unique valid start (everything before it must be compensated).
    if sum(gas) < sum(cost):
        return -1
    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start


# ---------------------------------------------------------------------------
# Problem 3 - Best Time to Buy and Sell Stock II  (LeetCode 122)
#
# You are given a list `prices` where prices[i] is the price of a stock on day
# i. You may buy and sell the stock many times (you must sell before buying
# again), and you may hold at most one share at a time. Return the maximum
# profit you can achieve. If no profit is possible, return 0.
#
# Example 1:
#   Input: prices = [7, 1, 5, 3, 6, 4]
#   Output: 7
# Example 2:
#   Input: prices = [1, 2, 3, 4, 5]
#   Output: 4
#
# Constraints:
#   - 0 <= len(prices) <= 1000
#   - 0 <= prices[i] <= 1000
# ---------------------------------------------------------------------------
def p3_max_profit(prices):
    # Unlimited transactions: collect every upward step. Selling before a
    # fall and buying back lower is always at least as good as holding.
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


if __name__ == "__main__":
    tests = [
        ("P1 can_jump", p1_can_jump, ([2, 3, 1, 1, 4],), True),
        ("P1 can_jump blocked", p1_can_jump, ([3, 2, 1, 0, 4],), False),
        ("P1 can_jump single zero", p1_can_jump, ([0],), True),
        ("P1 can_jump empty", p1_can_jump, ([],), True),
        ("P2 gas station", p2_can_complete_circuit, ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
        ("P2 gas station impossible", p2_can_complete_circuit, ([2, 3, 4], [3, 4, 3]), -1),
        ("P2 gas station single", p2_can_complete_circuit, ([5], [4]), 0),
        ("P3 max_profit", p3_max_profit, ([7, 1, 5, 3, 6, 4],), 7),
        ("P3 max_profit increasing", p3_max_profit, ([1, 2, 3, 4, 5],), 4),
        ("P3 max_profit decreasing", p3_max_profit, ([7, 6, 4, 3, 1],), 0),
        ("P3 max_profit single day", p3_max_profit, ([5],), 0),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
