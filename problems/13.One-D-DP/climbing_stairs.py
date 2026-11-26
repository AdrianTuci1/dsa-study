# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n:int) -> int:
        if n <= 2:
            return n
        
        #create an array to store the number of ways to reach each step
        dp = [0] * (n + 1)

        #there is one way to reach first step
        dp[1] = 1

        #there are two ways to reach the second step
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Example 1:
n = 2
solution = Solution()
print(f"Example 1 - Input: n = {n}, Output: {solution.climbStairs(n)}")  
# Output should be 2