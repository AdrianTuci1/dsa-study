"""
TREE (binary tree / BST) — funcții (fără OOP)

Fără clasă de nod! Un arbore = un TUPLU (valoare, stânga, dreapta); gol = None.

    (1, (2, None, None), (3, None, None))

Arborele e imutabil — funcțiile întorc un arbore NOU (stil funcțional).
Traversările și operațiile BST sunt toate funcții care primesc rădăcina.

Complexități: traversări O(n); BST search/insert/delete O(log n) mediu.
"""

from collections import deque


def node(value, left=None, right=None):
    """Construiește un nod (tuplu)."""
    return (value, left, right)


def is_empty(t):
    return t is None


def value(t):
    return t[0]


# ---------- Traversări ----------

def preorder(t):
    if t is None:
        return []
    return [t[0]] + preorder(t[1]) + preorder(t[2])


def inorder(t):
    if t is None:
        return []
    return inorder(t[1]) + [t[0]] + inorder(t[2])


def postorder(t):
    if t is None:
        return []
    return postorder(t[1]) + postorder(t[2]) + [t[0]]


def level_order(t):
    """Nivel cu nivel (BFS). Returnează listă de niveluri."""
    if t is None:
        return []
    result, q = [], deque([t])
    while q:
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur[0])
            if cur[1] is not None:
                q.append(cur[1])
            if cur[2] is not None:
                q.append(cur[2])
        result.append(level)
    return result


def height(t):
    if t is None:
        return 0
    return 1 + max(height(t[1]), height(t[2]))


def count_nodes(t):
    if t is None:
        return 0
    return 1 + count_nodes(t[1]) + count_nodes(t[2])


# ---------- BST ----------

def insert(t, val):
    """Inserează și returnează arborele nou. O(log n) mediu."""
    if t is None:
        return (val, None, None)
    v, left, right = t
    if val < v:
        return (v, insert(left, val), right)
    if val > v:
        return (v, left, insert(right, val))
    return t                             # duplicat -> neschimbat


def search(t, val):
    while t is not None:
        if val == t[0]:
            return True
        t = t[1] if val < t[0] else t[2]
    return False


def delete(t, val):
    """Șterge un nod și returnează arborele nou."""
    if t is None:
        return None
    v, left, right = t
    if val < v:
        return (v, delete(left, val), right)
    if val > v:
        return (v, left, delete(right, val))
    # găsit
    if left is None:
        return right
    if right is None:
        return left
    # doi copii -> înlocuim cu minimul din dreapta
    succ = right
    while succ[1] is not None:
        succ = succ[1]
    return (succ[0], left, delete(right, succ[0]))


def is_bst(t, low=float("-inf"), high=float("inf")):
    if t is None:
        return True
    v = t[0]
    if not (low < v < high):
        return False
    return is_bst(t[1], low, v) and is_bst(t[2], v, high)


if __name__ == "__main__":
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    t = node(1, node(2, node(4), node(5)), node(3))
    print("preorder  :", preorder(t))        # [1, 2, 4, 5, 3]
    print("inorder   :", inorder(t))         # [4, 2, 5, 1, 3]
    print("postorder :", postorder(t))       # [4, 5, 2, 3, 1]
    print("level     :", level_order(t))     # [[1], [2, 3], [4, 5]]
    print("height    :", height(t))          # 3
    print("count     :", count_nodes(t))     # 5

    bst = None
    for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst = insert(bst, x)
    print("BST inorder:", inorder(bst))      # sortat
    print("search(6) ->", search(bst, 6))    # True
    print("is_bst    ->", is_bst(bst))       # True
    print("dupa delete(10):", inorder(delete(bst, 10)))
