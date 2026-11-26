"""
CONCEPT: Graph BFS / DFS (grids and adjacency)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/14_graph_bfs_dfs.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Number of Islands  (LeetCode 200)
#
# Given a 2D grid of characters "1" (land) and "0" (water), count the number
# of islands. An island is a maximal group of land cells connected
# horizontally or vertically (not diagonally). An empty grid has 0 islands.
#
# Example 1:
#   Input: grid = [["1", "1", "0"],
#                  ["0", "1", "0"],
#                  ["0", "0", "1"]]
#   Output: 2
# Example 2:
#   Input: grid = [["1", "0", "1"]]
#   Output: 2
#
# Constraints:
#   - 0 <= number of rows, columns <= 300
#   - grid[i][j] is either "0" or "1"
# ---------------------------------------------------------------------------
def p1_num_islands(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            seen.add((r, c))
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
    return islands
    


# ---------------------------------------------------------------------------
# Problem 2 - Shortest Path in an Unweighted Undirected Graph
#
# Nodes are numbered 0 .. n-1. `edges` is a list of undirected pairs [u, v].
# Return the number of edges on a shortest path from node 0 to node n-1, or
# -1 if node n-1 cannot be reached. If n == 1 the answer is 0.
#
# Example 1:
#   Input: n = 4, edges = [[0, 1], [1, 2], [2, 3]]
#   Output: 3
# Example 2:
#   Input: n = 4, edges = [[0, 1], [2, 3]]
#   Output: -1
#
# Constraints:
#   - 1 <= n <= 1000
#   - 0 <= len(edges) <= 5000
#   - Graph may be disconnected and may contain multiple edges
# ---------------------------------------------------------------------------
def p2_shortest_path(n, edges):
    if n == 1:
        return 0
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    dist = [-1] * n
    dist[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist[n - 1]



# ---------------------------------------------------------------------------
# Problem 3 - Max Area of Island  (LeetCode 695)
#
# Given the same kind of grid as Problem 1, return the area (number of land
# cells) of the largest island. Return 0 if there is no land at all.
#
# Example 1:
#   Input: grid = [["1", "1", "0"],
#                  ["1", "0", "0"],
#                  ["0", "0", "1"]]
#   Output: 3
# Example 2:
#   Input: grid = [["0"]]
#   Output: 0
#
# Constraints:
#   - 0 <= number of rows, columns <= 300
#   - grid[i][j] is either "0" or "1"
# ---------------------------------------------------------------------------
def p3_max_area_island(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    best = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] !="1" or (r, c) in seen:
                continue
            area = 0
            seen.add((r, c))
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                area += 1
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
                best = max(best, area)
    return best




if __name__ == "__main__":
    tests = [
        ("P1 num_islands", p1_num_islands,
         ([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]],), 2),
        ("P1 num_islands", p1_num_islands, ([],), 0),
        ("P1 num_islands", p1_num_islands, ([["1"]],), 1),
        ("P1 num_islands", p1_num_islands, ([["1", "0", "1"]],), 2),
        ("P1 num_islands", p1_num_islands, ([["0", "0"], ["0", "0"]],), 0),
        ("P2 shortest_path", p2_shortest_path, (4, [[0, 1], [1, 2], [2, 3]]), 3),
        ("P2 shortest_path", p2_shortest_path, (4, [[0, 1], [2, 3]]), -1),
        ("P2 shortest_path", p2_shortest_path, (1, []), 0),
        ("P2 shortest_path", p2_shortest_path, (5, [[0, 1], [0, 2], [1, 3], [3, 4]]), 3),
        ("P2 shortest_path", p2_shortest_path, (3, [[0, 2], [2, 1], [0, 1]]), 1),
        ("P3 max_area_island", p3_max_area_island,
         ([["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]],), 3),
        ("P3 max_area_island", p3_max_area_island, ([["0"]],), 0),
        ("P3 max_area_island", p3_max_area_island, ([["1", "1", "1"], ["1", "1", "1"]],), 6),
        ("P3 max_area_island", p3_max_area_island, ([["1", "0"], ["0", "1"]],), 1),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
