# Given an m x n board of characters and a list of strings words, the task is to return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 x 10(4)
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# Probelm Explanation:
# To solve the "Word Search II" problem, you can use a Trie data structure and perform a depth-first search (DFS) on the board. Here's a step-by-step approach to solve the problem:

# Build a Trie from the given list of words:

# Create a Trie data structure to store all the words from the input list.
# For each word in the input list, insert it into the Trie, character by character. Make sure to mark the end of each word in the Trie.
# Perform DFS on the board:

# Iterate through each cell (i, j) on the board.
# For each cell, start a DFS traversal from that cell to search for words.
# During the DFS traversal, maintain a current path string.
# At each cell, check if the current path string, concatenated with the character in the cell, matches any word prefix in the Trie. If it does, continue the DFS.
# If the current path string matches a word in the Trie, add it to the result.
# Implement DFS with backtracking:

# During the DFS traversal, you will explore neighboring cells (horizontally and vertically) if they are within bounds and haven't been visited before.
# To prevent revisiting the same cell within the same word, mark the cell as visited (e.g., change its character to a special character like '#') before exploring it and restore its original character after the DFS traversal.
# Return the result:

# After completing the DFS traversal for all cells on the board, you will have collected all the valid words in the result set.
# Convert the result set to a list and return it as the final output.
# This approach efficiently finds all words on the board by utilizing the Trie data structure to prune unnecessary DFS paths and avoiding duplicate visits to the same cell within the same word. It ensures that each word is constructed from letters of sequentially adjacent cells without using the same letter cell more than once in a word.


class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def findWords(board, words):
    #dfs function to search for words starting from given cell
    def dfs(node, i, j, path):
        char = board[i][j] # get the character at the current cell
        curr_node = node.children.get(char) # find the corresponding trie node

        if not curr_node:
            return # if no matching trie node, stop the search
        
        path += char # add a character to the current path

        if curr_node.is_end_of_word:
            result.add(path) # if path matches a word add to the result

        temp, board[i][j] = board[i][j], "#" # mark the cell as visited

        # explore neighboring cells(up, down, left, right)
        if i > 0:
            dfs(curr_node, i - 1, j, path)
        if i < m - 1:
            dfs(curr_node, i + 1, j, path)
        if j > 0:
            dfs(curr_node, i, j - 1, path)
        if j < n - 1:
            dfs(curr_node, i, j + 1, path)

        board[i][j] = temp # restore cell original char
    
    # build a trie from the list of words
    def buildTrie():
        root = TrieNode() # create root node
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode() # create new node if needed
                node = node.children[char]
            node.is_end_of_word = True # mark the end of the word
        return root

    
    m, n = len(board), len(board[0]) # get dim of the board
    root = buildTrie() # build the trie from the list of words
    result = set() # use a set to store unique words found on the board

    #iterate through each cell on the board and start dfs from there
    for i in range(m):
        for j in range(n):
            dfs(root, i, j, "") # start dfs from each cell on the board

    return list(result) # convert set to a list and return result




