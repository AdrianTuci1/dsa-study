"""
LINKED LIST — funcții (fără OOP)

Fără clasă de nod! Reprezentăm un nod ca o LISTĂ de 2 elemente: [valoare, urmator].
Sfârșitul listei = None.

    [1, [2, [3, None]]]   <=>   1 -> 2 -> 3

Avantaj: nodurile sunt mutabile, deci poți face reverse in-place ȘI poți crea
cicluri (pentru testul de ciclu). Toate operațiile sunt funcții care primesc `head`.

Complexități: toate O(n) timp, O(1) spațiu suplimentar.
"""


def build(values):
    """Construiește lista din valori: [1,2,3] -> [1, [2, [3, None]]]."""
    head = None
    for v in reversed(values):
        head = [v, head]
    return head


def to_list(head):
    """Lista de valori (nu folosi pe o listă cu ciclu — se blochează!)."""
    out = []
    while head is not None:
        out.append(head[0])
        head = head[1]
    return out


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head[1]
    return count


def find(head, value):
    while head is not None:
        if head[0] == value:
            return True
        head = head[1]
    return False


def reverse(head):
    """Reverse in-place: întoarce noul cap. O(n) timp, O(1) spațiu."""
    prev = None
    while head is not None:
        nxt = head[1]
        head[1] = prev
        prev = head
        head = nxt
    return prev


def middle(head):
    """Mijlocul cu fast & slow pointers. O(n)."""
    slow = fast = head
    while fast is not None and fast[1] is not None:
        slow = slow[1]
        fast = fast[1][1]
    return slow


def has_cycle(head):
    """Detectare ciclu cu fast & slow (Floyd). O(n) timp, O(1) spațiu."""
    slow = fast = head
    while fast is not None and fast[1] is not None:
        slow = slow[1]
        fast = fast[1][1]
        if slow is fast:
            return True
    return False


def merge_sorted(a, b):
    """Interclasează două liste sortate. O(n + m)."""
    dummy = [0, None]
    tail = dummy
    while a is not None and b is not None:
        if a[0] <= b[0]:
            tail[1] = a
            a = a[1]
        else:
            tail[1] = b
            b = b[1]
        tail = tail[1]
    tail[1] = a if a is not None else b
    return dummy[1]


if __name__ == "__main__":
    head = build([1, 2, 3, 4])
    print("build:   ", to_list(head))          # [1, 2, 3, 4]
    print("length:  ", length(head))           # 4
    print("middle:  ", middle(head)[0])        # 3
    print("find(3): ", find(head, 3))          # True

    print("reverse: ", to_list(reverse(head)))  # [4, 3, 2, 1]

    a, b = build([1, 3, 5]), build([2, 4, 6])
    print("merge:   ", to_list(merge_sorted(a, b)))  # [1..6]

    # Ciclu: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (înapoi)
    c1, c2 = build([1, 2, 3]), build([4, 5])
    c1[1][1][1] = c2          # 3 -> 4
    c2[1][1] = c1[1]          # 5 -> 2
    print("has_cycle:", has_cycle(c1))         # True
