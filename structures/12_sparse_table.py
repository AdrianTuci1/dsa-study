"""
STRUCTURA: SPARSE TABLE (tabel rar) — RMQ static

Ce este:
    Un tabel precalculat pentru „minim pe interval" când array-ul NU se
    modifică niciodată. `table[k][i]` = minimul din fereastra de lungime
    `2^k` care începe pe poziția i.

Operații și complexitate:
    build(nums)           O(n log n) timp, O(n log n) spațiu
    query(left, right)    O(1)

Ideea-cheie:
    Orice interval de lungime L se acoperă cu DOUĂ ferestre de lungime
    `2^k`, unde k = floor(log2(L)): una lipită de capătul din stânga, una de
    capătul din dreapta. Se pot suprapune — de aceea merge doar pentru
    operații IDEMPOTENTE (min, max, gcd), nu pentru sumă.

    Prețul: nu există update. Dacă ai update-uri, folosește segment tree.
"""


class SparseTable:
    """RMQ static: minim pe [left, right] în O(1), fără update-uri."""

    def __init__(self, nums):
        self.n = len(nums)
        self.log = [0] * (self.n + 1)       # log[k] = floor(log2(k))
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.table = [list(nums)]           # nivelul 0: ferestre de lungime 1
        k = 1
        while (1 << k) <= self.n:
            prev = self.table[k - 1]        # ferestre de lungime 2^(k-1)
            half = 1 << (k - 1)
            size = self.n - (1 << k) + 1
            self.table.append([min(prev[i], prev[i + half]) for i in range(size)])
            k += 1

    def query(self, left, right):
        """Minimul nums[left..right] (ambele capete incluse). Interval nevid."""
        k = self.log[right - left + 1]
        row = self.table[k]
        return min(row[left], row[right - (1 << k) + 1])   # două ferestre lipite de capete

    def __repr__(self):
        return f"SparseTable(n={self.n}, nivele={len(self.table)})"


if __name__ == "__main__":
    st = SparseTable([4, 2, 7, 1, 9, 3])
    print("query(1, 3) ->", st.query(1, 3))    # 1 (min 2,7,1)
    print("query(0, 5) ->", st.query(0, 5))    # 1 (tot)
    print("query(0, 1) ->", st.query(0, 1))    # 2
    print("query(4, 5) ->", st.query(4, 5))    # 3
    print("query(2, 2) ->", st.query(2, 2))    # 7 (interval de lungime 1)

    print("nivele:", len(SparseTable([1]).table))   # 1 (doar nivelul 0)
    print("query single:", SparseTable([5]).query(0, 0))   # 5
