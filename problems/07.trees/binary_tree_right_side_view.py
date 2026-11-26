# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    if not root:
        return [] # if tree empty return empty list

    result = [] # initialize a list to store right side value
    queue = [root] # initialize a queue for level-order traversal with the root node

    while queue:
        # get the number of nodes at the current level
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)
        
            if i == level_size - 1:
                results.append(node.val)
            
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
    return result


# Example 1: 

# Construct the tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)
print(rightSideView(root1))
# [1, 3, 4]
