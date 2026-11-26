# Problem Description:

# Given the roots of two binary trees root and subRoot, return True if there is a subtree of root with the same structure and node values as subRoot, and False otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        
        return (
            tree1.val == tree2.val and
            self.isSameTree(tree1.left, tree2.left) and
            self.isSameTree(tree1.right, tree2.right)
        )

    

#root = [3,4,5,1,2]
#subRoot = [4,1,2]

# Example input
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Create an instance of the Solution class
solution = Solution()

# Test the isSubtree method
result = solution.isSubtree(root, subRoot)
print("Is subRoot a subtree of root?", result)
# Is subRoot a subtree of root? True