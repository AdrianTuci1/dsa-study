# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Constraints:

# The number of nodes in the tree is in the range 
# .
# -1000 <= Node.val <= 1000
# Probelm Explanation:
# TThe problem is to design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a data structure or object into a sequence of characters or bytes so that it can be easily stored in a file, transmitted over a network, or otherwise persisted. Deserialization is the reverse process of converting the serialized data back into the original data structure.

# In the context of this problem:

# Serialization: You are given a binary tree, and your task is to convert it into a string representation such that you can later recreate the same binary tree from this string. The format of serialization is flexible, but it should allow you to reconstruct the original binary tree accurately.

# Deserialization: Given a serialized string, you need to reconstruct the binary tree it represents, ensuring that it is identical to the original tree.

# Here are some key points to consider in solving this problem:

# The input can include any valid binary tree, including trees with nodes having integer values within the range [-1000, 1000].
# You don't necessarily need to follow a specific format for serialization, but it should be designed in a way that allows unambiguous deserialization.
# The goal is to serialize the tree structure and its values and then deserialize it back into the same structure and values.
# A common approach for serialization is to use a traversal method like preorder traversal, where you visit nodes in the order: root, left subtree, right subtree. This way, you can serialize the tree into a string, and during deserialization, you can reconstruct the tree by parsing the string in the same order.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Codec:
    def serialize(self, root):
        serialized = []

        def dfs(node):
            if not node:
                serialized.append("Null")
                return
            serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(serialized)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "Null":
                self.i += 1
                return None
            node = TreeNode(int(vals(self.i)))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()



# Example 1: 

# Example usage:
# Serialize a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized_tree = codec.serialize(root)
print(serialized_tree)

# Deserialize the serialized tree
new_root = codec.deserialize(serialized_tree)
# 1,2,Null,Null,3,4,Null,Null,5,Null,Null