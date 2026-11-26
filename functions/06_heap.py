"""
HEAP — funcții (fără OOP)

Un min-heap e doar o LISTĂ cu regula: fiecare părinte <= copii.
    parent(i) = (i - 1) // 2       left(i) = 2i + 1       right(i) = 2i + 2

Toate funcțiile primesc lista `h` ca argument — fără clasă.

Complexități: push O(log n), pop O(log n), peek O(1), heapify O(n).
"""


def sift_up(h, i):
    """Urcă elementul de la i până își găsește locul (folosit la push)."""
    while i > 0:
        parent = (i - 1) // 2
        if h[i] < h[parent]:
            h[i], h[parent] = h[parent], h[i]
            i = parent
        else:
            break


def sift_down(h, i, size=None):
    """Coboară elementul de la i (folosit la pop și heapify)."""
    n = size if size is not None else len(h)
    while True:
        smallest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and h[left] < h[smallest]:
            smallest = left
        if right < n and h[right] < h[smallest]:
            smallest = right
        if smallest == i:
            break
        h[i], h[smallest] = h[smallest], h[i]
        i = smallest


def heap_push(h, value):
    h.append(value)
    sift_up(h, len(h) - 1)


def heap_pop(h):
    """Scoate și returnează minimul."""
    if not h:
        raise IndexError("pop from empty heap")
    top = h[0]
    last = h.pop()
    if h:
        h[0] = last
        sift_down(h, 0)
    return top


def heap_peek(h):
    if not h:
        raise IndexError("peek from empty heap")
    return h[0]


def heapify(values):
    """Transformă o listă în heap, in-place, în O(n). Returnează lista."""
    h = list(values)
    for i in range(len(h) // 2 - 1, -1, -1):
        sift_down(h, i)
    return h


def k_largest(nums, k):
    """Cele mai mari k elemente, folosind un min-heap de dimensiune k. O(n log k)."""
    h = []
    for x in nums:
        heap_push(h, x)
        if len(h) > k:
            heap_pop(h)                  # scoatem minimul -> rămân cele mai mari
    return sorted(h, reverse=True)


# --- Max-heap simplu: aceleași funcții, dar pe valori negate ---

def max_push(h, value):
    heap_push(h, -value)


def max_pop(h):
    return -heap_pop(h)


def max_peek(h):
    return -heap_peek(h)


if __name__ == "__main__":
    h = heapify([5, 3, 8, 1, 9, 2])
    print("heapify, radacina:", h[0])            # 1
    heap_push(h, 0)
    print("pop ->", heap_pop(h))                 # 0
    print("pop ->", heap_pop(h))                 # 1
    print("peek ->", heap_peek(h))               # 2

    print("k_largest([3,1,4,1,5,9,2,6], 3):", k_largest([3, 1, 4, 1, 5, 9, 2, 6], 3))  # [9,6,5]

    mh = []
    for x in [5, 3, 8]:
        max_push(mh, x)
    print("max peek:", max_peek(mh))             # 8
