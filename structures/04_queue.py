"""
STRUCTURA: QUEUE (coadă)

Ce este:
    Structură FIFO (First In, First Out) — primul intrat e primul ieșit.
    Gândește „coadă la magazin".

Operații și complexitate:
    enqueue(x)  O(1)
    dequeue()   O(1)   (cu deque; cu listă simplă ar fi O(n) la popleft)
    peek()      O(1)

Ideea-cheie:
    Baza pentru BFS (parcurgere nivel cu nivel) și pentru orice „procesare în ordine".
    În Python folosește `collections.deque` — `append` și `popleft` sunt ambele O(1).
    NU folosi `list.pop(0)`: e O(n), fiindcă mută toate elementele.
"""

from collections import deque


class Queue:
    def __init__(self, iterable=None):
        self._data = deque(iterable) if iterable else deque()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]

    def is_empty(self):
        return not self._data

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue(front -> back: {list(self._data)})"


class CircularQueue:
    """Coadă cu capacitate fixă, implementată pe un array circular.

    Folosită în sisteme reale (buffer de rețea, scheduler) pentru a refolosi
    spațiul fără realocare. Inițializarea e O(capacity), restul O(1).
    """

    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * capacity
        self._head = 0          # indexul din față
        self._size = 0

    def enqueue(self, value):
        if self.is_full():
            raise IndexError("queue is full")
        tail = (self._head + self._size) % self._capacity
        self._data[tail] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def __len__(self):
        return self._size

    def __repr__(self):
        items = [self._data[(self._head + i) % self._capacity] for i in range(self._size)]
        return f"CircularQueue(front -> back: {items}, cap={self._capacity})"


if __name__ == "__main__":
    q = Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print(q)                          # front -> back: [1, 2, 3]
    print("dequeue ->", q.dequeue())  # 1
    print("peek    ->", q.peek())     # 2
    print(q)

    cq = CircularQueue(3)
    cq.enqueue("a")
    cq.enqueue("b")
    cq.enqueue("c")
    print(cq)                                     # [a, b, c]
    print("dequeue ->", cq.dequeue())             # a
    cq.enqueue("d")                               # refolosim slotul
    print(cq)                                     # [b, c, d]
