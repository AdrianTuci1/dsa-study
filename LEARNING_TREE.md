# Arborele de învățare — ce stăpânești înainte să treci mai departe

Scopul fișierului: să nu sari la un concept nou până nu-l stăpânești pe cel de dinainte.
Fiecare etapă are o **poartă** — un criteriu concret pe care îl treci înainte să urci.

**Cum se citește:** `★` esențial pentru interviu · `○` util, apare des · `◇` opțional, după ce
restul e solid. Codurile `E1.2` sunt doar numerotare în acest fișier, ca să putem vorbi despre
un nod anume — nu au legătură cu numerotarea din `practice/`.

> Regula: nu înveți „mai multe concepte", înveți **un concept bine**. O etapă se închide
> doar când fișierele ei de practice sunt `N/N passed` **și** le poți rescrie din memorie
> a doua zi.

---

## Arborele complet

```
ETAPA 0 — META (nu se termină niciodată, se exersează la fiecare problemă)
├── E0.1 Analiza complexității (O timp + O spațiu)            ★
├── E0.2 Descompunerea problemei (STUDY_PLAN §3)              ★
└── E0.3 Trace pe hârtie / dry-run                            ★
        │
        ▼
ETAPA 1 — FUNDAȚIA
├── E1.1 Array & Hashing                     ★   practice/01
├── E1.2 Two Pointers                        ★   practice/02
├── E1.3 Stack                               ★   practice/08
│        └── E1.3a Monotonic Stack           ○   (tot în practice/08)
└── E1.4 Queue                               ★   STRUCTURI §5 · structures/04_queue.py
        │
        ▼
ETAPA 2 — TEHNICI PE ARRAY/STRING + LISTE
├── E2.1 Sliding Window                      ★   practice/03
├── E2.2 Binary Search                       ★   practice/09
│        ├── E2.2a Căutare pe array rotit    ○
│        └── E2.2b Binary search pe răspuns  ★   (Koko, în practice/09)
├── E2.3 Linked List                         ★   STRUCTURI §3 · structures/02_linked_list.py
│        ├── E2.3a Fast & Slow Pointers      ★   practice/04
│        └── E2.3b In-place Reversal         ★   practice/07
├── E2.4 Merge Intervals                     ★   practice/05
├── E2.5 Cyclic Sort                         ○   practice/06
├── E2.6 Prefix Sum / sumă rulantă           ★   (baza pentru practice/03)
├── E2.7 Sortare + comparator                ★   (unealtă: 05, 06, 18)
└── E2.8 Matrix / grid 2D                    ○   practice/22 · TEHNICI §21
        │
        ▼
ETAPA 3 — ARBORI
├── E3.1 Tree BFS / level order              ★   practice/10
├── E3.2 Tree DFS (pre / in / post)          ★   practice/11
├── E3.3 BST (validate, kth smallest, LCA)   ★   practice/11 + problems/07.trees
└── E3.4 Construcție & serializare           ○   problems/07.trees
        │
        ▼
ETAPA 4 — PE ARBORI + RECURSIE
├── E4.1 Tries                               ★   STRUCTURI §10 · structures/09_trie.py · practice/19 · TEHNICI §18
└── E4.2 Backtracking                        ★   practice/13
         ├── E4.2a Subsets / combinații      ★
         ├── E4.2b Permutări                 ★
         ├── E4.2c Pruning (tăierea ramurilor) ★
         └── E4.2d Backtracking pe grid      ○   (Word Search)
        │
        ▼
ETAPA 5 — NIVEL AVANSAT (ordinea internă e flexibilă)
├── E5.1 Heap / Priority Queue               ★   practice/12
├── E5.2 Two Heaps                           ★   practice/12
├── E5.3 Graphs (BFS/DFS, grid, clone)       ★   practice/14
├── E5.4 Topological Sort                    ★   practice/15
├── E5.5 Union Find (DSU)                    ○   practice/16 · functions/10_union_find.py
├── E5.6 Advanced Graphs (Dijkstra, Bellman-Ford, MST)  ○   practice/23 · TEHNICI §22
├── E5.7 1-D DP                              ★   practice/17
├── E5.8 2-D DP                              ★   practice/17
└── E5.9 Greedy                              ★   practice/18
        │
        ▼
ETAPA 6 — DUPĂ INTERVIU / SPECIALIZARE (opțional)
├── E6.1 Design problems (LRU, LFU, Min Stack)          ○   practice/20 · TEHNICI §19
├── E6.2 Bit Manipulation                               ○   practice/21 · TEHNICI §20
├── E6.3 Math & Geometry                                ◇   practice/24 · TEHNICI §23
├── E6.4 Structuri avansate: Segment Tree, Fenwick (BIT), Sparse Table   ◇   practice/27 · STRUCTURI §11–13 · TEHNICI §26
├── E6.5 Tehnici avansate: sweep line, monotonic deque, quickselect,
│        binary lifting, meet-in-the-middle                             ◇   practice/28 · TEHNICI §27
├── E6.6 Algoritmi pe stringuri: KMP, Rabin-Karp, Z, Manacher,
│        Aho-Corasick                                                   ◇   practice/26 · TEHNICI §25
├── E6.7 DP avansat: knapsack, LIS, interval DP, bitmask, digit DP,
│        DP pe arbore                                                   ○   practice/25 · TEHNICI §24
├── E6.8 Grafuri avansate: SCC, punți/articulații, Euler, max flow,
│        bipartite matching                                             ◇   practice/29 · TEHNICI §28
└── E6.9 Competiție: Mo's algorithm, convex hull trick, simulare        ◇   TEHNICI §29 (fără fișier de practice)
```

---

## Etapa 0 — Meta

Nu e o etapă pe care o închizi, e ceva ce faci la fiecare problemă din toate celelalte etape.

| Nod | Ce înseamnă | Unde |
|---|---|---|
| E0.1 | Spui O(timp) și O(spațiu) pentru orice soluție, și știi ce e „acceptabil" pentru n ≤ 10⁵ vs n ≤ 20 | `STUDY_PLAN.md` §1 |
| E0.2 | Ce e inputul → reformulezi în cuvinte → cauți tiparul → exemplu mic pe hârtie → scrii brut → edge cases | `STUDY_PLAN.md` §3 |
| E0.3 | Rulezi algoritmul manual, în tabel, pe un exemplu de 5-6 elemente | orice problemă |

---

## Etapa 1 — Fundația

| Nod | Concept | Prioritate | Material | Poarta |
|---|---|---|---|---|
| E1.1 | Array & Hashing | ★ | `practice/01_array_hashing.py` · `STRUCTURI.md` §1, §2, §6 · `structures/01_array.py`, `05_hash_map.py` | 01 → `N/N passed` |
| E1.2 | Two Pointers | ★ | `practice/02_two_pointers.py` · `TEHNICI.md` §1 | 02 → `N/N passed` |
| E1.3 | Stack | ★ | `practice/08_stack.py` · `STRUCTURI.md` §4 · `structures/03_stack.py` | 08 → `N/N passed` |
| E1.3a | Monotonic Stack | ○ | tot `practice/08_stack.py` (Next Greater Element, Daily Temperatures) | cele 2 probleme de stack monoton trec |
| E1.4 | Queue | ★ | `STRUCTURI.md` §5 · `structures/04_queue.py` · `functions/04_queue.py` | scrii o coadă cu `deque` din memorie |

Aici nu înveți tipare, înveți **uneltele** din care sunt făcute toate celelalte. Fiecare tipar de
mai sus e o combinație de acces la index, doi pointeri, o stivă sau o coadă.

**Poarta etapei:** `01`, `02`, `08` → `N/N passed`, și a doua zi le rescrii din memorie.

---

## Etapa 2 — Tehnici pe array/string + liste

| Nod | Concept | Prioritate | Material | Poarta |
|---|---|---|---|---|
| E2.1 | Sliding Window | ★ | `practice/03_sliding_window.py` · `TEHNICI.md` §2 | 03 → `N/N passed` |
| E2.2 | Binary Search | ★ | `practice/09_binary_search.py` · `TEHNICI.md` §11 | 09 → `N/N passed` |
| E2.2a | Căutare pe array rotit | ○ | `problems/05.binary_search/` | cele 2 probleme de array rotit |
| E2.2b | Binary search pe răspuns | ★ | Koko Eating Bananas, în `practice/09` | știi să scrii `check(mid)` și să cauți primul `True` |
| E2.3 | Linked List | ★ | `STRUCTURI.md` §3 · `structures/02_linked_list.py` · `problems/06.linked_list/` | scrii reverse și detectare de ciclu din memorie |
| E2.3a | Fast & Slow Pointers | ★ | `practice/04_fast_slow_pointers.py` · `TEHNICI.md` §3 | 04 → `N/N passed` |
| E2.3b | In-place Reversal | ★ | `practice/07_inplace_linked_list_reversal.py` · `TEHNICI.md` §6 | 07 → `N/N passed` |
| E2.4 | Merge Intervals | ★ | `practice/05_merge_intervals.py` · `TEHNICI.md` §4 | 05 → `N/N passed` |
| E2.5 | Cyclic Sort | ○ | `practice/06_cyclic_sort.py` · `TEHNICI.md` §5 | 06 → `N/N passed` |
| E2.6 | Prefix Sum | ★ | `TEHNICI.md` §2 (suma rulantă) — nu are fișier propriu | de ce primele `k` elemente se adună o singură dată |
| E2.7 | Sortare + comparator | ★ | `STRUCTURI.md` §1 | sortezi cu `key=` / `lambda` fără să te uiți |
| E2.8 | Matrix / grid 2D | ○ | `practice/22_matrix.py` · `TEHNICI.md` §21 | parcurgi o matrice pe linii/coloane/diagonale |

**Poarta etapei:** `03`, `04`, `05`, `06`, `07`, `09` → `N/N passed`, cu rescriere din memorie
a doua zi pentru `03` și `09` (cele mai frecvente la interviu).

---

## Etapa 3 — Arbori

| Nod | Concept | Prioritate | Material | Poarta |
|---|---|---|---|---|
| E3.1 | Tree BFS (level order) | ★ | `practice/10_tree_bfs.py` · `TEHNICI.md` §7 | 10 → `N/N passed` |
| E3.2 | Tree DFS (pre/in/post) | ★ | `practice/11_tree_dfs.py` · `TEHNICI.md` §8 | 11 → `N/N passed` |
| E3.3 | BST: validate, kth smallest, LCA | ★ | `problems/07.trees/` (`validate_bst`, `kth_smallest_element_in_bst`, `lowest_common_ancestor_bst`) | scrii din memorie `dfs(node, low, high)` pentru validate |
| E3.4 | Construcție & serializare | ○ | `problems/07.trees/` (`construct_binary_tree...`, `serialize_and_deserialize_bt`, `binary_tree_maximum_path_sum`) | — |

Prima structură cu adevărat recursivă. Aici se antrenează recursia de care are nevoie Etapa 4.

**Poarta etapei:** `10` și `11` → `N/N passed`; scrii din memorie o traversare DFS și una BFS.

---

## Etapa 4 — Pe arbori + recursie

| Nod | Concept | Prioritate | Material | Poarta |
|---|---|---|---|---|
| E4.1 | Tries | ★ | `practice/19_tries.py` · `TEHNICI.md` §18 · `STRUCTURI.md` §10 · `structures/09_trie.py` · `problems/08.tries/` | 19 → `N/N passed`; implementezi clasa `Trie` (`insert`/`search`/`startsWith`) din memorie |
| E4.2 | Backtracking (choose → explore → unchoose) | ★ | `practice/13_backtracking.py` · `TEHNICI.md` §10, §16 | 13 → `N/N passed` |
| E4.2a | Subsets / combinații | ★ | `problems/10.backtracking/combination_sum.py` | — |
| E4.2b | Permutări | ★ | `practice/13` (Permutations) | — |
| E4.2c | Pruning | ★ | `practice/13` (când tai ramura, când continui) | explici de ce tai, nu doar că tai |
| E4.2d | Backtracking pe grid | ○ | `problems/10.backtracking/word_search.py` | — |

⚠️ **Notă:** tries are acum fișier de practice (`practice/19_tries.py`); materialul de referință
rămâne în `problems/08.tries/` și `structures/09_trie.py`.

**Poarta etapei:** `13` și `19` → `N/N passed`; implementezi Trie din memorie.

---

## Etapa 5 — Nivel avansat

Ordinea internă e flexibilă. Singurele legături reale: Heap → Two Heaps, Graphs → Topo Sort /
Union Find, Heap → Advanced Graphs, 1-D DP → 2-D DP.

| Nod | Concept | Prioritate | Material | Poarta |
|---|---|---|---|---|
| E5.1 | Heap / Priority Queue | ★ | `practice/12_two_heaps.py` · `STRUCTURI.md` §7 · `structures/06_heap.py` | scrii push/pop cu `heapq` din memorie (inclusiv max-heap cu negativ) |
| E5.2 | Two Heaps | ★ | `practice/12` (Running Median) · `TEHNICI.md` §9 | 12 → `N/N passed` |
| E5.3 | Graphs BFS/DFS (grid, clone) | ★ | `practice/14_graph_bfs_dfs.py` · `STRUCTURI.md` §9 · `TEHNICI.md` §17 | 14 → `N/N passed` |
| E5.4 | Topological Sort (Kahn + DFS) | ★ | `practice/15_topological_sort.py` · `TEHNICI.md` §12 | 15 → `N/N passed` |
| E5.5 | Union Find (DSU) | ○ | `practice/16_union_find.py` · `TEHNICI.md` §13 · `functions/10_union_find.py` | 16 → `N/N passed` |
| E5.6 | Advanced Graphs: Dijkstra, Bellman-Ford, MST (Prim/Kruskal) | ○ | `practice/23_advanced_graphs.py` · `TEHNICI.md` §22 | scrii Dijkstra cu heap și un MST din memorie; `problems/12.advanced-graphs/` are doar Alien Dictionary (topo sort) |
| E5.7 | 1-D DP | ★ | `practice/17_dynamic_programming.py` · `TEHNICI.md` §14 · `problems/13.One-D-DP/` | House Robber din memorie |
| E5.8 | 2-D DP | ★ | `practice/17` · `problems/14.Two-D-DP/` | Unique Paths și LCS din memorie |
| E5.9 | Greedy | ★ | `practice/18_greedy.py` · `TEHNICI.md` §15 | 18 → `N/N passed` |

**Poarta etapei:** `12`, `14`, `15`, `16`, `17`, `18` → `N/N passed` (`23` e opțional și nu blochează etapa).

---

## Etapa 6 — După interviu / specializare

Nu blochează nimic. Sunt conceptele care apar în interviuri de nivel avansat, în competiții sau
când vrei să aprofundezi un domeniu. Materialul e acum **în repo**: exercițiile în
`practice/19`–`practice/29`, teoria în `TEHNICI.md` §18–§29, iar structurile avansate și în
`STRUCTURI.md` §11–§13, cu implementări în `structures/` și `functions/`. Doar subiectele de
competiție (E6.9) nu au fișier de practice — sunt enumerate în `TEHNICI.md` §29.

| Nod | Ce conține | Prioritate | Material |
|---|---|---|---|
| E6.1 | Design problems: LRU Cache (hash map + listă dublu înlănțuită), LFU, Min Stack, Implement Queue using Stacks | ○ | `practice/20_design.py` · `TEHNICI.md` §19 |
| E6.2 | Bit Manipulation: XOR tricks, `n & (n-1)`, numărare biți, măști | ○ | `practice/21_bit_manipulation.py` · `TEHNICI.md` §20 |
| E6.3 | Math & Geometry: rotire matrice, spirală, numere prime, geometrie de bază | ◇ | `practice/24_math_geometry.py` · `practice/22_matrix.py` · `TEHNICI.md` §23 |
| E6.4 | Structuri avansate: Segment Tree, Fenwick / Binary Indexed Tree, Sparse Table | ◇ | `practice/27_advanced_structures.py` · `STRUCTURI.md` §11–§13 · `structures/10`–`12` · `functions/11`–`13` · `TEHNICI.md` §26 |
| E6.5 | Tehnici avansate: sweep line, monotonic deque (Sliding Window Maximum), quickselect (Kth Largest), binary lifting (LCA), meet-in-the-middle | ◇ | `practice/28_advanced_techniques.py` · `TEHNICI.md` §27 |
| E6.6 | Algoritmi pe stringuri: KMP, Rabin-Karp, Z-function, Manacher, Aho-Corasick | ◇ | `practice/26_string_algorithms.py` · `TEHNICI.md` §25 |
| E6.7 | DP avansat: 0/1 knapsack, LIS, interval DP, bitmask DP, digit DP, DP pe arbore, state machine DP | ○ | `practice/25_advanced_dp.py` · `TEHNICI.md` §24 |
| E6.8 | Grafuri avansate: componente tare conexe (Tarjan/Kosaraju), punți și puncte de articulație, drum Euler, max flow, bipartite matching | ◇ | `practice/29_advanced_graphs_2.py` · `TEHNICI.md` §28 |
| E6.9 | Competiție: Mo's algorithm, convex hull trick, simulare, geometrie computațională | ◇ | `TEHNICI.md` §29 (fără fișier de practice) |

Ordinea recomandată dacă ajungi aici: **E6.1 → E6.2 → E6.7 → E6.4 → restul.** Design problems
(primul) sunt cele mai probabile la interviuri serioase, pentru că îți cer să combini structuri
învățate deja.

---

## Dependențe reale vs. ordine pedagogică

Ordinea e o ordine de **învățare**, nu o ierarhie matematică strictă.

| Legătură | Tip | De ce |
|---|---|---|
| Queue → Tree BFS, Graphs BFS | strictă | BFS fără coadă nu există |
| Linked List → Fast & Slow, In-place Reversal | strictă | tehnica nu are sens fără listă |
| Recursie (E3.2) → Tries, Backtracking | strictă | ambele sunt recursie |
| Trees → Tries | strictă | trie e un arbore |
| Graphs → Topological Sort, Union Find | strictă | — |
| Heap → Two Heaps, Advanced Graphs | strictă | — |
| 1-D DP → 2-D DP | strictă | a doua e prima cu o dimensiune în plus |
| Backtracking → DP | pedagogică | recursia de la backtracking e cea mai bună rampă spre DP |
| Fundamente → restul | pedagogică | Binary Search ar merge și singur, dar indecșii corecți se învață pe array/two pointers |
| Sortare (E2.7) → Merge Intervals, Greedy | practică | ambele presupun input sortat |
| Prefix Sum (E2.6) → Sliding Window (fixă) | practică | „intră unul, iese unul" e prefix sum rulant |

---

## Ritm realist

Cât durează Etapa 1 + Etapa 2? Depinde de cât timp ai pe zi, pentru că „stăpânit" nu înseamnă
o singură trecere.

**Volumul de lucru:**

| | Probleme | Timp prima trecere | Timp poarta (rescrieri) |
|---|---|---|---|
| Etapa 1 (`01`, `02`, `08`) | 9 | ~4 h | ~1 h |
| Etapa 2 (`03`, `04`, `05`, `06`, `07`, `09`) | 18 | ~9-10 h | ~2 h |
| Teorie + citit (`STRUCTURI`, `TEHNICI`) | — | ~2 h | — |
| **Total** | **27** | **~15-16 h** | **~3 h** |

30 min per problemă e media realistă la început (trace pe hârtie → scris → debug → verificat),
și nu scade până nu se așază tiparul.

**Cât înseamnă asta în zile:**

| Ritm | Ore/săptămână | Prima trecere | Stăpânit (cu poarta) |
|---|---|---|---|
| 45 min/zi (ritmul din `STUDY_PLAN.md`) | ~5 h | ~3 săptămâni | ~3.5 săptămâni |
| 1 h/zi | ~7 h | ~2 săptămâni | ~2.5 săptămâni |
| 2 h/zi | ~14 h | ~7-8 zile | ~10 zile |
| 3 h/zi | ~21 h | ~5 zile | ~7 zile |

**Răspunsul direct:** la 45 min/zi, nu — o săptămână nu ajunge pentru Etapa 1+2 la nivel de
stăpânire. La ~2 h/zi, da, dar e o săptămână plină și poarta de rescriere se termină în zilele
8-10. Vezi mai jos planul de 7 zile pentru ritmul de 2 h/zi.

### Plan de 7 zile (2 h/zi) — prima trecere prin Etapa 1 + 2

| Zi | Ce faci | Timp |
|---|---|---|
| 1 | `STRUCTURI.md` §1, §2, §6 → `practice/01` (3 probleme) | 2 h |
| 2 | `practice/02` (3) + recapitulare `01` din memorie | 2 h |
| 3 | `STRUCTURI.md` §4, §5 → `practice/08` (3) + coadă cu `deque` | 2 h |
| 4 | `TEHNICI.md` §2 → `practice/03` (3, cu trace pe hârtie la P1) | 2 h |
| 5 | `practice/09` (3) + `practice/04` (3) | 2 h |
| 6 | `practice/07` (3) + `practice/06` (3) | 2 h |
| 7 | `practice/05` (3) + recapitulare: rescrii 2-3 funcții din memorie | 2 h |

Zilele 8-10 (30-45 min fiecare): **poarta** — rescrei din memorie `01`, `02`, `08`, `03`, `09`,
`04`, `07`, `06`, `05`, și verifici că ai `N/N passed`.

**Dacă trebuie să comprimi**, nu tăia trace-ul pe hârtie și nici rescrierea din memorie (alea
sunt exact părțile care construiesc skill-ul). Taie din cuprins: mută `05` (Merge Intervals) și
`06` (Cyclic Sort) în Etapa 2 târzie sau în Etapa 5 — sunt ramuri independente, nu blochează
nimic din ce vine după.

---

## Cum folosești poarta

„Stăpânesc" nu înseamnă „am citit" și nici „am rezolvat o dată". Înseamnă trei lucruri:

1. `python3 practice/NN_<concept>.py` afișează **`N/N passed`**, fără să te uiți la soluție.
2. A doua zi rescrii funcțiile din memorie, pe o foaie, și se potrivesc.
3. Poți explica **de ce** e O(n) sau O(n log n), nu doar că a trecut.

Dacă oricare dintre cele trei pică, etapa nu e închisă.

```bash
cd practice && python3 03_sliding_window.py        # o etapă
cd practice && for f in *.py; do echo "== $f =="; python3 "$f"; done   # toate
```

Referințe: [`STUDY_PLAN.md`](./STUDY_PLAN.md) (ritm și metodă),
[`TEHNICI.md`](./TEHNICI.md) (tehnici), [`STRUCTURI.md`](./STRUCTURI.md) (structuri),
[`problems/`](./problems) (soluții de referință), [`PROBLEMS.md`](./PROBLEMS.md) (indexul problemelor).
