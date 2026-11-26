"""
STRUCTURA: FENWICK TREE (Binary Indexed Tree / BIT)

Ce este:
    Un array de prefixe „cu superputeri": `tree[i]` ține suma unei porțiuni de
    lungime `i & (-i)` care se termină pe poziția i. Nu e un arbore explicit —
    structura „copiilor" e dată de biții celui mai puțin semnificativ.

Operații și complexitate:
    build(nums)              O(n)
    add(index, delta)        O(log n)
    prefix_sum(index)        O(log n)
    range_sum(left, right)   O(log n)

Indexare: intern 1-based (`tree` are n+1 poziții, `tree[0]` e umplutură),
iar API-ul de aici e 0-based, ca `nums`.

Ideea-cheie:
    `i & (-i)` izolează ultimul bit de 1 → sari din prefix în prefix logaritmic.
    La add urci cu `i += i & (-i)`, la prefix_sum cobori cu `i -= i & (-i)`.
    Mult mai puțin cod decât segment tree-ul, dar doar pentru operații
    INVERSABILE (sumă, xor) — nu merge la min/max.
"""


class Fenwick:
    """BIT pentru sumă pe interval, cu update pe poziție (adunare)."""

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] + list(nums)        # 1-based, copiem valorile
        for i in range(1, self.n + 1):      # build O(n), nu n * O(log n)
            j = i + (i & -i)
            if j <= self.n:
                self.tree[j] += self.tree[i]

    def add(self, index, delta):
        """nums[index] += delta."""
        i = index + 1                       # API 0-based -> intern 1-based
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, index):
        """Suma nums[0..index] (ambele capete incluse)."""
        i = index + 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_sum(self, left, right):
        """Suma nums[left..right] (ambele capete incluse)."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def __repr__(self):
        return f"Fenwick(n={self.n}, tree={self.tree})"


if __name__ == "__main__":
    fw = Fenwick([1, 2, 3, 4, 5])
    print("prefix_sum(4) ->", fw.prefix_sum(4))      # 15 (tot)
    print("prefix_sum(0) ->", fw.prefix_sum(0))      # 1
    print("range_sum(1, 3) ->", fw.range_sum(1, 3))  # 9 (2+3+4)

    fw.add(1, 10)                                    # nums[1] = 12
    print("dupa add(1, 10)")
    print("prefix_sum(4) ->", fw.prefix_sum(4))      # 25
    print("range_sum(1, 3) ->", fw.range_sum(1, 3))  # 19 (12+3+4)
    print("range_sum(0, 0) ->", fw.range_sum(0, 0))  # 1

    fw.add(0, -1)
    print("dupa add(0, -1)")
    print("range_sum(0, 4) ->", fw.range_sum(0, 4))  # 24 (0+12+3+4+5)
