"""
STRUCTURA: SEGMENT TREE (arbore de intervale)

Ce este:
    Un arbore binar construit peste array-ul `nums`, în care fiecare nod ține
    agregatul (aici SUMA) unei porțiuni [lo, hi]. Frunzele sunt elementele,
    iar fiecare nod intern = suma celor doi copii.

Operații și complexitate:
    build(nums)            O(n)
    update(index, value)   O(log n)
    query(left, right)     O(log n)

Reprezentare în array (indexarea nodurilor de la 1):
    nod i -> copii 2*i și 2*i+1, rădăcina 1
    pentru n elemente e nevoie de 4*n noduri

Ideea-cheie:
    Orice interval se descompune în O(log n) noduri ale arborelui. La o
    modificare pe poziție recalculezi doar drumul de la frunză la rădăcină,
    nu tot array-ul. Pentru SUMĂ se poate folosi și Fenwick (mai scurt), dar
    segment tree-ul e general: merge la min/max/gcd, lazy propagation, etc.
"""


class SegmentTree:
    """Segment tree pentru sumă pe interval, cu update pe poziție (set)."""

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)      # 4*n e dimensiunea sigură
        if self.n:
            self._build(1, 0, self.n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:                        # frunză = un singur element
            self.tree[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, index, value):
        """Setează nums[index] = value."""
        self._update(1, 0, self.n - 1, index, value)

    def _update(self, node, lo, hi, i, value):
        if lo == hi:
            self.tree[node] = value
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node, lo, mid, i, value)
        else:
            self._update(2 * node + 1, mid + 1, hi, i, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, left, right):
        """Suma nums[left..right] (ambele capete incluse)."""
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, lo, hi, left, right):
        if right < lo or hi < left:         # interval disjunct
            return 0
        if left <= lo and hi <= right:      # interval complet acoperit
            return self.tree[node]
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, left, right)
                + self._query(2 * node + 1, mid + 1, hi, left, right))

    def __repr__(self):
        return f"SegmentTree(n={self.n}, tree={self.tree[:2 * self.n]})"


if __name__ == "__main__":
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    print("query(1, 3) ->", st.query(1, 3))        # 15 (3+5+7)
    print("query(0, 5) ->", st.query(0, 5))        # 36 (tot)

    st.update(1, 10)                               # nums[1] = 10
    print("dupa update(1, 10)")
    print("query(1, 3) ->", st.query(1, 3))        # 22 (10+5+7)
    print("query(1, 1) ->", st.query(1, 1))        # 10
    print("query(2, 2) ->", st.query(2, 2))        # 5

    # Aplicație clasică: sumă pe subarray, multe query-uri amestecate cu update-uri
    st2 = SegmentTree([4, -1, 0, 6, 2])
    st2.update(2, 100)
    print("query(0, 2) ->", st2.query(0, 2))       # 103 (4-1+100)
