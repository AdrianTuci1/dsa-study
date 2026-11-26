"""
HASH MAP — funcții (fără OOP)

Tabelul e o LISTĂ DE BUCKETS: fiecare bucket e o listă de perechi (cheie, valoare).
`hash(key) % len(table)` alege bucket-ul. Coliziunile se rezolvă prin înlănțuire.

Toate operațiile primesc `table` ca prim argument — fără clasă.

Complexitate: O(1) mediu per operație.
"""


def new_table(capacity=8):
    return [[] for _ in range(capacity)]


def put(table, key, value):
    bucket = table[hash(key) % len(table)]
    for i, (k, _) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)      # actualizează
            return
    bucket.append((key, value))


def get(table, key):
    for k, v in table[hash(key) % len(table)]:
        if k == key:
            return v
    raise KeyError(key)


def contains(table, key):
    return any(k == key for k, _ in table[hash(key) % len(table)])


def delete(table, key):
    bucket = table[hash(key) % len(table)]
    for i, (k, _) in enumerate(bucket):
        if k == key:
            bucket.pop(i)
            return
    raise KeyError(key)


# --- Utilitare practice pe dicționare (folosite la majoritatea problemelor) ---

def frequency(items):
    """Numără frecvențele. O(n)."""
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    return counts


def first_duplicate(items):
    """Primul element care se repetă, sau None. O(n)."""
    seen = set()
    for x in items:
        if x in seen:
            return x
        seen.add(x)
    return None


def two_sum(nums, target):
    """Indicii celor două numere care dau target. O(n)."""
    seen = {}                            # valoare -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    t = new_table()
    put(t, "a", 1)
    put(t, "b", 2)
    put(t, "a", 99)                      # suprascrie
    print("get('a')      ->", get(t, "a"))          # 99
    print("contains('b') ->", contains(t, "b"))     # True
    delete(t, "b")
    print("contains('b') ->", contains(t, "b"))     # False

    print("frequency:", frequency("hello"))         # {'h':1,'e':1,'l':2,'o':1}
    print("first_duplicate:", first_duplicate([1, 2, 3, 2, 1]))  # 2
    print("two_sum:", two_sum([2, 7, 11, 15], 9))   # [0, 1]
