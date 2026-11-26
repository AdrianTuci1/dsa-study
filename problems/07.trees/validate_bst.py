# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def is_vaild_BST(root):
    def is_valid(node, min_val, max_val):
        if node is None:
            return True

        if not (min_val < node.val < max_val):
            return False

        return (is_valid(node.left, min_val, node.val) and
                is_valid(node.right, node.val, max_val))

    
    return is_valid(root, float('-inf'), float('inf'))



# Example 1: 

# Example usage:
# Create the tree for the first example: [2, 1, 3]
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(is_valid_BST(root1))
# True
