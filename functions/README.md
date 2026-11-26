# Functions — structuri implementate ca funcții (fără OOP)

Același set de structuri ca în [`../structures/`](../structures/README.md), dar scrise
**practic, fără clase**: funcții care primesc datele ca argument, exact cum ai scrie
la un interviu sau în competitive programming.

Regula: **nu există `class`**. Structurile sunt reprezentate cu tipuri native:
- listă Python → array, stack, heap
- `deque` → queue
- `[valoare, urmator]` → nod de linked list
- `dict` → hash map, trie, adjacency list, union-find (`parent` e o listă)

Rulează orice fișier direct:
```bash
python3 functions/06_heap.py
```

| # | Fișier | Structură | Cum e reprezentată |
|---|---|---|---|
| 01 | [`01_array.py`](./01_array.py) | Array | `list` |
| 02 | [`02_linked_list.py`](./02_linked_list.py) | Linked List | nod = `[valoare, urmator]` |
| 03 | [`03_stack.py`](./03_stack.py) | Stack | `list` (push/pop la un capăt) |
| 04 | [`04_queue.py`](./04_queue.py) | Queue | `collections.deque` |
| 05 | [`05_hash_map.py`](./05_hash_map.py) | HashMap | listă de buckets |
| 06 | [`06_heap.py`](./06_heap.py) | Heap | `list` + `sift_up` / `sift_down` |
| 07 | [`07_tree.py`](./07_tree.py) | Tree / BST | tuplu `(val, stanga, dreapta)` |
| 08 | [`08_graph.py`](./08_graph.py) | Graph | `dict` adjacency list |
| 09 | [`09_trie.py`](./09_trie.py) | Trie | `dict` imbricat |
| 10 | [`10_union_find.py`](./10_union_find.py) | Union Find (DSU) | listă `parent` + `rank` |
| 11 | [`11_segment_tree.py`](./11_segment_tree.py) | Segment Tree | tuplu `(tree, n)`, 4n noduri indexate de la 1 |
| 12 | [`12_fenwick.py`](./12_fenwick.py) | Fenwick / BIT | listă `tree` de lungime n+1 (1-based) |
| 13 | [`13_sparse_table.py`](./13_sparse_table.py) | Sparse Table | tuplu `(table, log)` de liste |

## structures/ vs functions/ — când folosești ce

| | `structures/` (OOP) | `functions/` (fără OOP) |
|---|---|---|
| Stil | clase cu metode | funcții cu argumente |
| Când | citești/înveți designul structurii | scrii repede la interviu |
| Exemplu | `stack.pop()` | `pop(stack)` |
| Avantaj | encapsulare, claritate | direct, fără boilerplate |

Explicația conceptuală (când le folosești, complexități) e în [`../STRUCTURI.md`](../STRUCTURI.md).
