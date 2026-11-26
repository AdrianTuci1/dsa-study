# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        def max_path_sum_helper(node):
            if not node:
                return 0
            
            left_max = max(0, max_path_sum_helper(node.left))
            right_max = max(0, max_path_sum_helper(node.right))

            self.max_sum = max(self.max_sum, left_max + right_max + node.val)

            return max(left_max, right_max) + node.val

        
        self.max_sum = float('-inf')
        max_path_sum_helper(root)
        return self.max_sum


# Example 1: 

# Example usage:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
solution = Solution()
print(solution.maxPathSum(root1))
# 6

