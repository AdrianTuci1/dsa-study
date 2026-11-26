"""
STRUCTURA: ARRAY (tabel dinamic / Dynamic Array)

Ce este:
    O colecție de elemente așezate consecutiv în memorie, accesate prin index.
    Aici implementăm de la zero un array dinamic (ca `list()` din Python), ca să
    înțelegem de ce accesul e O(1) și de ce inserarea la mijloc e O(n).

Operații și complexitate:
    get(i)         O(1)        acces direct la index
    push(v)        O(1)        amortizat (când se umple, dublăm capacitatea)
    insert(i, v)   O(n)        mutăm elementele spre dreapta
    delete(i)      O(n)        mutăm elementele spre stânga
    find(v)        O(n)        căutare liniară

Ideea-cheie:
    Accesul e O(1) pentru că adresa se calculează direct: baza + index * mărime.
    Dublarea capacității la umplere face ca push să fie O(1) AMORTIZAT: costul
    copierii e „plătit" de toate push-urile de dinainte.
"""


class DynamicArray:
    def __init__(self, capacity=2):
        self._capacity = max(1, capacity)
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def get(self, index):
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def push(self, value):
        """Adaugă la final. O(1) amortizat."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        """Inserează la index, împingând restul la dreapta. O(n)."""
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index):
        """Șterge elementul de la index, trăgând restul la stânga. O(n)."""
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1

    def find(self, value):
        """Returnează indexul primei apariții sau -1. O(n)."""
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __repr__(self):
        items = ", ".join(str(self._data[i]) for i in range(self._size))
        return f"[{items}] (size={self._size}, capacity={self._capacity})"


if __name__ == "__main__":
    arr = DynamicArray()
    for x in [10, 20, 30]:
        arr.push(x)
    print("dupa push:", arr)                 # [10, 20, 30]

    arr.insert(1, 15)
    print("dupa insert(1, 15):", arr)        # [10, 15, 20, 30]

    arr.delete(0)
    print("dupa delete(0):", arr)            # [15, 20, 30]

    print("find(20) ->", arr.find(20))       # 1
    print("get(2)   ->", arr.get(2))         # 30
    print("len      ->", len(arr))           # 3
