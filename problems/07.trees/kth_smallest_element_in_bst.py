# Given the root of a binary search tree, and an integer k, return the k th 
#  smallest value (1-indexed) of all the values of the nodes in the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def kthSmallest(root, k)
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
    
        k -= 1
        if k == 0
            return root.val
        root = root.right


# Example 1: 

# Example usage:
# Create the tree for the first example: root = [3,1,4,null,2], k = 1
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)
k1 = 1
print(kthSmallest(root1, k1)) 
# 1
