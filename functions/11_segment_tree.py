"""
SEGMENT TREE — funcții (fără OOP)

Un segment tree e doar o LISTĂ de `4*n` noduri (indexate de la 1) plus `n`.
Nu ai nevoie de clasă: pasezi `(tree, n)` funcțiilor.

    nod i -> copii 2*i și 2*i+1, rădăcina 1
    nodul i ține suma intervalului [lo, hi] al array-ului original

Complexități: build O(n), update O(log n), query O(log n).
Pentru SUMĂ e mai scurt cu Fenwick, dar segment tree-ul e general
(min/max/gcd, lazy propagation, range update).
"""


def _build(tree, node, lo, hi, nums):
    if lo == hi:                       # frunză = un singur element
        tree[node] = nums[lo]
        return
    mid = (lo + hi) // 2
    _build(tree, 2 * node, lo, mid, nums)
    _build(tree, 2 * node + 1, mid + 1, hi, nums)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def seg_build(nums):
    """Construiește arborele. Returnează `(tree, n)`, cu `tree` indexat de la 1."""
    n = len(nums)
    tree = [0] * (4 * n) if n else []
    if n:
        _build(tree, 1, 0, n - 1, nums)
    return tree, n


def _update(tree, node, lo, hi, i, value):
    if lo == hi:
        tree[node] = value
        return
    mid = (lo + hi) // 2
    if i <= mid:
        _update(tree, 2 * node, lo, mid, i, value)
    else:
        _update(tree, 2 * node + 1, mid + 1, hi, i, value)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def seg_update(tree, n, index, value):
    """Setează nums[index] = value."""
    _update(tree, 1, 0, n - 1, index, value)


def _query(tree, node, lo, hi, left, right):
    if right < lo or hi < left:                     # interval disjunct
        return 0
    if left <= lo and hi <= right:                  # interval complet acoperit
        return tree[node]
    mid = (lo + hi) // 2
    return (_query(tree, 2 * node, lo, mid, left, right)
            + _query(tree, 2 * node + 1, mid + 1, hi, left, right))


def seg_query(tree, n, left, right):
    """Suma nums[left..right] (ambele capete incluse)."""
    return _query(tree, 1, 0, n - 1, left, right)


if __name__ == "__main__":
    tree, n = seg_build([1, 3, 5, 7, 9, 11])
    print("query(1, 3) ->", seg_query(tree, n, 1, 3))    # 15 (3+5+7)
    print("query(0, 5) ->", seg_query(tree, n, 0, 5))    # 36 (tot)

    seg_update(tree, n, 1, 10)                           # nums[1] = 10
    print("dupa update(1, 10)")
    print("query(1, 3) ->", seg_query(tree, n, 1, 3))    # 22 (10+5+7)
    print("query(1, 1) ->", seg_query(tree, n, 1, 1))    # 10

    tree2, n2 = seg_build([4, -1, 0, 6, 2])
    seg_update(tree2, n2, 2, 100)
    print("query(0, 2) ->", seg_query(tree2, n2, 0, 2))  # 103 (4-1+100)
