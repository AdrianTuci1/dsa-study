"""
STRUCTURA: HASH MAP / HASH SET

Ce este:
    HashMap = colecție cheie -> valoare cu acces (aproape) O(1).
    HashSet = doar chei unice, fără valori.

Operații și complexitate (medie):
    put(key, value)   O(1)
    get(key)          O(1)
    delete(key)       O(1)
    contains(key)     O(1)

    În cazul cel mai rău toate devin O(n) dacă toate cheile ajung în același bucket
    (coliziune). De aceea redimensionăm când load factor-ul depășește ~0.75.

Ideea-cheie:
    `hash(key) % capacity` decide bucket-ul. Coliziunile se rezolvă prin
    ÎNLĂNȚUIRE (chaining): fiecare bucket e o listă de perechi (key, value).

    În Python, `dict` și `set` sunt deja implementate eficient — folosește-le în
    cod real. Aici le construim ca să înțelegem mecanismul.
"""


class HashMap:
    def __init__(self, capacity=8, load_factor=0.75):
        self._capacity = max(1, capacity)
        self._load_factor = load_factor
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def _hash(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        bucket = self._buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:                 # cheie existentă -> actualizăm
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / self._capacity > self._load_factor:
            self._resize(self._capacity * 2)

    def get(self, key):
        for k, v in self._buckets[self._hash(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key):
        bucket = self._buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        return any(k == key for k, _ in self._buckets[self._hash(key)])

    def _resize(self, new_capacity):
        old_items = [item for bucket in self._buckets for item in bucket]
        self._capacity = new_capacity
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0
        for k, v in old_items:
            self.put(k, v)

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"HashMap({ {k: v for b in self._buckets for k, v in b} })"


class HashSet:
    """Doar mulțime de chei unice, construită peste un map."""

    def __init__(self):
        self._map = HashMap()

    def add(self, key):
        self._map.put(key, True)

    def remove(self, key):
        self._map.delete(key)

    def contains(self, key):
        return self._map.contains(key)

    def __len__(self):
        return len(self._map)

    def __repr__(self):
        return f"HashSet({ {k for b in self._map._buckets for k, _ in b} })"


if __name__ == "__main__":
    m = HashMap()
    m.put("a", 1)
    m.put("b", 2)
    m.put("a", 99)                    # suprascrie
    print(m)                          # {'a': 99, 'b': 2}
    print("get('a')      ->", m.get("a"))
    print("contains('b') ->", m.contains("b"))
    m.delete("b")
    print("dupa delete('b'):", m, "| len =", len(m))

    s = HashSet()
    for x in [1, 2, 2, 3]:
        s.add(x)
    print(s)                          # {1, 2, 3}
    print("contains(2) ->", s.contains(2))
