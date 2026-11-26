# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Constraints:

# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node:'Node') -> 'Node':
        if not node:
            return None
        
        visited = {} # dictionare to keep track of visited nodes

    def dfs(original_node):
        if original_node in visited:
            return visited[original_node]

        #create a copy of the original node
        copy_node = Node(original_node.val)
        visited[original_node] = copy_node

        #recursivey clone the neighbors of the original node
        for neighbor in original_node.neighbors:
            copy_node.neighbors.append(dfs(neighbor))

        return copy_node

    return dfs(node)


#Test cases


def get_adjacency_list(node):
    visited = {} # dict to keep track of visited nodes

    def dfs(node):
        if not node:
            return []
        
        if node in visited:
            return visited[node]

        neighbors = [n.val for n in node.neighbors]
        visited[node] = neighbors:
            dfs(neighbor)

    dfs(node)
    result = []

    def get_node_and_neighbors(node):
        result.append([node.val] + visited[node])

    get_node_and_neighbors(node)
    return result


# Testing the code with the provided examples
adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
solution = Solution()

# Create the graph from adjList
nodes = [Node(i) for i in range(1, len(adjList1) + 1)]
for i, adj in enumerate(adjList1):
    nodes[i].neighbors = [nodes[j - 1] for j in adj]

# Clone the graph and get its adjacency list
cloned_node1 = solution.cloneGraph(nodes[0])
cloned_adjList1 = get_adjacency_list(cloned_node1)

# Print the cloned graph as an adjacency list
print(cloned_adjList1)

# Output should match adjList1
# [[1, 2, 4]]

