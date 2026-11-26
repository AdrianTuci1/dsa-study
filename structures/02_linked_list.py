"""
STRUCTURA: LINKED LIST (listă înlănțuită)

Ce este:
    O listă de noduri, fiecare nod ține o valoare și un pointer către următorul.
    Simplă (singly) = un singur pointer `next`. Dublă (doubly) = și `prev`.

Operații și complexitate:
    acces la index            O(n)   -> nu ai indexare, doar „mers" de la head
    inserare/ștergere la cap  O(1)   -> avantajul față de array
    inserare/ștergere la coadă O(1)  -> dacă ții și un pointer `tail`
    căutare                   O(n)

Ideea-cheie:
    Pentru a evita cazurile speciale de la cap, folosește un DUMMY NODE:
        dummy = ListNode(0, head)
    Pentru reverse ții trei pointeri: prev -> curr -> next.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def prepend(self, val):
        """Adaugă la început. O(1)."""
        self.head = ListNode(val, self.head)
        self._size += 1

    def append(self, val):
        """Adaugă la final. O(n) fără `tail`, O(1) cu `tail`."""
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._size += 1

    def delete(self, val):
        """Șterge prima apariție a valorii. O(n)."""
        dummy = ListNode(0, self.head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self._size -= 1
                break
            cur = cur.next
        self.head = dummy.next

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def reverse(self):
        """Inversează lista in-place. O(n) timp, O(1) spațiu."""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

    def __repr__(self):
        return " -> ".join(str(x) for x in self.to_list()) or "None"


class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """Cu head + tail: inserare/ștergere la ambele capete în O(1)."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def push_front(self, val):
        node = DoublyListNode(val, None, self.head)
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def push_back(self, val):
        node = DoublyListNode(val, self.tail, None)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self._size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def pop_back(self):
        if self.tail is None:
            raise IndexError("pop from empty list")
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out


if __name__ == "__main__":
    sll = SinglyLinkedList()
    for x in [1, 2, 3]:
        sll.append(x)
    print("singly append 1,2,3:", sll)        # 1 -> 2 -> 3
    sll.prepend(0)
    print("prepend(0):        ", sll)        # 0 -> 1 -> 2 -> 3
    sll.delete(2)
    print("delete(2):         ", sll)        # 0 -> 1 -> 3
    sll.reverse()
    print("reverse():         ", sll)        # 3 -> 1 -> 0

    dll = DoublyLinkedList()
    dll.push_back(1)
    dll.push_back(2)
    dll.push_front(0)
    print("doubly:            ", dll.to_list())   # [0, 1, 2]
    print("pop_back ->", dll.pop_back(), "| pop_front ->", dll.pop_front())
    print("doubly ramas:      ", dll.to_list())    # [1]
