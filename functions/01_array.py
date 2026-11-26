"""
ARRAY — operații ca FUNCȚII (fără OOP)

Ideea: un array e deja o listă Python. Nu ai nevoie de clasă — scrii funcții care
primesc lista ca argument. Așa arată codul „de interviu", unde implementezi doar
operația cerută, nu o clasă întreagă.

Complexități:
    insert_at / delete_at   O(n)   (mută elementele)
    find                    O(n)
    prefix_sums             O(n)   (apoi range_sum e O(1)!)
    reverse_in_place        O(n)
"""


def insert_at(arr, index, value):
    """Inserează manual, împingând restul la dreapta. O(n)."""
    arr.append(None)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value
    return arr


def delete_at(arr, index):
    """Șterge manual, trăgând restul la stânga. O(n)."""
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    return arr


def find(arr, value):
    for i, x in enumerate(arr):
        if x == value:
            return i
    return -1


def prefix_sums(arr):
    """prefix[i] = suma primelor i elemente. Suma oricărui interval devine O(1)."""
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix, left, right):
    """Suma arr[left..right] inclusiv, din prefix sums. O(1)."""
    return prefix[right + 1] - prefix[left]


def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def rotate_right(arr, k):
    """Rotire la dreapta cu k poziții. O(n)."""
    n = len(arr)
    if n == 0:
        return arr
    k %= n
    return arr[-k:] + arr[:-k] if k else arr[:]


if __name__ == "__main__":
    arr = [10, 20, 30]
    insert_at(arr, 1, 15)
    print("insert_at(1, 15):", arr)           # [10, 15, 20, 30]

    delete_at(arr, 0)
    print("delete_at(0):    ", arr)           # [15, 20, 30]

    print("find(20) ->", find(arr, 20))       # 1

    p = prefix_sums([1, 2, 3, 4])
    print("prefix_sums:", p)                  # [0, 1, 3, 6, 10]
    print("sum(1..2)  ->", range_sum(p, 1, 2))  # 5

    print("reverse:", reverse_in_place([1, 2, 3]))        # [3, 2, 1]
    print("rotate(2):", rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
