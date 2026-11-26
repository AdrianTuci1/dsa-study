# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    root_idx_inorder = inorder.index(root_val)

    root.left = buildTree(preorder[1:1 + root_indx_inorder], inorder[:root_idx_inorder])
    root.right = buildTree(preorder[1 + root_idx_inorder:], inorder[root_idx_inorder + 1:])

    return root

def treeToList(root):
    # Initialize an empty list to store the elements of the binary tree
    result = []
    
    # Initialize a queue for level-order traversal starting with the root
    queue = [root]

    while queue:
        # Pop the front node from the queue
        node = queue.pop(0)

        # If the node is not None (i.e., a valid node), add its value to the result list
        if node:
            result.append(node.val)
            
            # Add the left and right children of the node to the queue
            queue.append(node.left)
            queue.append(node.right)
        else:
            # If the node is None, add None to the result to represent an empty node
            result.append(None)

    # Remove any trailing None values from the result list
    while result and result[-1] is None:
        result.pop()

    # Return the resulting list representing the binary tree elements
    return result


# Example 1: 

# Example usage:
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
# result = buildTree(preorder, inorder)

# print(treeToList(result))
# [3, 9, 20, None, None, 15, 7]