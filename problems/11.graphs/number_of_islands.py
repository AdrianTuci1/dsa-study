#200

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List

class Solution:
    def numIslands(self, grid:List[List[str]]) -> int:
        if not grid:
            return 0

    m, n = len(grid), len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
            return
        
        grid[row][col] = '0' #mark th current cell as visited
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)] #define four posible dir to move

        for dr, dc in directions:
            #explore adjacent cells
            dfs(row + dr, col + dc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands

grid1 = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
]

solution = Solution()
result1 = solution.numIslands(grid1)
print("Example 1 Output:", result1)  # Expected output: 1
# Example 1 Output: 1
