# Structures — implementări de structuri de date

Câte un fișier de cod pentru fiecare structură, implementată **de la zero** (fără
biblioteci), cu explicație în docstring și un exemplu rulabil la final.

Rulează orice fișier direct:
```bash
python3 structures/01_array.py
```

| # | Fișier | Structură | Operații principale |
|---|---|---|---|
| 01 | [`01_array.py`](./01_array.py) | Array dinamic (ArrayList) | get O(1), push O(1) amortizat, insert/delete O(n) |
| 02 | [`02_linked_list.py`](./02_linked_list.py) | Linked List (simplă + dublă) | prepend O(1), reverse O(n), delete O(n) |
| 03 | [`03_stack.py`](./03_stack.py) | Stack (LIFO) | push/pop/peek O(1) |
| 04 | [`04_queue.py`](./04_queue.py) | Queue (FIFO) + coadă circulară | enqueue/dequeue O(1) |
| 05 | [`05_hash_map.py`](./05_hash_map.py) | HashMap (chaining) + HashSet | put/get/delete O(1) mediu |
| 06 | [`06_heap.py`](./06_heap.py) | MinHeap / MaxHeap | push/pop O(log n), peek O(1) |
| 07 | [`07_tree.py`](./07_tree.py) | Binary Tree + BST | traversări O(n), search/insert/delete mediu O(log n) |
| 08 | [`08_graph.py`](./08_graph.py) | Graph (adjacency list) | BFS/DFS O(V+E), topo sort, cicluri |
| 09 | [`09_trie.py`](./09_trie.py) | Trie (prefix tree) | insert/search/startsWith O(L) |
| 10 | [`10_segment_tree.py`](./10_segment_tree.py) | Segment Tree (sumă pe interval) | build O(n), update/query O(log n) |
| 11 | [`11_fenwick.py`](./11_fenwick.py) | Fenwick / BIT (prefix sums) | build O(n), add/prefix_sum O(log n) |
| 12 | [`12_sparse_table.py`](./12_sparse_table.py) | Sparse Table (RMQ static) | build O(n log n), query O(1), fără update |

Explicația conceptuală (când le folosești, complexități, capcane) e în
[`../STRUCTURI.md`](../STRUCTURI.md).
