"""
UNION FIND / DSU — funcții (fără OOP)

Cea mai „funcțională" structură: nu ai nevoie de clasă deloc, doar de un array
`parent` (și unul `rank`) pe care le pasezi funcțiilor. Așa se scrie și în
competitive programming.

    make_set(n)            -> fiecare nod e singur în grupa lui
    find(parent, x)        -> rădăcina grupei lui x (cu path compression)
    union(parent, rank, a, b) -> unește grupele; False dacă erau deja unite
    connected(parent, a, b)   -> sunt în aceeași grupă?

Complexitate: aproape O(1) amortizat per operație.
"""


def make_set(n):
    return list(range(n))


def find(parent, x):
    """Rădăcina lui x, cu path compression (aplatizează drumul)."""
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, rank, a, b):
    """Unește grupele lui a și b. False dacă erau deja în aceeași grupă."""
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True


def connected(parent, a, b):
    return find(parent, a) == find(parent, b)


def count_components(parent):
    """Câte grupe (componente conexe) există."""
    return len({find(parent, i) for i in range(len(parent))})


def has_cycle(n, edges):
    """Ciclu într-un graf NEORIENTAT: o muchie între două noduri deja unite. O(E·α)."""
    parent, rank = make_set(n), [0] * n
    for u, v in edges:
        if not union(parent, rank, u, v):
            return True
    return False


if __name__ == "__main__":
    parent, rank = make_set(5), [0] * 5
    union(parent, rank, 0, 1)
    union(parent, rank, 1, 2)
    print("connected(0, 2):", connected(parent, 0, 2))    # True
    print("connected(0, 3):", connected(parent, 0, 3))    # False
    print("componente     :", count_components(parent))   # 3

    print("has_cycle(3, [(0,1),(1,2),(2,0)]):", has_cycle(3, [(0, 1), (1, 2), (2, 0)]))  # True
    print("has_cycle(3, [(0,1),(1,2)])       :", has_cycle(3, [(0, 1), (1, 2)]))          # False
