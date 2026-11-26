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
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if self._size == self.__capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index):
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        for i in range(index, self._size - 1)
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
    
    def find(self, value):
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