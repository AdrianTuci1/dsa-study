"""
QUEUE — funcții (fără OOP)

O coadă FIFO se face practic cu `collections.deque`: `append` la dreapta,
`popleft` din stânga — ambele O(1).

⚠️ Nu folosi `list.pop(0)` — e O(n), mută toate elementele.
"""

from collections import deque


def new_queue(iterable=None):
    return deque(iterable) if iterable else deque()


def enqueue(q, value):
    q.append(value)              # adaugă la spate. O(1)


def dequeue(q):
    if not q:
        raise IndexError("dequeue from empty queue")
    return q.popleft()           # scoate din față. O(1)


def peek(q):
    if not q:
        raise IndexError("peek from empty queue")
    return q[0]


def is_empty(q):
    return not q


def size(q):
    return len(q)


def rotate(q, k):
    """Rotește coada cu k poziții (ex. round-robin). O(k)."""
    for _ in range(k % len(q) if q else 0):
        q.append(q.popleft())
    return q


def process_in_order(tasks):
    """Aplicație: procesează elementele în ordinea sosirii. O(n)."""
    q = new_queue(tasks)
    out = []
    while not is_empty(q):
        out.append(dequeue(q))
    return out


if __name__ == "__main__":
    q = new_queue()
    for x in [1, 2, 3]:
        enqueue(q, x)
    print("queue:", list(q))                     # [1, 2, 3]
    print("dequeue ->", dequeue(q))              # 1
    print("peek    ->", peek(q))                 # 2
    print("queue:", list(q))                     # [2, 3]

    print("rotate(1):", list(rotate(new_queue([1, 2, 3, 4]), 1)))  # [2, 3, 4, 1]
    print("process:", process_in_order(["a", "b", "c"]))           # ['a', 'b', 'c']
