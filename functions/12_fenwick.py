"""
FENWICK / BIT — funcții (fără OOP)

BIT-ul e doar o LISTĂ `tree` de lungime n+1 (1-based, `tree[0]` e umplutură).
Toate funcțiile primesc lista ca argument — fără clasă.

    tree[i] = suma unei porțiuni de lungime `i & (-i)` care se termină pe i
    add:         i += i & (-i)     (urci spre rădăcină)
    prefix_sum:  i -= i & (-i)     (cobori spre 0)

Indexare: intern 1-based, dar funcțiile de aici primesc indecși 0-based,
ca array-ul original. Complexități: build O(n), add/prefix_sum O(log n).
"""


def fenwick_build(nums):
    """Construiește BIT-ul în O(n): copiază valorile, apoi le propagă părinților."""
    n = len(nums)
    tree = [0] + list(nums)
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            tree[j] += tree[i]
    return tree


def fenwick_add(tree, index, delta):
    """nums[index] += delta."""
    n = len(tree) - 1
    i = index + 1                       # API 0-based -> intern 1-based
    while i <= n:
        tree[i] += delta
        i += i & -i


def fenwick_prefix_sum(tree, index):
    """Suma nums[0..index] (ambele capete incluse)."""
    i = index + 1
    total = 0
    while i > 0:
        total += tree[i]
        i -= i & -i
    return total


def fenwick_range_sum(tree, left, right):
    """Suma nums[left..right] (ambele capete incluse)."""
    return fenwick_prefix_sum(tree, right) - fenwick_prefix_sum(tree, left - 1)


if __name__ == "__main__":
    fw = fenwick_build([1, 2, 3, 4, 5])
    print("prefix_sum(4) ->", fenwick_prefix_sum(fw, 4))       # 15 (tot)
    print("prefix_sum(0) ->", fenwick_prefix_sum(fw, 0))       # 1
    print("range_sum(1, 3) ->", fenwick_range_sum(fw, 1, 3))   # 9 (2+3+4)

    fenwick_add(fw, 1, 10)                                     # nums[1] = 12
    print("dupa add(1, 10)")
    print("prefix_sum(4) ->", fenwick_prefix_sum(fw, 4))       # 25
    print("range_sum(1, 3) ->", fenwick_range_sum(fw, 1, 3))   # 19 (12+3+4)

    fenwick_add(fw, 0, -1)
    print("dupa add(0, -1)")
    print("range_sum(0, 4) ->", fenwick_range_sum(fw, 0, 4))   # 24 (0+12+3+4+5)
