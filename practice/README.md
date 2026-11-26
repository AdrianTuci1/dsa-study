# Practice — probleme de rezolvat singur

Aici ai **seturi de probleme pentru fiecare concept**, câte 3 per concept. Enunțurile sunt
**în engleză**, exact ca la interviu.

**Stare:** fișierele `01`–`16` sunt exercițiile tale (unele încă parțial rezolvate), iar
`17`–`25` conțin acum **soluții de referință complete** — toate testele trec, deci le poți
citi, compara cu ale tale și rescrie din memorie. `26`–`29` sunt încă stub-uri.
Pentru memorare (recall activ, repetiție spațiată) vezi
[`../learning/README.md`](../learning/README.md).

## Cum se folosește

1. Alege un concept (un fișier).
2. Citește enunțul fiecărei probleme din docstring/comentarii.
3. Scrie soluția înlocuind `raise NotImplementedError` din funcția problemei.
4. Rulează fișierul ca să-ți verifici singur rezultatul:

```bash
python3 practice/02_two_pointers.py
```

Output-ul folosește semne simple:
- `[ ]` — problema nu e încă rezolvată (stub-ul ridică `NotImplementedError`)
- `[v]` — test trecut
- `[x]` — test picat (îți arată ce ai primit vs. ce se aștepta)
- la final: `N/M passed`

> Sfat: rezolvă întâi **pe hârtie** (descompunere, exemplu mic, complexitate), apoi scrie codul.

## Concepetele

| # | Fișier | Concept |
|---|---|---|
| 01 | [`01_array_hashing.py`](./01_array_hashing.py) | Array & Hashing |
| 02 | [`02_two_pointers.py`](./02_two_pointers.py) | Two Pointers |
| 03 | [`03_sliding_window.py`](./03_sliding_window.py) | Sliding Window |
| 04 | [`04_fast_slow_pointers.py`](./04_fast_slow_pointers.py) | Fast & Slow Pointers |
| 05 | [`05_merge_intervals.py`](./05_merge_intervals.py) | Merge Intervals |
| 06 | [`06_cyclic_sort.py`](./06_cyclic_sort.py) | Cyclic Sort |
| 07 | [`07_inplace_linked_list_reversal.py`](./07_inplace_linked_list_reversal.py) | In-place Linked List Reversal |
| 08 | [`08_stack.py`](./08_stack.py) | Stack (incl. monotonic) |
| 09 | [`09_binary_search.py`](./09_binary_search.py) | Binary Search (incl. on answer) |
| 10 | [`10_tree_bfs.py`](./10_tree_bfs.py) | Tree BFS |
| 11 | [`11_tree_dfs.py`](./11_tree_dfs.py) | Tree DFS |
| 12 | [`12_two_heaps.py`](./12_two_heaps.py) | Two Heaps / Heap |
| 13 | [`13_backtracking.py`](./13_backtracking.py) | Backtracking |
| 14 | [`14_graph_bfs_dfs.py`](./14_graph_bfs_dfs.py) | Graph BFS / DFS |
| 15 | [`15_topological_sort.py`](./15_topological_sort.py) | Topological Sort |
| 16 | [`16_union_find.py`](./16_union_find.py) | Union Find (DSU) |
| 17 | [`17_dynamic_programming.py`](./17_dynamic_programming.py) | Dynamic Programming (1-D & 2-D) |
| 18 | [`18_greedy.py`](./18_greedy.py) | Greedy |

### Blocul avansat (după ce etapele 1–5 sunt închise)

| # | Fișier | Concept | Prioritate |
|---|---|---|---|
| 19 | [`19_tries.py`](./19_tries.py) | Tries (prefix tree) | ★ |
| 20 | [`20_design.py`](./20_design.py) | Design problems (LRU, Min Stack, coadă din două stive) | ○ |
| 21 | [`21_bit_manipulation.py`](./21_bit_manipulation.py) | Bit Manipulation | ○ |
| 22 | [`22_matrix.py`](./22_matrix.py) | Matrix / 2D Grid (spirală, rotire, zeroes) | ○ |
| 23 | [`23_advanced_graphs.py`](./23_advanced_graphs.py) | Grafuri avansate I (Dijkstra, MST, Bellman-Ford cu K opriri) | ○ |
| 24 | [`24_math_geometry.py`](./24_math_geometry.py) | Math & Geometry (happy number, fast pow, ciur) | ◇ |
| 25 | [`25_advanced_dp.py`](./25_advanced_dp.py) | DP avansat (0/1 knapsack, LIS, edit distance) | ○ |
| 26 | [`26_string_algorithms.py`](./26_string_algorithms.py) | Algoritmi pe stringuri (KMP, rolling hash, Manacher) | ◇ |
| 27 | [`27_advanced_structures.py`](./27_advanced_structures.py) | Structuri avansate (segment tree, Fenwick, sparse table) | ◇ |
| 28 | [`28_advanced_techniques.py`](./28_advanced_techniques.py) | Tehnici avansate (deque monoton, quickselect, sweep line) | ◇ |
| 29 | [`29_advanced_graphs_2.py`](./29_advanced_graphs_2.py) | Grafuri avansate II (SCC, punți, matching bipartit) | ◇ |

Fișierul 19 (Tries) este `★` și se poate face mai devreme, imediat după arbori (Etapa 4); restul
blocului este opțional și nu blochează etapele 1–5. Prioritatea fiecăruia e cea din
[`../LEARNING_TREE.md`](../LEARNING_TREE.md).

Ordinea urmează planul din [`../STUDY_PLAN.md`](../STUDY_PLAN.md). Teoria fiecărui concept e în
[`../TEHNICI.md`](../TEHNICI.md), iar implementările de structuri în
[`../structures/`](../structures/README.md) și [`../functions/`](../functions/README.md).

## Cum îți verifici progresul

Rulează toate fișierele dintr-o dată:

```bash
for f in practice/*.py; do echo "== $f =="; python3 "$f"; done
```

Numărul de `[v]` crește pe măsură ce rezolvi. Când un fișier afișează `N/N passed`, tot conceptul e gata.
