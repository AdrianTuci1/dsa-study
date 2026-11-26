# In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# You need to return the number of connected components in that graph.

def countConnectedComponents(n, edges):
    #def a helper function for depth-first search
    def dfs(node):
        if not visited[node]: #if a node has not been visited yet
            visited[node] = True # mark it as visited
            for neighbor in graph[node]: #explore all neighbors in current node
                dfs(neighbor)

    #create an empty adjacency list to represent the graph
    graph = [[] for _ in range(n)]

    #initialize a boolean list to keep track of visited nodes
    visited = [False] * n

    #populate the adjancecy list with edges from the input
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    #initialize a counter to keep track of the number of connected components
    count = 0

    #iterate through all nodes in the graph
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)

    return count

# Example 1
n1 = 3
edges1 = [[0, 1], [0, 2]]
print(countConnectedComponents(n1, edges1))  # Output: 1
# 1


