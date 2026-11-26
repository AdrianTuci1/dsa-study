# Structuri de date — referință cu explicație

Scopul acestui fișier: să știi, pentru fiecare structură de date, **ce este**, **operațiile**
și **complexitatea lor**, **când o folosești** și dificultățile tipice. E „foaia de lucru"
pe care o consulți înainte de un bloc de exerciții.

> Convenție de complexitate: `n` = numărul de elemente din structură. `O(1)` = instant,
> `O(n)` = liniar, `O(log n)` = logaritmic (împărțim la jumătate), `O(n log n)` = sortare.

> 💻 Fiecare structură are și o **implementare de la zero** în [`structures/`](./structures/README.md),
> cu exemplu rulabil. Fișierul de cod e indicat la finalul fiecărei secțiuni.

---

## 1. Arrays / Strings

**Ce este:** o colecție de elemente situate una după alta în memorie, accesate pozițional (index).

**Operații și complexitate (array):**
| Operație | Complexitate | Observație |
|---|---|---|
| Acces la index `a[i]` | O(1) | punctul forte |
| Căutare | O(n) | liniar; dacă e sortat → O(log n) cu BS |
| Adăugare la final | O(1) amortizat | (în Python, lista dinamiză) |
| Inserare / ștergere la mijloc | O(n) | trebuie mutate elementele după |
| Sortare | O(n log n) | `sorted()` / `.sort()` |

**Explicație cheie:** indexarea O(1) e superputerea — folosește-o ca să „sari" direct la o poziție.
Dezavantajul: inserarea/ștergerea la mijloc e costisitoare, fiindcă restul trebuie șifonat la stânga/dreapta.

**Când o folosești:** aproape orice problemă cu „array" sau „string". Pentru sistat cuvintele,
numără frecvențe cu un `dict`/`Counter` în loc să cauți în fiecare pas.

**De reținut (edge cases):** gol, un singur element, duplicate, negative, valori extreme.

---

## 2. Strings

**Ce este:** un array de caractere (în Python, imutabil).

**Operații de bază:** lungime `len(s)` O(1), acces `s[i]` O(1), concatenare (O(n)). Conversie
la listă `list(s)` ca să poți modifica, apoi `''.join(list)`.

**Explicație cheie:** stringurile sunt **imutabile** în Python — orice „modificare" creează un obiect
nou. De-aia, dacă construiești un rezultat caractere cu caractere, adună într-o listă și fă `join`
la final (mai eficient decât `+=` într-un loop).

**Tipare frecvente:** verificare anagramă (Counter), palindrom (two pointers), substrings
(sliding window), encoding/decoding.

---

## 3. Linked List

**Ce este:** o listă de noduri, unde fiecare nod ține o valoare și un pointer către următorul
(singly) sau și către anteriorul (doubly).

**Operații și complexitate:**
| Operație | Complexitate | Observație |
|---|---|---|
| Acces la index | O(n) | **nu** ai acces O(1) — trebuie să parcurgi |
| Inserare / ștergere la început | O(1) | avantajul față de array |
| Inserare / ștergere la poziție cunoscută | O(1) | dacă ai deja pointer |
| Căutare | O(n) | liniar |

**Explicație cheie:** nu ai indexare, doar „mers" de la head înainte. Tiparele clasice sunt:
**fast & slow pointers** (detecție ciclu, middle), **reverse**, **merge** a două liste.

**De reținut:**
- Folosește un **dummy node** (`dummy = ListNode(0); dummy.next = head;`) ca să eviți cazurile speciale de la head.
- La reverse, ții trei pointeri: `prev → curr → next`.

---

## 4. Stack

**Ce este:** structură care respectă LIFO (Last In, First Out — ultimul care intră e primul care iese).

**Operații și complexitate:**
| Operație | Complexitate |
|---|---|
| `push` (adaugă) | O(1) |
| `pop` (scoate) | O(1) |
| `peek` / `top` (uită-te) | O(1) |

**Explicație cheie:** gândește „cutie de cărți" — pui deasupra, iei deasupra. E perfect când trebuie să
memorezi **contextul** într-o ordine inversă.

**Când apare:** paranteze valide, evaluare de expresii, „nearest greater/smaller", traversări de
tree iterative (DFS), undo history.

---

## 5. Queue

**Ce este:** structură FIFO (First In, First Out — primul care intră e primul care iese).

**Operații și complexitate:**
| Operație | Complexitate |
|---|---|
| `enqueue` (adaugă la coadă) | O(1) |
| `dequeue` (scoate din coadă) | O(1) |
| `peek` (uită-te la front) | O(1) |

**Explicație cheie:** „coadă la magazin" — primul ajuns, primul servit. Baza pentru **BFS** (parcurgere
în lățime), unde mergem „nivel cu nivel". În Python folosește `collections.deque` (sau `deque`),
care are `append` și `popleft` ambele O(1).

---

## 6. HashMap / HashSet

**Ce este:** structura cheie-valoare (map) sau doar un set de chei unice.

**Operații și complexitate (medie):**
| Operație | HashMap | HashSet |
|---|---|---|
| Acces `map[key]` | O(1) | — |
| Inserare `map[key] = v` | O(1) | O(1) |
| Ștergere | O(1) | O(1) |
| `key in map` | O(1) | O(1) |

**Explicație cheie:** transformă căutarea O(n) în O(1) schimbând „căutăm în listă" cu
„căutăm cheia". E cel mai folosit accelerator de complexitate din toate problemele.

**Când apare:**
- **Two Sum** — cauți complementul `target - num` într-un map.
- **Numărare frecvențe** (`Counter` / `defaultdict(int)`).
- **Detecție duplicate** (`set`).
- **Sliding window / substrings** — memorezi ultima poziție a unui caracter.

**De reținut:** în Python `{}` = dict, `set()` = set. Un `defaultdict(list)` te scapă de verificarea
„există cheia?".

---

## 7. Heap / Priority Queue

**Ce este:** un arbore binari special (de obicei min-heap) care ține mereu cel mai mic (sau cel mai
mare) element pe poziția 0 (rădăcină). Nu garantează elementele sortate, doar „cel mai mic/mare primul".

**Operații și complexitate:**
| Operație | Complexitate | Observație |
|---|---|---|
| `push` (inserare) | O(log n) | — |
| `pop` (scoate extremul) | O(log n) | — |
| `peek` (uită-te la rădăcină) | O(1) | — |
| Construire din listă | O(n) | `heapify` |

**Explicație cheie:** când trebuie să iei **repetat** elementul minim sau maxim, heap-ul e O(log n)
per operație, față de O(n) la căutare liniară în listă.

În Python, `heapq` face **min-heap** implicit. Pentru max-heap, pui valorile negative
(`heappush(h, -x)`); la scoatere iei `-heappop(h)`.

**Când apare:** „kth largest/smallest", merge k liste sortate, stream la care ceri mediană (two heaps),
top k frecvente.

---

## 8. Tree (Binary Tree / BST)

**Ce este:** structură ierarhică de noduri, fiecare cu maxim 2 copii (left, right). Un **BST** are
proprietatea: tot ce e în subarborele stâng < nod < tot ce e în subarborele drept (valori distincte).

**Tipuri de traversare și complexitate:**
| Traversare | Ordine | Utilizare |
|---|---|---|
| Pre-order | nod → left → right | serialize, copy |
| In-order | left → nod → right | pe BST dă **ordine sortată** |
| Post-order | left → right → nod | ștergere, path sum |
| Level-order (BFS) | nivel cu nivel | shortest path, right side view |

**Operații (BST, medie):** `search` O(log n), `insert` O(log n), `delete` O(log n) — dar pe un
BST dezechilibrat devin O(n).

**Explicație cheie:** în general, pe tree se spune „recurezi": rezolvi problema pe subarbore,
apoi combinezi rezultatele (post-order), sau citești nodul curent înainte (pre-order). La niveluri
folosești BFS cu o coadă (queue).

---

## 9. Graph (adjacency list)

**Ce este:** un set de noduri (vertices) și muchii (edges) între ele, reprezentat de obicei ca
`{ node: [vecini] }` — o mapă de la nod la lista vecinilor săi.

**Complexitate la parcurgere:**
| Parcurgere | Complexitate | Coadă? |
|---|---|---|
| DFS (stivă recursivă) | O(V + E) | — |
| BFS (coadă) | O(V + E) | da |

unde `V` = număr de noduri, `E` = număr de muchii.

**Explicație cheie:** pentru grafuri, cheia e alegerea **DFS vs BFS**. BFS dă cel mai scurt drum
în graf neponderat; DFS citește „cât de adânc se poate", bun pentru component conexe, cicluri,
detecții topologice.

**Când apare:** numărare de insule, connected components, cycle detection, topolog ordin (dependențe),
shortest path în grid.

---

## 10. Trie (Prefix Tree)

**Ce este:** un arbore în care fiecare nod reprezintă un prefix; muchiile sunt caractere.
Permite verificări de prefix foarte rapide.

**Complexitate:**
| Operație | Complexitate |
|---|---|
| Insert | O(`L`) |
| Search | O(`L`) |
| Prefix exists | O(`L`) |

unde `L` = lungimea cuvântului.

**Explicație cheie:** gândește-l ca un „dicționar de autocomplete". Fiecare nod are un `children`
(dict de la caracter → nod) și un flag `is_word` la final de cuvânt.

**Când apare:** căutare de cuvinte cu wildcard (`Word Search II`, `Design Add and Search Words`),
prefix matching, autocomplete.

---

## 11. Segment Tree

**Ce este:** un arbore binar construit peste array: fiecare nod ține agregatul (aici **suma**) unei
porțiuni `[lo, hi]`, frunzele sunt elementele, iar un nod intern = suma celor doi copii.
Se reprezintă ca listă de `4 * n` noduri, indexate de la 1 (`copii(i) = 2i, 2i+1`).

**Complexitate:**
| Operație | Complexitate |
|---|---|
| Build | O(n) |
| Update pe poziție | O(log n) |
| Query pe interval | O(log n) |

unde `n` = numărul de elemente.

**Explicație cheie:** orice interval se descompune în O(log n) noduri ale arborelui, iar la o
modificare pe poziție recalculezi doar drumul frunză → rădăcină. E structura **generală** pentru
„query pe interval + update": merge la sumă, min/max, gcd, iar cu *lazy propagation* și la update
pe interval (nu doar pe poziție).

**Când apare:** sumă/min/max pe subarray-uri amestecate cu modificări (`Range Sum Query - Mutable`,
`Count of Smaller Numbers After Self`), sau când Fenwick nu e suficient (min/max, update pe interval).

**Exemplu de cod scurt:**
```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:                            # frunză = un element
            self.tree[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, i, value):                 # nums[i] = value, O(log n)
        self._update(1, 0, self.n - 1, i, value)

    def _update(self, node, lo, hi, i, value):
        if lo == hi:
            self.tree[node] = value
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node, lo, mid, i, value)
        else:
            self._update(2 * node + 1, mid + 1, hi, i, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, left, right):               # suma pe [left, right], O(log n)
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, lo, hi, left, right):
        if right < lo or hi < left:
            return 0                            # disjunct -> element neutru
        if left <= lo and hi <= right:
            return self.tree[node]              # complet acoperit
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, left, right)
                + self._query(2 * node + 1, mid + 1, hi, left, right))
```

---

## 12. Fenwick / BIT (Binary Indexed Tree)

**Ce este:** un array de prefixe „cu superputeri": `tree[i]` ține suma unei porțiuni de lungime
`i & (-i)` care se termină pe poziția `i`. Nu e un arbore explicit — relația părinte/copil e dată
de biții celui mai puțin semnificativ.

**Complexitate:**
| Operație | Complexitate |
|---|---|
| Build | O(n) |
| Add pe poziție (`nums[i] += delta`) | O(log n) |
| Prefix sum (`nums[0..i]`) | O(log n) |
| Range sum (`nums[left..right]`) | O(log n) |

**Explicație cheie:** `i & (-i)` izolează ultimul bit de 1 → sari din prefix în prefix logaritmic:
la `add` urci cu `i += i & (-i)`, la `prefix_sum` cobori cu `i -= i & (-i)`. Intern e **1-based**
(`tree` are `n + 1` poziții, `tree[0]` e umplutură), dar API-ul de sus rămâne **0-based**, ca
`nums`: `i = index + 1` doar la intrarea în structură. Mai puțin cod și constantă mai mică decât
segment tree-ul, dar doar pentru operații **inversabile** (sumă, xor) — nu merge la min/max.

**Când apare:** prefix sums pe date care se modifică, numărare de inversiuni (`Count of Smaller
Numbers After Self`), statistici de ordine, `Range Sum Query - Mutable`.

**Exemplu de cod scurt:**
```python
def bit_build(nums):                    # O(n), nu n * O(log n)
    n = len(nums)
    tree = [0] + list(nums)
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            tree[j] += tree[i]
    return tree

def bit_add(tree, index, delta):        # nums[index] += delta, O(log n)
    i = index + 1                       # API 0-based -> intern 1-based
    while i < len(tree):
        tree[i] += delta
        i += i & -i                     # urc spre părinți

def bit_prefix(tree, index):            # suma nums[0..index], O(log n)
    i, total = index + 1, 0
    while i > 0:
        total += tree[i]
        i -= i & -i                     # cobor spre 0
    return total

def bit_range(tree, left, right):       # suma nums[left..right]
    return bit_prefix(tree, right) - bit_prefix(tree, left - 1)
```

---

## 13. Sparse Table

**Ce este:** un tabel precalculat pentru „minim pe interval" pe un array care **nu se modifică
niciodată**: `table[k][i]` = minimul ferestrei de lungime `2^k` care începe pe poziția `i`.

**Complexitate:**
| Operație | Complexitate |
|---|---|
| Build | O(n log n) timp, O(n log n) spațiu |
| Query (`min` pe `[left, right]`) | O(1) |
| Update | **nu există** |

**Explicație cheie:** un interval de lungime `L` se acoperă cu **două** ferestre de lungime `2^k`,
unde `k = floor(log2(L))`: una lipită de capătul din stânga, una de capătul din dreapta.
`log` se precalculează, deci query-ul nu are nicio buclă. Ferestrele se pot suprapune — de aceea
merge doar pentru operații **idempotente** (`min`, `max`, `gcd`), nu pentru sumă.

**Când apare:** RMQ static (mii de întrebări „minimul dintre `l` și `r`" pe un array neschimbat),
LCA cu tur Euler, orice preprocesare care cumpără O(1) per query cu O(n log n) memorie.

**Exemplu de cod scurt:**
```python
def sparse_build(nums):
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

def sparse_query(table, log, left, right):   # minim pe [left, right], O(1)
    k = log[right - left + 1]
    row = table[k]
    return min(row[left], row[right - (1 << k) + 1])   # două ferestre lipite de capete
```

---

## Tabel rezumativ — structuri vs complexitate vs folosire

| Structură | Esență | Întrebarea-pereche | Complexitate clasică |
|---|---|---|---|
| Array/String | acces index O(1) | „am nevoie de elementul de pe poziția i?" | acces O(1) |
| Linked List | înserare la început O(1) | „mut mult la început?" | acces O(n) |
| Stack | LIFO | „am nevoie de reverse/context?" | push/pop O(1) |
| Queue | FIFO | „am nevoie de BFS / nivel cu nivel?" | enqueue/dequeue O(1) |
| HashMap/Set | cheie → valoare | „trebuie să caut rapid o cheie?" | get/set O(1) |
| Heap | excelent la min/max | „iau repetat minimul/maximul?" | push/pop O(log n) |
| Tree | ierarhie, recursie | „problema se împarte în sub-probleme?" | DFS/BFS O(n) |
| Graph | noduri + muchii | „am conexiuni între entități?" | O(V+E) |
| Trie | prefixe | „caut cuvinte după prefix?" | O(L) |
| Segment Tree | agregat pe porțiuni, arbore | „query pe interval **și** update-uri?" | update/query O(log n) |
| Fenwick / BIT | prefixe pe biți | „prefix sums cu update-uri?" | add/prefix O(log n) |
| Sparse Table | ferestre de puteri ale lui 2 | „multe query-uri, zero update-uri?" | query O(1), fără update |
