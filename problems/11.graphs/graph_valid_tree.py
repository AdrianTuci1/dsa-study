# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Constraints:

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    
    adj_list ={i: [0] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)

        for neighbor in adj_list[node]:
            if neighbor != parent:
                if not dfs(neighbor, node):
                    return False
        
        return True

    if not dfs(0, -1):
        return False
    
    return len(visited) == n

# Example 1
n1 = 5
edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(validTree(n1, edges1))  # Output: true
# True
