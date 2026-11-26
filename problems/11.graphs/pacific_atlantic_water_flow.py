# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]
        #check if input matrix is empty
        if not heights:
            return []

        m, n = len(heights), len(heights[0])

        #initialize boolean matrices to keep track of the ceels reachable from each ocean
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        #dfs function to mark cells that can be reached from an ocean
        def dfs(x, y, reachable):
            if reachable[x][y]:
                return
            rechable[x][y] = True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and heights[new_x][new_y] >= heights[x][y]:
                    dfs(new_x, new_y, reachable)

        #start DFS from the Pacific Ocean (left and top edges)
        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n - 1, atlantic_reachable)
        
        for j in range(n):
            dfs(0, j, pacific_reachable)
            dfs(m - 1, j, atlantic_reachable)
        
        result = []

        #find cells that can flow to both the Pacific and Atlantic ocenas
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result



# Example 1
heights1 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

solution = Solution()
print(solution.pacificAtlantic(heights1)) 
# Expected Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]