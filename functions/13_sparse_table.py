"""
SPARSE TABLE — funcții (fără OOP)

RMQ static (minim pe interval) ca două LISTE, fără clasă:

    table[k][i] = minimul din fereastra de lungime 2^k care începe pe poziția i
    log[i]      = floor(log2(i))     (precalculat, ca query-ul să fie O(1))

    build: O(n log n)      query: O(1)      update: NU există

Toate funcțiile primesc `(table, log)` ca argumente. Merge doar pentru operații
IDEMPOTENTE (min, max, gcd) — nu pentru sumă, fiindcă ferestrele se suprapun.
"""


def sparse_build(nums):
    """Construiește tabelul. Returnează `(table, log)`."""
    n = len(nums)
    log = [0] * (n + 1)                 # log[k] = floor(log2(k))
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1

    table = [list(nums)]                # nivelul 0: ferestre de lungime 1
    k = 1
    while (1 << k) <= n:
        prev = table[k - 1]
        half = 1 << (k - 1)
        size = n - (1 << k) + 1
        table.append([min(prev[i], prev[i + half]) for i in range(size)])
        k += 1
    return table, log


def sparse_query(table, log, left, right):
    """Minimul nums[left..right] (interval nevid). Două ferestre lipite de capete."""
    k = log[right - left + 1]
    row = table[k]
    return min(row[left], row[right - (1 << k) + 1])


if __name__ == "__main__":
    st, lg = sparse_build([4, 2, 7, 1, 9, 3])
    print("query(1, 3) ->", sparse_query(st, lg, 1, 3))   # 1 (min 2,7,1)
    print("query(0, 5) ->", sparse_query(st, lg, 0, 5))   # 1 (tot)
    print("query(0, 1) ->", sparse_query(st, lg, 0, 1))   # 2
    print("query(2, 2) ->", sparse_query(st, lg, 2, 2))   # 7 (lungime 1)

    st1, lg1 = sparse_build([5])
    print("nivele pt. n=1:", len(st1))                    # 1 (doar nivelul 0)
    print("query(0, 0) ->", sparse_query(st1, lg1, 0, 0)) # 5

    # Când e util: multe query-uri pe un array care nu se schimbă (RMQ static)
    st2, lg2 = sparse_build([9, 4, 7, 1, 8, 2])
    print("query(0, 5) ->", sparse_query(st2, lg2, 0, 5)) # 1
    print("query(0, 2) ->", sparse_query(st2, lg2, 0, 2)) # 4
