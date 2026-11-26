# Plan de studiu DSA — 2-3 luni

Scopul: să poți **descompune** o problemă nouă și să o **rezolvi** în timp de interviu
(15-25 min). Lucrurile de mai jos nu învață „mai multe probleme" — învață să **recunoști
tiparul** și să **scrii soluția din reflex**.

> Regula de aur: calitate > cantitate. 8-12 probleme bine înțelese pe un tipar
> valorează mai mult decât 50 de probleme rezolvate superficial.

---

## 1. Stratul de fundație (scrie-le din cap, fără să te uiți)

Înainte de tipare, trebuie să scrii fluent aceste lucruri. Dacă unul e găunos, tiparele
de deasupra cad.

| Categorie | Ce să știi fluent |
|---|---|
| Structuri | Array/String, Linked List, Stack, Queue, HashMap/HashSet, Heap (Priority Queue), Tree (BT/BST), Graph (adjacency list), Trie |
| Tehnici | Recursie + backtracking, Two pointers, Sliding window, Prefix sums, Binary search (incl. pe răspuns), Sorting (când ajută), DFS, BFS |
| Complexitate | Calculezi rapid O(timp) + O(memorie) și știi când e „acceptabil" |

**Test rapid:** scrie din cap `binary_search`, `dfs` pe tree, `bfs` cu level order,
`heap` (push/pop). Dacă te blochezi, exersează astea **înainte** de tipare.

---

## 2. Tiparele esențiale (acoperă ~90% din probleme)

Ordinea din tabel = ordinea în care le înveți (de la cele mai frecvente la cele mai rare).

| # | Tipar | Când apare | Ce faci |
|---|---|---|---|
| 1 | Two Pointers | array sortat / perechi / sumă | `left+right` sau `slow+fast` |
| 2 | Sliding Window | subarray/substring cu constrângere | window fixă sau variabilă + HashMap |
| 3 | Fast & Slow Pointers | ciclu în listă, middle | detectare ciclu, găsire middle |
| 4 | Merge Intervals | intervale care se suprapun | sort + merge |
| 5 | Cyclic Sort | numere 1..n / missing number | sort in-place cu swap |
| 6 | In-place Reversal of Linked List | reverse list / reverse k nodes | manipulare pointeri |
| 7 | Tree BFS (Level Order) | niveluri, shortest path în tree | queue |
| 8 | Tree DFS | path, diametru, validate BST | recursie sau stack (pre/in/post) |
| 9 | Two Heaps | median, top K din stream | max-heap + min-heap |
| 10 | Subsets / Combinations | toate submulțimile / combinații | backtracking |
| 11 | Modified Binary Search | array rotit, căutare pe răspuns | BS pe condiție, nu pe egalitate |
| 12 | Topological Sort | dependențe, ordinea cursurilor | Kahn sau DFS |
| 13 | Union Find (DSU) | componente conexe | path compression + union by rank |
| 14 | Dynamic Programming | optimizare / numărare / path-uri | 1D, 2D, knapsack, LCS, LIS |
| 15 | Greedy | alegere locală optimă | sort + alegere, interval scheduling |
| 16 | Backtracking | permutări, combinații, sudoku | choose → explore → unchoose |

**Prioritate de învățare (în ordine):**
1. Two Pointers + Sliding Window
2. Binary Search (incl. pe răspuns)
3. Tree DFS/BFS
4. Graph DFS/BFS + Topo Sort
5. Heap + Two Heaps
6. Backtracking
7. DP (1D → 2D)
8. Restul

După ce acestea sunt solide, tiparele avansate (opționale, pentru interviuri de nivel avansat sau
competiții) sunt în `TEHNICI.md` §18–§29, cu exerciții în `practice/19`–`practice/29`. Ordinea și
prioritatea lor sunt în [`LEARNING_TREE.md`](./LEARNING_TREE.md), Etapa 6. Singurul care merită
făcut mai devreme este Tries (`practice/19`), imediat după arbori.

---

## 3. Cum descompui o problemă (metoda care contează cel mai mult)

Aplică **mereu** acești pași, în ordine. Nu sări peste niciunul.

### Pasul 1 — Citește de 2 ori și identifică
- Ce e **inputul**? (array, string, tree, graph, linked list…)
- Ce **constrângeri** ai? (n ≤ 10⁵ → O(n log n) maxim; n ≤ 20 → 2ⁿ ok)
- Ce se **returnează** exact?

### Pasul 2 — Reformulează în cuvinte simple
„Trebuie să găsesc cel mai lung subarray cu sumă ≤ k" → Sliding Window.

### Pasul 3 — Caută tiparul
Întreabă-te în ordine:
- E subarray / substring? → Sliding Window sau Prefix sum
- E pereche / triplă? → Two Pointers
- E pe tree? → Tree DFS sau BFS
- Trebuie toate posibilitățile? → Backtracking / Subsets
- Trebuie max / min? → DP sau Greedy sau Binary Search pe răspuns
- E graf cu dependențe? → Topo Sort sau Union Find

### Pasul 4 — Exercițiu pe hârtie
Găsește un exemplu mic, rezolvă-l **manual**. Pașii pe care i-ai făcut tu = algoritmul.

### Pasul 5 — Scrie brut, apoi optimizează
Scrie întâi versiunea O(n²) (sau orice merge), apoi aplică tiparul ca să optimizezi.

### Pasul 6 — Edge cases din start
Golește array/listă/string, un singur element, duplicate, numere negative, ciclu,
valori extreme. Testează-le **înainte** să zici că ai terminat.

---

## 4. Cum exersezi eficient (nu „rezolvi multe")

1. **Un tipar → 8-12 probleme** (ușoare + medii). Folosește liste concentrate: Blind 75, NeetCode 150, LeetCode pe tag.
2. **A doua zi:** rescrie soluția din memorie. Asta bagă tiparul în reflex.
3. **Blocaj > 30-40 min:** citește soluția, înțelege tiparul, **închide**, rescrie singur. Nu copia!
4. **Jurnal scurt** — în `old/` sau lângă fișiere adaugă 1 linie:
   > „Problema X → Tipar Y → Ideea cheie Z".

---

## 5. Ritmul recomandat (25-45 min / zi, aproximativ 2 luni)

Poate părea puțin, dar consistența zilnică bate sesiunile lungi o dată pe săptămână.
Dacă ai mai mult timp, dublează zilele, nu lungi sesiunea peste 90 min.

| Săptămâni | Focus | Tipare | Probleme țintă |
|---|---|---|---|
| 1 | Arrays + Hashing | Two Pointers, Sliding Window | 12-15 ușoare-medii |
| 2 | Two Pointers + Sliding Window | — | 8-10 |
| 3 | Binary Search | Modified BS | 6-8 |
| 4 | Trees | Tree DFS + BFS | 10-12 |
| 5 | Stack + Linked List | Fast&Slow, Reversal | 6-8 |
| 6 | Heaps | Two Heaps | 4-6 |
| 7 | Graphs | DFS/BFS + Topo Sort | 8-10 |
| 8 | Backtracking | Subsets/Combinations | 6-8 |
| 9-10 | Dynamic Programming | 1D → 2D | 8-12 |
| 11-12 | Recapitulare + modele | toate | 2 zile de exercițiu mixt / live |

**Checkpoint la 6 săptămâni:** ar trebui să poți rezolva un „medium" necunoscut din
listele Blind 75 în 15-20 min.

---

## 6. Ordinea completă de studiu (în detaliu)

1. Arrays + Hashing + Two Pointers + Sliding Window
2. Stack + Linked List
3. Binary Search + Trees (DFS/BFS)
4. Heaps + Graphs (BFS/DFS + Topo)
5. Backtracking
6. Dynamic Programming (începe cu Climbing Stairs, House Robber, Knapsack, LCS)
7. Advanced (Trie, Union Find, Segment Tree — opțional): `practice/19`–`29`, `TEHNICI.md` §18–§29

---

## 7. Trucuri care contează la interviu

- **Spune tiparul cu voce tare** înainte de a scrie cod. Arată că descompui, nu doar „știu eu".
- **Complexitate:** numește O() la final — timp + spațiu.
- **Write brute → optimize.** Nu te grăbi spre soluția optimă; arată raționamentul.
- **Testează cu exemplul** dat + un edge case, manual (dry-run).
- **Cod curat:** nume clare, fără găuri de logică. Intervievezi logica, nu rapperi.

---

## 8. Notă despre `problems/old/` (variantele brute)

Folderul `problems/old/` conține primele tale încercări — multe au greșeli de sintaxă sau folosesc abordări naive (brute force).
Sunt utile ca **istoric** și ca exercițiu de „de ce era greșit?", **nu** ca forme de referință.
Pentru rezolvarea de referință folosește folderele categorisite din `problems/` (vezi `PROBLEMS.md`).

Dacă preferi, le putem arhiva într-un subfolder `problems/archive/` separat ca să nu încarce lista principală.

---

## 9. Fișierele de referință

- [`STRUCTURI.md`](./STRUCTURI.md) — toate structurile de date, cu explicație, complexitate și când le folosești.
- [`structures/`](./structures/README.md) — cod cu OOP: fiecare structură ca o clasă.
- [`functions/`](./functions/README.md) — cod fără OOP: aceleași structuri ca funcții (practic).
- [`TEHNICI.md`](./TEHNICI.md) — toate tehnicile/algoritmii, cu explicație, schelet de cod și când apar.
- [`practice/`](./practice/README.md) — exerciții: câte 3 probleme per concept (01–18, plus blocul avansat 19–29), enunțuri în engleză, de rezolvat singur.

Citește-le **înainte** de fiecare bloc de exerciții, apoi revino la ele când te blochezi.
