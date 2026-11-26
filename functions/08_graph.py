"""
GRAPH — funcții (fără OOP)

Reprezentare: adjacency list = { nod: [vecini] }. Funcțiile primesc `adj` (sau
lista de muchii) ca argument — fără clasă.

Complexități: BFS/DFS O(V + E); topo sort O(V + E).
"""

from collections import deque


def build_graph(edges, directed=False):
    """Construiește adjacency list din lista de muchii. Toate nodurile devin chei."""
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, [])
        if not directed:
            adj[v].append(u)
    return adj


def bfs(adj, start):
    """Parcurgere în lățime — cel mai scurt drum în graf neponderat. O(V+E)."""
    visited = {start}
    order = []
    q = deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in adj.get(node, []):
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return order


def dfs(adj, start):
    """Parcurgere în adâncime, iterativ cu stivă. O(V+E)."""
    visited, order, stack = set(), [], [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nxt in reversed(adj.get(node, [])):
            if nxt not in visited:
                stack.append(nxt)
    return order


def dfs_recursive(adj, node, visited=None):
    """Varianta recursivă (mai naturală, dar poate depăși stiva pe grafuri mari)."""
    if visited is None:
        visited = set()
    visited.add(node)
    order = [node]
    for nxt in adj.get(node, []):
        if nxt not in visited:
            order += dfs_recursive(adj, nxt, visited)
    return order


def shortest_path(adj, start, target):
    """Numărul minim de muchii start -> target (BFS). -1 dacă nu există."""
    q = deque([(start, 0)])
    visited = {start}
    while q:
        node, dist = q.popleft()
        if node == target:
            return dist
        for nxt in adj.get(node, []):
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, dist + 1))
    return -1


def connected_components(adj):
    """Numărul de componente conexe (graf neorientat). O(V+E)."""
    seen, count = set(), 0
    for node in adj:
        if node not in seen:
            count += 1
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur in seen:
                    continue
                seen.add(cur)
                stack.extend(adj[cur])
    return count


def has_cycle_undirected(adj):
    """Detectează ciclu într-un graf neorientat (DFS cu părinte)."""
    seen = set()

    def dfs(node, parent):
        seen.add(node)
        for nxt in adj[node]:
            if nxt not in seen:
                if dfs(nxt, node):
                    return True
            elif nxt != parent:
                return True
        return False

    for node in adj:
        if node not in seen:
            if dfs(node, None):
                return True
    return False


def topological_sort(nodes, edges):
    """Ordonare topologică (Kahn) pentru graf orientat aciclic. O(V+E).

    Returnează [] dacă există ciclu.
    """
    adj = {n: [] for n in nodes}
    indegree = {n: 0 for n in nodes}
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    q = deque([n for n in nodes if indegree[n] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return order if len(order) == len(nodes) else []


if __name__ == "__main__":
    adj = build_graph([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("E", "F")])
    print("BFS de la A:", bfs(adj, "A"))
    print("DFS de la A:", dfs(adj, "A"))
    print("DFS recursiv:", dfs_recursive(adj, "A"))
    print("drum A->D  :", shortest_path(adj, "A", "D"))
    print("componente :", connected_components(adj))     # 2
    print("are ciclu? :", has_cycle_undirected(adj))      # True

    nodes = ["A", "B", "C", "D"]
    edges = [("C", "A"), ("C", "B"), ("A", "D"), ("B", "D")]
    print("topo sort  :", topological_sort(nodes, edges))  # C inainte, D ultimul
