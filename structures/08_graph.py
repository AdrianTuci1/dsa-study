"""
STRUCTURA: GRAPH (graf)

Ce este:
    Un set de noduri (vertices) și muchii (edges) între ele. Reprezentarea cea mai
    folosită: ADJACENCY LIST = { nod: [vecini] }.

Tipuri:
    - neorientat: muchia u-v merge în ambele sensuri
    - orientat (directed): muchia u->v merge doar de la u la v
    - ponderat: muchiile au cost (aici folosim neponderat, cu cost 1)

Complexitate parcurgere: O(V + E), unde V = noduri, E = muchii.

Ideea-cheie:
    BFS (coadă)  -> cel mai scurt drum în graf NEPONDERAT, explorare nivel cu nivel.
    DFS (recursie/stivă) -> explorare în adâncime, componente conexe, cicluri, topo sort.

    Întotdeauna ține un `visited` ca să nu te întorci în cerc.
"""

from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def nodes(self):
        return list(self.adj.keys())

    def bfs(self, start):
        """Parcurgere în lățime. O(V + E). Returnează ordinea vizitării."""
        visited = {start}
        order = []
        q = deque([start])
        while q:
            node = q.popleft()
            order.append(node)
            for nxt in self.adj[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return order

    def dfs(self, start):
        """Parcurgere în adâncime (iterativ, cu stivă). O(V + E)."""
        visited, order, stack = set(), [], [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for nxt in reversed(self.adj[node]):
                if nxt not in visited:
                    stack.append(nxt)
        return order

    def shortest_path(self, start, target):
        """Cel mai scurt drum (număr de muchii) cu BFS. -1 dacă nu există."""
        q = deque([(start, 0)])
        visited = {start}
        while q:
            node, dist = q.popleft()
            if node == target:
                return dist
            for nxt in self.adj[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, dist + 1))
        return -1

    def connected_components(self):
        """Număr de componente conexe (pentru graf neorientat)."""
        seen, count = set(), 0
        for node in self.adj:
            if node not in seen:
                count += 1
                stack = [node]
                while stack:
                    cur = stack.pop()
                    if cur in seen:
                        continue
                    seen.add(cur)
                    stack.extend(self.adj[cur])
        return count

    def has_cycle_undirected(self):
        """Detectează ciclu într-un graf neorientat (DFS cu părinte)."""
        seen = set()

        def dfs(node, parent):
            seen.add(node)
            for nxt in self.adj[node]:
                if nxt not in seen:
                    if dfs(nxt, node):
                        return True
                elif nxt != parent:
                    return True
            return False

        for node in self.adj:
            if node not in seen:
                if dfs(node, None):
                    return True
        return False

    def topological_sort(self):
        """Ordonare topologică (Kahn) pentru graf ORIENTAT aciclic. O(V + E).

        Returnează [] dacă există ciclu (nu se poate ordona).
        """
        nodes = set(self.adj)
        for u in self.adj:
            nodes.update(self.adj[u])
        indegree = {node: 0 for node in nodes}
        for u in self.adj:
            for nxt in self.adj[u]:
                indegree[nxt] += 1
        q = deque([n for n in nodes if indegree[n] == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nxt in self.adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == len(nodes) else []


if __name__ == "__main__":
    g = Graph(directed=False)
    for u, v in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("E", "F")]:
        g.add_edge(u, v)
    print("BFS de la A:", g.bfs("A"))
    print("DFS de la A:", g.dfs("A"))
    print("drum A->D  :", g.shortest_path("A", "D"))
    print("componente :", g.connected_components())     # 2
    print("are ciclu? :", g.has_cycle_undirected())      # True (A-B-D-C-A)

    dag = Graph(directed=True)
    for u, v in [("C", "A"), ("C", "B"), ("A", "D"), ("B", "D")]:
        dag.add_edge(u, v)
    print("topo sort  :", dag.topological_sort())        # C inaintea A,B; A,B inaintea D
