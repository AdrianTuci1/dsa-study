# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def levelOrder(root):
    if not root:
        return []
    
    result = []

    queue = [root]

    while queue:
        level_values = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_values)

    return result


# Example 1: 

# Construct the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = levelOrder(root)
print(result)
# [[3], [9, 20], [15, 7]]