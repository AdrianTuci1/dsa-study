# You have a robot positioned on a grid with m rows and n columns. The robot starts at the top-left corner of the grid (position [0][0]) and wants to reach the bottom-right corner (position [m-1][n-1]).

# The robot has movement restrictions - it can only move in two directions:

# Right (to the next column)
# Down (to the next row)
# Your task is to find the total number of unique paths the robot can take to reach from the starting position to the destination.

# For example, on a 3×3 grid, the robot needs to make exactly 2 moves right and 2 moves down to reach the destination. The different orderings of these moves create different paths, such as:

# Right → Right → Down → Down
# Right → Down → Right → Down
# Down → Down → Right → Right
# And so on...
# Given integers m (number of rows) and n (number of columns), return the count of all possible unique paths from [0][0] to [m-1][n-1].

# The answer is guaranteed to be at most 2 × 10^9.


class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row > 0:
                    dp[row][col] += dp[row - 1][col]

                if col > 0:
                    dp[row][col] += dp[row][col - 1]
        
        return dp[m - 1][n - 1]

sol = Solution()
print(sol.uniquePaths(14, 14))

