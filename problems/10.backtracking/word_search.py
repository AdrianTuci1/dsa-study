# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Probelm Explanation:
# The problem is to determine whether a given word can be constructed from characters in an m x n grid of characters. The word can be formed by moving sequentially through horizontally or vertically neighboring cells in the grid, and you cannot use the same cell more than once.

# Here are the specifics of the problem:

# You are given an m x n grid, which is a 2D board of characters.
# You are also given a string word consisting of lowercase and uppercase English letters.
# Your task is to determine if the word can be found in the grid by moving from one cell to an adjacent cell (horizontally or vertically) and collecting the characters sequentially to form the word.
# You can't use the same cell more than once when forming the word.
# If it's possible to form the word in the grid, return True; otherwise, return False.
# For example, consider the following grid and word:

# board = [["A", "B", "C", "E"],
#          ["S", "F", "C", "S"],
#          ["A", "D", "E", "E"]]         
# word = "ABCCED"
# In this case, the word "ABCCED" can be formed by moving through the cells (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,3) in the grid. Therefore, the function should return True.

# Conversely, if the word is impossible to construct, such as in the case of the word "ABCB" for the same grid, where there's no valid path that forms the word, the function should return False.

# The problem involves searching for a path through the grid that matches the characters in the word while respecting the constraints mentioned. It can be solved using depth-first search (DFS) or backtracking.


from typing import List

class Solution:
    def exist(self, board:List[List[str]], word:str) -> bool:
        def dfs(i, j, k):
            #check if the current position is out of bounds or doesn't match the character in the word
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i] != word[k]:
                return False
            
            # if we have matched all characters in the word, return True
            if k == len(word) - 1:
                return True
            
            # temporarily mark the current cell to prevent revisiting.
            tmp, board[i][j] = board[i][j], "/"

            #explore adjacent cells by making reucrsive calls in all four directions
            found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, j + 1)

            board[i][j] = tmp

            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False



# Example 1: 

# Create an instance of the Solution class
solution = Solution()

# Test case 1: Word "ABCCED" can be found in the grid
board1 = [["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]]
word1 = "ABCCED"
print(solution.exist(board1, word1))  # Expected output: True
# True
# Example 2

# Test case 2: Word "SEE" can be found in the grid
word2 = "SEE"
print(solution.exist(board1, word2))  # Expected output: True
# True