"""
STRUCTURA: HEAP (Priority Queue)

Ce este:
    Un arbore binar complet (reprezentat ca array) care ține mereu extremul
    (minimul sau maximul) în rădăcină. NU e sortat complet — doar rădăcina e garantată.

Operații și complexitate:
    push(x)            O(log n)
    pop()  (extremul)  O(log n)
    peek() (rădăcina)  O(1)
    build (heapify)    O(n)

Reprezentare în array (0-indexat):
    parent(i) = (i - 1) // 2
    left(i)   = 2 * i + 1
    right(i)  = 2 * i + 2

Ideea-cheie:
    MIN-HEAP: fiecare părinte <= copii. MAX-HEAP: fiecare părinte >= copii.
    `sift_up` (la push) urcă elementul nou; `sift_down` (la pop/heapify) coboară rădăcina.

    În Python, `heapq` = min-heap. Pentru max-heap se pun valorile negative.
"""


class MinHeap:
    def __init__(self, items=None):
        self._data = list(items) if items else []
        if self._data:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def push(self, value):
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self):
        """Scoate și returnează minimul."""
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] < self._data[parent]:
                self._data[i], self._data[parent] = self._data[parent], self._data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self._data)
        while True:
            smallest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == i:
                break
            self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
            i = smallest

    def _heapify(self):
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i)

    def __repr__(self):
        return f"MinHeap({self._data})"


class MaxHeap:
    """Max-heap = min-heap peste valori negate."""

    def __init__(self, items=None):
        self._heap = MinHeap([-x for x in items] if items else None)

    def __len__(self):
        return len(self._heap)

    def push(self, value):
        self._heap.push(-value)

    def pop(self):
        return -self._heap.pop()

    def peek(self):
        return -self._heap.peek()

    def __repr__(self):
        return f"MaxHeap({[-x for x in self._heap._data]})"


if __name__ == "__main__":
    h = MinHeap([5, 3, 8, 1, 9, 2])
    print("heapify:", h)                       # radacina = 1
    h.push(0)
    print("dupa push(0):", h)
    print("pop ->", h.pop())                   # 0
    print("pop ->", h.pop())                   # 1
    print("peek ->", h.peek())                 # 2

    mx = MaxHeap([5, 3, 8, 1])
    print("max peek:", mx.peek())              # 8
    mx.push(10)
    print("max pop ->", mx.pop())              # 10

    # Aplicație clasică: cele mai mari k elemente
    import heapq
    nums, k = [3, 1, 4, 1, 5, 9, 2, 6], 3
    print(f"top {k} din {nums}:", heapq.nlargest(k, nums))   # [9, 6, 5]
