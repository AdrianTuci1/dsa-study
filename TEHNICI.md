# Tehnici & algoritmi — referință cu explicație

Scopul: pentru fiecare tipar, să știi **când apare**, **ideea-cheie** și **scheletul de cod**,
ca să recunoști tiparul și să scrii soluția din reflex.

> Ordinea de mai jos e o proiectură de învățare (nu de importanță absolută): începe de sus.

---

## 1. Two Pointers

**Când apare:** array/string, trebuie perechi, triplete sau să compari din două capete. Tinde să
apară pe listă **sortată** sau când vrei să eviți o buclă dublă O(n²).

**Ideea-cheie:** ții doi indecși (`left`, `right`) și îi apropii/care unul spre altul, economisind
muncă. Uns aranjat: `left+right` pentru sumă „prea mică → mută left", „prea mare → mută right".

**Schelet:**
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

**Exemple:** Valid Palindrome, Container With Most Water, 3Sum.

---

## 2. Sliding Window

**Când apare:** subarray/substring cu anumită proprietate — lungime maximă/minimă, sumă țintă,
caractere unice, frecvență. Trebuie să iei toate ferestrele dar eficient.

**Ideea-cheie:** menții o **fereastră** `[left, right]` (indecși) și o extinzi cu `right`; când
constrângerea e încălcată, micșorezi din `left`. Evită recalcularea de la zero la fiecare pas.

**Schelet (fereastră variabilă):**
```python
def length_of_longest_substring(s):
    seen = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in seen:      # încălcată → micșorez din stânga
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Exemple:** Longest Substring Without Repeating, Minimum Window Substring, Best Time to Buy and Sell.

---

## 3. Fast & Slow Pointers (tortoise & hare)

**Când apare:** linked list — detecție de ciclu, găsirea mijlocului, găsirea nodului de început al ciclului.

**Ideea-cheie:** un pointer merge cu 1 pas, altul cu 2. Dacă se întâlnesc → există ciclu.
Pentru mijloc: când `fast` ajunge la final, `slow` e la mijloc.

**Schelet:**
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Exemple:** Linked List Cycle, Middle of the Linked List, Find the Duplicate Number.

---

## 4. Merge Intervals

**Când apare:** listă de intervale `[start, end]`; trebuie să le unești (suprapunere), să găsești
intersecții sau intervale libere.

**Ideea-cheie:** **sortează după start**, apoi mergi prin listă. Dacă intervalul curent
`start <= end_curent` → suprapunere, extinzi `end`; altfel închizi intervalul și începi unul nou.

**Schelet:**
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])
    return result
```

**Exemple:** Merge Intervals, Insert Interval, Meeting Rooms.

---

## 5. Cyclic Sort

**Când apare:** valori de la `1` la `n`, sau într-un array indexat `0..n` unde chestia „corectă"
la index `i` ar fi valoarea cunoscută. Missing number, duplicate number.

**Ideea-cheie:** mută fiecare element în poziția lui „corectă" prin swap, apoi scanezi. Fiecare
element se plasează în O(1) o dată → total O(n).

**Schelet:**
```python
def find_duplicate(nums):            # valorile 1..n, array lungime n+1
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]
```

**Exemple:** Find the Missing Number, Find All Duplicates in an Array.

---

## 6. In-place Reversal of Linked List

**Când apare:** reverse list, reverse în grupuri de k, palindrom pe linked list.

**Ideea-cheie:** folosești 3 pointeri `prev, curr, next` și răsucești legăturile una câte una.
Fără memorie extra (spațiu O(1)).

**Schelet:**
```python
def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
```

**Exemple:** Reverse Linked List, Reverse Nodes in k-Group, Palindrome Linked List.

---

## 7. Tree BFS (Level Order Traversal)

**Când apare:** „nivel cu nivel", shortest path în tree, right side view, zigzag.

**Ideea-cheie:** o **coadă** (queue). La fiecare iterație, procesezi nodurile aflate în coadă,
împingi copiii lor, iar fiecare „val" = un nivel.

**Schelet:**
```python
from collections import deque
def level_order(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result
```

**Exemple:** Binary Tree Level Order Traversal, Binary Tree Right Side View.

---

## 8. Tree DFS

**Când apare:** path, sum, diametru, validate BST, lowest common ancestor, toate problemele
de „recursie pe subarbore".

**Ideea-cheie:** alegi ordinea (pre/in/post). Pentru probleme care cer un „rezultat agregat"
dintr-un subarbore (sumă, adâncime, path), folosești **post-order** — aduni rezultatele copiilor,
apoi combini la nodul curent. Multe se rezolvă cu o funcție recursivă care returnează informația
de care ai nevoie în sus.

**Schelet (max depth):**
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Exemple:** Maximum Depth, Diameter of Binary Tree, Validate BST, Binary Tree Maximum Path Sum.

---

## 9. Two Heaps

**Când apare:** mediană dintr-un stream, top k elemente, „cel mai mare din jumătatea mică" +
„cel mai mic din jumătatea mare". De obicei vrei să accesezi ambele extreme dintr-o colecție.

**Ideea-cheie:** un **max-heap** pentru jumătatea inferioară, un **min-heap** pentru cea superioară.
Ții jumătățile echilibrate (±1). Mediana = topul unuia dintre heap-uri (sau media celor două).

**Schelet:**
```python
import heapq
class MedianFinder:
    def __init__(self):
        self.max_h = []   # jumătatea inferioară (valori negative)
        self.min_h = []   # jumătatea superioară

    def addNum(self, num):
        heapq.heappush(self.max_h, -num)
        heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
        if len(self.max_h) < len(self.min_h):
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))

    def findMedian(self):
        if len(self.max_h) > len(self.min_h):
            return -self.max_h[0]
        return (-self.max_h[0] + self.min_h[0]) / 2
```

**Exemple:** Find Median from Data Stream.

---

## 10. Subsets / Combinations (Backtracking)

**Când apare:** „toate submulțimile", „toate combinațiile", „toate permutările" — trebuie **toate**
soluțiile posibile, nu una. Problemele tipice: subsets, combination sum, permute, sudoku, word search.

**Ideea-cheie:** `choose → explore → unchoose`. La fiecare pas alegi un candidat, îl adaugi la
soluția curentă, recurezi, apoi îl scoți (backtrack). Folosești un `index`/„start" ca să eviți
submulțimile duplicate și să nu repeți combinații.

**Schelet (subsets):**
```python
def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res
```

**Exemple:** Subsets, Combination Sum, Permutations, Word Search.

---

## 11. Modified Binary Search

**Când apare:** căutare pe array rotit, căutare pe răspuns („găsește minimul care îndeplinește
condiția"), căutare pe valori monotone. Nu cauți neapărat egalitate — cauți **prima/ultima poziție
care respectă o condiție**.

**Ideea-cheie:** standardul `left...right` + `mid`, dar condiția de mutare nu e `nums[mid] == target`,
ci o **predicat** care decide în ce jumătate mergi. La array rotit, identifici care jumătate e sortată.

**Schelet (căutare pe răspuns):**
```python
def min_fulfilling(lo, hi, good):
    while lo < hi:
        mid = (lo + hi) // 2
        if good(mid):
            hi = mid          # căutăm prima poziție care îndeplinește
        else:
            lo = mid + 1
    return lo
```

**Exemple:** Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, Koko Eating Bananas.

---

## 12. Topological Sort

**Când apare:** dependențe / ordinare — „ordinea cursurilor", „timp de executare cu task-uri
dependente", detectarea ciclului într-un graf orientat **acelic**.

**Ideea-cheie (Kahn):** calculezi gradul de intrare pentru fiecare nod. Pune în coadă toate
nodurile cu grad 0 (fără dependențe), apoi scoți unul, decrementezi gradul vecinilor; când un
vecin ajunge la 0, îl pui în coadă. Dacă pui în coadă `n` noduri → ordinul există; altfel → ciclu.

**Schelet (Kahn):**
```python
from collections import deque, defaultdict
def topo_sort(n, edges):
    indeg = [0] * n
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == n else []   # [] => există ciclu
```

**Exemple:** Course Schedule, Alien Dictionary.

---

## 13. Union Find / Disjoint Set Union (DSU)

**Când apare:** componente conexe într-un graf neorientat, „întrebări 'sunt în aceeași grupare?'",
validare că un graf e copac (un ciclu = muchie care unește două noduri deja în aceeași grupare).

**Ideea-cheie:** fiecare nod are un „părinte". `find(x)` urcă până la rădăcină (cu **path
compression**); `union(a, b)` leagă două grupări (cu **union by rank**). Complexitate aproape O(1)
amortizat.

**Schelet:**
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

**Exemple:** Number of Connected Components, Graph Valid Tree, Network Delay Time.

---

## 14. Dynamic Programming

**Când apare:** optimizare (max/min), numărare de căi/soluții, subprobleme care se repetă.
Exemplul clasic: Fibonacci, Climbing Stairs, House Robber, Knapsack, LCS, LIS.

**Ideea-cheie:** găsești **subproblemele** suprapuse, definiți un `dp[i]` = răspunsul pentru primele
`i` elemente, și o **tranziție** `dp[i] = f(dp[i-1], dp[i-2], ...)`. Poți merge **bottom-up**
(iterativ, de la cazul de bază) — cel mai curat.

**Schelet (1D, Fibonacci):**
```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

**Schelet (2D, LCS):**
```python
def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

**Exemple:** Climbing Stairs, House Robber (I/II), Unique Paths, LCS, Maximum Product Subarray.

---

## 15. Greedy

**Când apare:** alegere locală optimă care duce la optimul global. „Sortare + alegere". Interval
scheduling (maxim număr de activități), minim/maximizare cu schimbare, jump game.

**Ideea-cheie:** la fiecare pas alegi **local** ce pare cel mai bun și speri/nu-ți trebuie backtracking.
Greedy e mai rapid (O(n log n) de obicei), dar trebuie să **justifici** că alegerea locală e corectă
global. Dacă nu e garantată → DP.

**Exemple:** Merge Intervals, Non-overlapping Intervals, Jump Game, Gas Station.

---

## 16. Backtracking

**Când apare:** toate soluțiile posibile într-un spațiu de căutare, constrânse crescător. Permutări,
combinații, sudoku, N-Queens, word search.

**Ideea-cheie:** fă alegere → verifică dacă merge → recurge → **desfă-o** (unchoose). E o DFS pe
„arborele de decizii". Spațiu O(n!) / O(2ⁿ) — deci input mic (n ≤ 20).

**Schelet:**
```python
def permute(nums):
    res = []
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return res
```

**Exemple:** Permutations, Combination Sum, Word Search, N-Queens.

---

## 17. BFS / DFS (pe graf)

**Când apare:** parcurgere de graf, component conexe, cycle detection, shortest path în grid
(BFS), ordonare (DFS + stack).

**Ideea-cheie:**
- **BFS** = coadă → explorezi „nivel cu nivel"; găsește **cel mai scurt** drum în graf neponderat.
- **DFS** = recursie/stivă → explorezi „cât de adânci" mergi; bun pentru component conexe și
  back-tracking.

Folosește un `visited` set (sau grid modificat) ca să nu te buclеzi.

---

## 18. Trie (arbore de prefixe)

**Când apare:** enunțul cere căutare după **prefix** (autocomplete, `startsWith`), potrivirea de
cuvinte cu wildcard `'.'`, sau „care cuvinte din dicționar apar într-un grid". Semnalul clar:
„există vreun cuvânt care începe cu...?" — hash map-ul nu te ajută aici, trie-ul da.

**Ideea-cheie:** fiecare nod ține un dict `children` (caracter → nod) și un flag `is_word`.
Inserarea și căutarea coboară caracter cu caracter: O(`L`), unde `L` = lungimea cuvântului,
indiferent câte cuvinte sunt stocate. Prefixele comune sunt partajate („car" nu se duplică în
„care" și „cart"), deci spațiu O(total caractere). Hash map-ul răspunde O(1) la un cuvânt exact,
dar la un prefix ar trebui să verifice toate cheile (O(n·`L`)); trie-ul răspunde O(`L`).

**Schelet:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}       # caracter -> TrieNode
        self.is_word = False     # un cuvant se termina aici


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())   # creeaza nodul daca lipseste
        node.is_word = True

    def _walk(self, s):          # coboara pe text; None daca drumul nu exista
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):      # cuvant intreg
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):   # doar prefix
        return self._walk(prefix) is not None


# wildcard: la '.' trebuie sa ramifici pe toti copiii
def search_wildcard(root, pattern):
    def dfs(node, i):
        if i == len(pattern):
            return node.is_word
        if pattern[i] == ".":
            return any(dfs(child, i + 1) for child in node.children.values())
        nxt = node.children.get(pattern[i])
        return nxt is not None and dfs(nxt, i + 1)
    return dfs(root, 0)
```

**Exemple:** Implement Trie, Design Add and Search Words, Word Search II, Replace Words,
Search Suggestions System.

**Capcane:**
- `search("app")` e `False` dacă s-a inserat doar „apple": coborârea reușește, dar `is_word` e
  `False`. De asta ai nevoie de flag separat, nu doar de existența nodului.
- Wildcard-ul `'.'` nu înseamnă „sari un caracter" pe un singur drum: la `'.'` se ramifică pe
  **toți** copiii (DFS recursiv), altfel ratezi potrivirile.
- Word Search II nu se rezolvă cu trie singur: pui cuvintele în trie, apoi faci backtracking pe
  grid (fiecare celulă poate fi start, marchezi celula folosită și o eliberezi la întoarcere) și te
  oprești imediat când prefixul curent nu mai există în trie. Fără trie, cauți fiecare cuvânt
  separat din fiecare celulă → prea lent.
- La Word Search II, dacă nu marchezi celula, poți refolosi aceeași literă în același cuvânt și
  raportezi potriviri false (ex.: „abcb" pe board-ul `[[a,b],[c,d]]`).

---

## 19. Design problems (LRU, Min Stack, coadă din două stive)

**Când apare:** enunțul zice „proiectează o structură de date" și îți dă lista de operații și
complexitatea cerută, de obicei O(1) per operație — LRU Cache, Min Stack, Implement Queue using
Stacks, Insert Delete GetRandom O(1), Design Twitter.

**Ideea-cheie:** nu inventezi nimic nou, ci **combini** structuri deja știute ca să obții
complexitatea cerută: hash map + listă dublu înlănțuită (LRU), stivă + stivă de minime paralele
(Min Stack), două stive cu transfer rar (coadă). De asta apar des la interviuri — verifică dacă
stăpânești primitivele, nu dacă știi un algoritm exotic.

**Schelet (LRU: hash map + listă dublu înlănțuită, O(1) per operație):**
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()      # cheie -> valoare, cel mai recent folosit la final

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)     # get reusit = devine cel mai recent folosit
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  # update: nu schimba dimensiunea, dar reinnoieste recenta
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)   # evacueaza LRU (primul intrat)
```

**Schelet (Min Stack: stiva de valori + stiva de minime paralele):**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []                  # mins[i] = minimul primelor i+1 valori

    def push(self, val):
        self.stack.append(val)
        self.mins.append(val if not self.mins else min(val, self.mins[-1]))

    def pop(self):
        self.mins.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]
```

**Schelet (coadă din două stive, cost amortizat O(1)):**
```python
class MyQueue:
    def __init__(self):
        self.inbox = []      # aici intra push
        self.outbox = []     # de aici iese pop / peek

    def push(self, x):
        self.inbox.append(x)

    def _move(self):         # transfera doar cand outbox e gol
        while self.inbox:
            self.outbox.append(self.inbox.pop())

    def pop(self):
        if not self.outbox:
            self._move()
        return self.outbox.pop()

    def peek(self):
        if not self.outbox:
            self._move()
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox
```

**Exemple:** LRU Cache, Min Stack, Implement Queue using Stacks, Insert Delete GetRandom O(1).

**Capcane:**
- LRU: `dict` simplu nu ține ordinea; ai nevoie de `OrderedDict` cu `move_to_end` sau de lista
  dublu înlănțuită scrisă de tine. `list.pop(0)` (sau căutarea LRU-ului prin listă) dă O(n).
- LRU: `put` pe o cheie existentă **nu** mărește dimensiunea, dar trebuie să reînnoiască recența —
  altfel evacuezi cheia greșită la următorul `put`.
- Min Stack: dacă ții minimul într-o singură variabilă, după `pop` nu mai știi care era minimul
  dinainte — de asta ții un minim per nivel. În varianta care urcă în stiva de minime doar când
  valoarea scade sau e egală, condiția e `<=`, nu `<`, altfel duplicatele te păcălesc la `pop`.
- Coada din două stive: transferă doar când `outbox` e gol — fiecare element se mută cel mult o
  dată, deci O(1) amortizat. Dacă re-echilibrezi stivele la fiecare operație, ajungi la O(n) per
  operație în loc de amortizat.

---

## 20. Bit Manipulation

**Când apare:** cauți un element care nu are pereche, numeri biți, inversezi biți, lucrezi cu
subset-uri ca mască de biți sau vrei constant space / operații O(1) în loc de structuri auxiliare.
De obicei enunțul spune „O(1) extra space" sau „fără hash map".

**Ideea-cheie:** XOR anulează perechile — `a ^ a == 0`, `a ^ 0 == a`, e comutativ și asociativ,
deci `x ^= fiecare element` lasă exact elementul fără pereche. `n & (n - 1)` **șterge cel mai puțin
semnificativ bit de 1**, deci numărul de iterații până la 0 = numărul de biți de 1 (Hamming weight).
Shift + mască: `n >> i & 1` citește bitul `i`, `1 << i` construiește masca, `|` pune un bit, `& ~mască`
îl șterge.

**Schelet:**
```python
def single_number(nums):
    x = 0
    for v in nums:          # perechile se anulează: a ^ a == 0
        x ^= v
    return x

def hamming_weight(n):
    count = 0
    while n:                # n & (n - 1) șterge ultimul bit de 1
        n &= n - 1
        count += 1
    return count

def reverse_bits(n):
    out = 0
    for _ in range(32):     # fix 32 de biți
        out = (out << 1) | (n & 1)
        n >>= 1
    return out

def get_bit(n, i):
    return (n >> i) & 1     # al i-lea bit, indexat de la LSB
```

**Exemple:** Single Number, Number of 1 Bits, Reverse Bits, Counting Bits, Subsets (bitmask).

**Capcane:** în Python int-urile au **precizie arbitrară**, deci nu există overflow pe 32 de biți și
`~n == -n - 1`; numerele negative sunt în complement față de doi cu semn infinit (biți de 1 la
infinit), deci `n >> i` pe numere negative rămâne negativ. Când problema cere 32 de biți, aplică
masca: `n & 0xFFFFFFFF` (utile după shiftări pe valori negative și când compari cu constante pe
32 de biți). Nu te baza pe exact 32 de biți în buclele `while n` (poți citi biți „în plus"). Și
`bin(n).count("1")` rezolvă, dar la interviu se cere metoda pe biți.

---

---

## 21. Matrice / Grid 2D

**Când apare:** parcurgere în spirală, rotire de imagine, marcare de linii și coloane, sau orice
problemă cu `matrix[i][j]`: drumuri în grilă, insule, shortest path pe grid. Practic un grid e un
**graf implicit** — fiecare celulă are muchii către vecinii `(r ± 1, c)` și `(r, c ± 1)`.

**Ideea-cheie:** ții patru granițe — `top, bottom, left, right` — și le strângi după fiecare tură
(sus →, dreapta ↓, jos ←, stânga ↑) pentru spirală. Pentru rotația 90° în sens orar: **transpui**
(`matrix[i][j] <-> matrix[j][i]`, doar deasupra diagonalei) apoi **oglindești fiecare linie** —
in-place, O(1) spațiu extra. Pentru „set zeroes": folosești **prima linie și prima coloană ca
markeri** (reții separat dacă ele însele trebuie zeroizate), ca să nu aloci O(m·n). Pentru matrici =
liste de liste, fiecare linie e o referință: copiază cu `[row[:] for row in matrix]`.

**Schelet:**
```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:         # poate fi și [] și [[]]
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    out = []
    while top <= bottom and left <= right:
        for c in range(left, right + 1):    # sus, spre dreapta
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):    # jos, în jos
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:                   # jos, spre stânga
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:                   # stânga, în sus
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1
    return out

def rotate(matrix):                         # 90° orar, in-place
    n = len(matrix)
    for i in range(n):                      # transpunere
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:                      # oglindire pe orizontală
        row.reverse()

def set_zeroes(matrix):                     # in-place, cu markeri
    if not matrix or not matrix[0]:
        return
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))
    for r in range(1, rows):                # linia/coloana 0 = markeri
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = matrix[0][c] = 0
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
```

**Exemple:** Spiral Matrix, Rotate Image, Set Matrix Zeroes, Number of Islands, Unique Paths.

**Capcane:** fără verificările `if top <= bottom` / `if left <= right` înainte de tururile de jos și
de stânga, matricele cu o singură linie sau o singură coloană repetă elemente. Cazurile limită sunt
`[]`, `[[]]`, `[[x]]` (1x1), toate zerourile și numerele negative. La problemele „in-place" nu aloca
o matrice nouă și nu returna nimic (funcția modifică argumentul) — iar `[row] * n` copiază doar
referințe, deci nu e o copie reală. Complexitatea e O(m·n) timp la toate trei; spațiu extra O(1)
pentru rotație și set-zeroes, O(1) în afară de lista rezultat pentru spirală.

---

---

## 22. Grafuri avansate I (Dijkstra, Bellman-Ford, MST)

### 22.1 Dijkstra cu heap

**Când apare:** cel mai scurt drum într-un graf **cu ponderi** (drum minim, „network delay",
„cheapest price" fără limită de opriri, „path with minimum effort"). Merge pe graf orientat sau
neorientat, cu o singură sursă.

**Ideea-cheie:** greedy + heap. Distanța minimă a nodului neextras încă nu se mai poate îmbunătăți
(asta e exact motivul pentru care ponderile trebuie să fie **>= 0**). Extragi nodul cu distanța
minimă, apoi **relaxezi** muchiile lui: dacă `dist[u] + w < dist[v]`, actualizezi și bagi în heap.
Cu heap: `O((V + E) log V)`; fără heap (scanare liniară): `O(V²)` — mai bun doar pe grafuri foarte dense.

**Schelet:**
```python
import heapq

def dijkstra(n, adj, start):              # adj[u] = [(v, w)], toate w >= 0
    INF = float("inf")
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]                     # (distanță, nod) — heapq e min-heap
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:                   # intrare veche (lazy deletion) → ignor
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:              # relaxare
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist                           # INF pe pozițiile inaccesibile
```

**Exemple:** Network Delay Time, Path with Minimum Effort, Cheapest Flights Within K Stops
(versiunea fără limita de K), Swim in Rising Water.

**Capcane:** o **muchie negativă** strică tot (nodul „finalizat" poate fi îmbunătățit mai târziu)
→ folosește Bellman-Ford. Nu pune `(nod, dist)` în heap, altfel tie-break-ul devine aleatoriu.
Cu `dist[node]` unic rezultatul e unic; pentru drumuri distincte care cer ordine (ex. „cel mai mic
drum lexicografic") sortă/evaluează vecinii explicit.

---

### 22.2 Bellman-Ford (inclusiv „cel mult K opriri")

**Când apare:** ponderi **negative**, detectare de ciclu negativ, sau când drumul e limitat la un
număr de pași/muchii („cheapest flight with at most K stops").

**Ideea-cheie:** `V - 1` runde de relaxare peste **toate** muchiile. La runda `i` ai sigur distanțele
minime care folosesc cel mult `i` muchii. De aici două lucruri: rezistă la ponderi negative (nu
„finalizezi" niciodată un nod prematur) și, rulând doar `K + 1` runde, obții exact răspunsul cu cel
mult `K + 1` muchii = cel mult `K` opriri. Complexitate `O(V * E)`.

**Schelet:**
```python
def bellman_ford(n, edges, src, k=None):  # edges = [(u, v, w)]
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    rounds = n - 1 if k is None else k + 1     # k opriri = k + 1 muchii
    for _ in range(rounds):
        nxt = dist[:]                          # copie: o rundă = o muchie în plus
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < nxt[v]:
                nxt[v] = dist[u] + w
        if nxt == dist:                        # nimic nu s-a schimbat → ne oprim
            break
        dist = nxt
    return dist

# ciclu negativ: mai fă o rundă peste muchii; dacă încă se poate relaxa → există ciclu negativ
```

**Exemple:** Cheapest Flights Within K Stops (787), Network Delay Time (743, varianta cu ponderi
negative dacă apar), Bellman-Ford clasic / Negative Cycle Detection.

**Capcane:** fără copie (`nxt = dist[:]`) limita de `K` opriri dispare — într-o singură rundă
poți înlănțui mai multe muchii și obții drumul neoptimizat-nelimitat. Ordinea muchiilor nu contează
pentru corectitudine, doar numărul de runde.

---

### 22.3 MST: Kruskal (sortare + DSU) și Prim (heap)

**Când apare:** „leagă toate punctele cât mai ieftin" — cost minim de conectare, cabluri/rețele,
clustering. Graf **neorientat**, cu ponderi (poate fi și graf complet implicit, ex. distanța
Manhattan între toate perechile de puncte).

**Ideea-cheie:** ambele sunt greedy și dau același cost total (muchii diferite uneori).
**Kruskal:** sortezi muchiile crescător și le adaugi dacă nu închid ciclu (`DSU` verifică asta) —
`O(E log E)`, câștigă pe grafuri rare. **Prim:** pornești dintr-un nod și extinzi arborele mereu cu
muchia minimă care iese din el (heap) — `O(E log V)`, câștigă pe grafuri dense / graf complet
implicit, unde nu vrei să materializezi toate muchiile.

**Schelet (Kruskal):**
```python
def kruskal(n, edges):                       # edges = [(w, u, v)]
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]    # path compression
            x = parent[x]
        return x
    total = used = 0
    for w, u, v in sorted(edges):
        ru, rv = find(u), find(v)
        if ru == rv:                         # ar închide ciclu → sar
            continue
        parent[rv] = ru
        total += w
        used += 1
        if used == n - 1:                    # n - 1 muchii = arbore
            break
    return total
```

**Schelet (Prim, cu heap pe muchii / „punctelor cele mai apropiate"):**
```python
import heapq

def prim(n, adj, start=0):                   # adj[u] = [(v, w)]
    seen = [False] * n
    pq = [(0, start)]                        # (cost, nod)
    total = used = 0
    while pq and used < n:
        w, u = heapq.heappop(pq)
        if seen[u]:                           # intrare veche
            continue
        seen[u] = True
        total += w
        used += 1
        for v, w2 in adj[u]:
            if not seen[v]:
                heapq.heappush(pq, (w2, v))
    return total
```

**Exemple:** Min Cost to Connect All Points (1584), Connecting Cities With Minimum Cost, Optimize
Water Distribution, Minimum Spanning Tree clasic.

**Capcane:** Kruskal pe graf complet construit explicit are `O(n²)` memorie (pentru `n = 1000`
puncte sunt ~500k muchii — acceptabil, dar sub 5000 de puncte devine problema); Prim e mai bun
acolo. `n = 0 / 1` → costul e 0 (arborele are 0 muchii), nu uita cazul. Puncte duplicate → muchie
de cost 0, răspunsul rămâne valid.

---

## 23. Math & Geometrie

**Când apare:** probleme de divizibilitate („împarte în bucăți egale", fracții), precomputare de
prime, puteri uriașe sau calcule modulo, procese iterative pe cifre care pot intra în buclă,
verificări geometrice (coliniaritate, arie, orientare).

**Ideea-cheie:** matematica nu cere structuri de date, ci o **observație** care reduce forța brută:
Euclid înjumătățește numerele la fiecare pas, ciurul taie compusele o singură dată, exponențiarea
înjumătățește exponentul, iar un proces iterativ pe o mulțime finită se analizează ca **ciclu pe o
funcție**. Toate se fac în **intregi** când e posibil.

**Exemple:** Count Primes, Happy Number, Pow(x, n), Max Points on a Line, Rotate Image.

---

### 23.1 cmmdc / cmmmc (Euclid)

**Când apare:** fracții simplificate, „cea mai mare lungime de bucată care împarte exact",
periodicitate, gcd pe mai multe numere.

**Ideea-cheie:** `cmmdc(a, b) = cmmdc(b, a % b)` până când `b == 0`; complexitate O(log min(a,b)).
`cmmmc(a, b) = a // cmmdc(a, b) * b` — împarte **înainte** de a înmulți.

**Schelet:**
```python
def gcd(a, b):
    while b:
        a, b = b, a % b        # Euclid
    return a

def lcm(a, b):
    return a // gcd(a, b) * b  # împart întâi, apoi înmulțesc

# pentru o listă: reduce cu gcd peste toate elementele
```

**Capcane:** `a * b // gcd` în C++/Java poate da overflow — întâi împărțirea. Pentru 0:
`gcd(0, x) == x`.

---

### 23.2 Ciurul lui Eratostene

**Când apare:** „câte numere prime până la n", factorizare pentru multe numere, precomputare de
divizori / funcții multiplicative.

**Ideea-cheie:** marchezi compusele pornind de la `p * p` (orice multiplu mai mic are un factor prim
mai mic, deja procesat); te oprești când `p * p >= n`. Timp O(n log log n), spațiu O(n).

**Schelet:**
```python
def count_primes(n):
    if n < 3:
        return 0
    is_prime = bytearray([1]) * n              # indici 0..n-1
    is_prime[0] = is_prime[1] = 0
    p = 2
    while p * p < n:
        if is_prime[p]:
            is_prime[p * p::p] = bytearray(len(is_prime[p * p::p]))   # taie multiplii
        p += 1
    return sum(is_prime)
```

**Exemple:** Count Primes, Prime Arrangements, Closest Prime Numbers in Range.

**Capcane:** `n = 0/1/2` → răspuns 0 (atenție la indicii 0 și 1); `bytearray` ține memoria mică față
de o listă de bool-uri; nu reporni de la `p`, ci de la `p * p`.

---

### 23.3 Aritmetică modulară și exponențiere rapidă

**Când apare:** `x^n` pentru n uriaș, răspunsuri modulo 10^9+7, combinatorică (nCp), hash-uri,
recursii cu numere mari.

**Ideea-cheie:** adunarea/înmulțirea se pot face modulo la fiecare pas, iar `x^n` se calculează în
O(log n) prin înjumătățirea exponentului: `x^n = (x^2)^(n/2)` pentru n par, `x * x^(n-1)` pentru n
impar. Exponent negativ → inversezi baza.

**Schelet:**
```python
def mod_pow(base, exp, mod):
    r, base = 1, base % mod
    while exp:
        if exp & 1:              # bitul curent din exponent
            r = r * base % mod
        base = base * base % mod
        exp >>= 1
    return r

def my_pow(x, n):                # LeetCode 50 (float)
    if n < 0:
        x, n = 1 / x, -n         # în Python -(-2**31) e în siguranță
    r = 1.0
    while n:
        if n & 1:
            r *= x
        x *= x
        n >>= 1
    return r
```

**Exemple:** Pow(x, n), Super Pow, Pow(x, n) modular.

**Capcane:** în C++/Java `-n` pentru `n == INT_MIN` dă overflow → folosește `long`. Compararea
float cu `==` e corectă doar pentru valori exact reprezentabile (puteri ale lui 2, 0.5); evita
baze ca 3.0 sau rezultate iraționale în teste.

---

### 23.4 Happy Number — detectarea ciclului pe o funcție

**Când apare:** orice proces iterativ `x -> f(x)` pe o mulțime finită: suma pătratelor cifrelor,
collatz, „next number", graf funcțional (fiecare nod are o singură muchie ieșire).

**Ideea-cheie:** pe o mulțime finită, secvența intră obligatoriu într-un ciclu (eventual de lungime
1, adică un punct fix). Detectezi cu un `set` de valori văzute (simplu, spațiu O(ciclu + coadă))
sau cu **Floyd** (doi pointeri, spațiu O(1)).

**Schelet:**
```python
def digit_square_sum(n):
    s = 0
    while n:
        n, d = divmod(n, 10)
        s += d * d
    return s

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:   # 1 = punct fix; repetiție = ciclu fără 1
        seen.add(n)
        n = digit_square_sum(n)
    return n == 1

# Floyd (spațiu O(1)): slow = f(n), fast = f(f(n)), apoi slow = f(slow), fast = f(f(fast))
```

**Exemple:** Happy Number, Find the Duplicate Number (același principiu de ciclu).

**Capcane:** condiția de oprire e `n == 1 or n in seen` — nu doar „s-a repetat"; pentru happy
number nu ai nevoie de Floyd ca să treci testele, dar e varianta O(1) spațiu.

---

### 23.5 Geometrie de bază (întregi, fără float)

**Când apare:** puncte coliniare, orientare (viraj stânga/dreapta), arie de triunghi/poligon,
intersecții de segmente, convex hull.

**Ideea-cheie:** produsul vectorial 2D (cross) decide totul:
`cross(o, a, b) = (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)`. Semnul dă orientarea, `0` înseamnă
coliniaritate. Aria triunghiului = `|cross| / 2`, aria poligonului = `|Σ cross| / 2` (shoelace).
Calculele rămân în intregi, deci `== 0` e o comparație sigură.

**Schelet:**
```python
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    # > 0 -> viraj la stânga, < 0 -> la dreapta, == 0 -> coliniare

def double_area(poly):                      # shoelace, întoarce dublul ariei
    s = 0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        s += x1 * y2 - x2 * y1
    return abs(s)                           # arie = double_area / 2
```

**Exemple:** Max Points on a Line, Valid Boomerang, Convex hull (vezi și secțiunea 29).

**Capcane:** nu folosi `sqrt` / float pentru coliniaritate (erori de rotunjire) — doar cross;
semnul ariei depinde de ordinea punctelor, ia `abs` la final. Rotirea de matrice (Rotate Image)
e treabă de **matrix/grid**, nu de geometrie: 90° orar = transpunere + reverse pe fiecare linie.

---

## 24. DP avansat (knapsack, LIS, interval, bitmask, digit, arbore, state machine)

### 24.1 0/1 Knapsack și knapsack cu repetare

**Când apare:** „alegi obiecte cu greutate și valoare încă încap într-o capacitate" — maximizarea
valorii, subset sum cu target mic, Partition Equal Subset Sum (capacitate = suma / 2), numărul minim
de monede, Target Sum. Semnalul: **două dimensiuni** (obiecte × capacitate), cu capacitatea de ordinul
miilor, nu al miliardelor.

**Ideea-cheie:** `dp[i][c]` = valoarea maximă folosind **primele `i` obiecte** cu capacitatea `c`.
Tranziția e alegerea binară „iau obiectul / nu-l iau":
`dp[i][c] = max(dp[i-1][c], dp[i-1][c-w] + v)`. Tabelul are `(n+1) × (cap+1)` celule, iar răspunsul se
citește din **colțul din dreapta-jos**, `dp[n][cap]`, pentru că subproblema „toate obiectele, toată
capacitatea" e exact întrebarea pusă (și `dp[n][c]` e monoton nedescrescător în `c`, deci
`dp[n][cap]` e maximul pe `c <= cap`). Prima linie `dp[0][*] = 0` (niciun obiect → valoare 0).

Linia `i` depinde **doar** de linia `i-1`, deci poți păstra un singur array 1-D `dp[c]`. Cheia e
**ordinea buclei peste capacitate**: mergând **invers** (`cap → w`), `dp[c-w]` aparține încă „rundei
precedente" (fără obiectul curent) → fiecare obiect se ia cel mult o dată. Dacă mergi crescător,
`dp[c-w]` a fost deja actualizat cu obiectul curent → îl folosești de mai multe ori, adică rezolvi
fără să vrei **knapsack cu repetare (unbounded)**. Spațiu: O(cap).

**Schelet:**
```python
def knapsack_01(weights, values, cap):          # fiecare obiect cel mult o dată
    dp = [0] * (cap + 1)                        # dp[c] = valoarea maximă cu capacitatea c
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):         # INVERS: dp[c - w] e încă "fără obiectul curent"
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]                              # = dp[n][cap] din tabelul 2-D

def knapsack_unbounded(weights, values, cap):   # obiecte reutilizabile (stoc infinit)
    dp = [0] * (cap + 1)
    for c in range(1, cap + 1):
        for w, v in zip(weights, values):       # crescător: obiectul poate fi luat din nou
            if w <= c:
                dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]
```

**Exemple:** Partition Equal Subset Sum (416), Coin Change (322, unbounded cu sentinel `inf`),
Coin Change II (518, numărare), Target Sum (494), Last Stone Weight II (1049), Ones and Zeroes (474).

**Capcane:** ordinea buclei interioare decide varianta — **invers = 0/1, crescător = cu repetare**;
e greșeala care trece „aproape" toate testele. „Imposibil" nu se reprezintă prin `0` (0 e o valoare
validă, ex. valoarea unui obiect) ci prin `inf` / `-1` convențional (Coin Change). Capacitatea `0`
sau lista de obiecte goală → `0`. Când aduni număr de soluții (Coin Change II), inițializează
`dp[0] = 1` și nu folosi `min`/`max`.

---

### 24.2 LIS cu patience sorting și bisect

**Când apare:** „cea mai lungă subsecvență strict crescătoare", înlănțuire de perechi/șiruri,
Russian Doll Envelopes (după sortare), Maximum Length of Pair Chain, când `n` e peste ~2500 și O(n²)
nu mai intră.

**Ideea-cheie:** ții `tails[k]` = **cea mai mică valoare cu care poate să se termine** o subsecvență
crescătoare de lungime `k+1`. `tails` e mereu strict crescător, deci poți căuta binar. Pentru fiecare
`x` din listă: `i = bisect_left(tails, x)`; dacă `i == len(tails)` → `x` extinde cea mai lungă
subsecvență găsită până acum (LIS crește), altfel înlocuiești `tails[i] = x` (LIS de lungime `i+1` se
termină acum într-o valoare mai mică → e „mai util" pentru elementele viitoare). Răspunsul final e
`len(tails)`. Cost: O(n log n), spațiu O(n). Pentru „strict crescător" folosește `bisect_left`, pentru
„nedescrescător" (permite egale) `bisect_right`.

**Schelet:**
```python
import bisect

def lis(nums):
    tails = []                              # tails[k] = minimul care termină o subsecvență de lungime k+1
    for x in nums:
        i = bisect.bisect_left(tails, x)    # prima poziție cu tails[i] >= x
        if i == len(tails):
            tails.append(x)                 # x extinde cea mai lungă subsecvență
        else:
            tails[i] = x                    # înlocuire: aceeași lungime, final mai mic
    return len(tails)                       # lungimea LIS
```

**Exemple:** Longest Increasing Subsequence (300), Russian Doll Envelopes (354: sortare pe lățime
crescător, iar la lățimi egale pe înălțime **descrescător**, apoi LIS strict pe înălțimi),
Longest String Chain (1048), Maximum Length of Pair Chain (646).

**Capcane:** `tails` **nu** este o subsecvență validă din listă — e doar frontiera minimelor; pentru a
reconstrui subsecvența reală ai nevoie de indecși/părinți. La „strict" vs „permite egale" alegerea
lui `bisect_left` / `bisect_right` schimbă răspunsul. Dacă aplici LIS pe perechi sortate, ordinea
tie-break-ului e cea care face trucul (vezi Russian Doll Envelopes).

---

### 24.3 Interval DP

**Când apare:** problema se descompune pe un **interval contiguu** `[i, j]`, iar decizia e „ce se
întâmplă ultimul/primul în interval": Burst Balloons, Palindrome Partitioning, Matrix Chain
Multiplication, Minimum Cost to Cut a Stick, Strange Printer, Guess Number Higher or Lower II.

**Ideea-cheie:** `dp[i][j]` = răspunsul optim pentru intervalul `i..j`, răspunsul final e
`dp[0][n-1]`. Enumeri un punct de rupere `k` și combini `dp[i][k]` cu `dp[k+1][j]`. Cheia e să alegi
corect **ordinea evenimentelor**: la Burst Balloons alegi balonul care e spart **ultimul** în interval,
nu primul — la acel moment vecinii lui sunt fix `i-1` și `j+1` (nu depind de ce s-a spart înainte),
deci subproblemele devin independente. Calculezi pe **lungimi crescătoare** de interval, ca orice
subinterval folosit să fie deja gata.

**Schelet:**
```python
def max_coins(nums):                            # Burst Balloons; padding cu 1 la ambele capete
    a = [1] + nums + [1]
    n = len(a)
    dp = [[0] * n for _ in range(n)]            # dp[i][j] = câștigul maxim pe intervalul deschis (i, j)
    for length in range(2, n):                  # lungimi crescătoare: subintervalele sunt deja calculate
        for i in range(0, n - length):
            j = i + length
            for k in range(i + 1, j):           # k = ultimul balon spart din (i, j)
                gain = a[i] * a[k] * a[j] + dp[i][k] + dp[k][j]
                dp[i][j] = max(dp[i][j], gain)
    return dp[0][n - 1]                         # tot intervalul, fără cei doi pereți de 1
```

**Exemple:** Burst Balloons (312), Palindrome Partitioning II (132: tabel `is_palin[i][j]` + `cuts[i]`),
Minimum Cost to Cut a Stick (1547), Strange Printer (664), Matrix Chain Multiplication.

**Capcane:** ordinea buclelor (**după lungimea intervalului**) e obligatorie; dacă iterezi `i`
crescător citești celule necalculate. La numărare de moduri tranziția se **adună** (`+`, nu `max`),
iar intervalul gol (`n = 0` sau `n = 1`) e un caz de bază separat. Nu amesteca „interval deschis"
(ca mai sus, cu padding) cu „interval închis" — majoritatea bug-urilor aici sunt de indexare ±1.

---

### 24.4 Bitmask DP (n ≤ 20)

**Când apare:** probleme peste **submulțimi** de până la ~20 de elemente: TSP / Shortest Path
Visiting All Nodes, Partition to K Equal Sum Subsets, Matchsticks to Square, acoperire de mască cu
cost minim (stickers), assignment / matching. Condiția de intrare: `n ≤ 20`, pentru că starea e
`2^n`.

**Ideea-cheie:** starea e o **mască de biți** peste mulțimea deja „rezolvată" (+ eventual poziția
curentă). `dp[mask][i]` = cel mai bun rezultat când ai folosit submulțimea `mask` și ești în nodul
`i`. Tranziția adaugă un element nou `j` care nu e în mască:
`dp[mask | (1 << j)][j] = min(..., dp[mask][i] + cost(i, j))`. Enumeri măștile crescător (submulțimi
mai mici întâi) → O(2ⁿ · n²) timp, O(2ⁿ · n) spațiu. Când poziția curentă nu contează, starea e
doar `dp[mask]`.

**Schelet:**
```python
def tsp(dist):                                  # dist[i][j], n <= 20
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]     # dp[mask][i]: am văzut `mask`, sunt în nodul i
    dp[1][0] = 0                                # pornesc din nodul 0
    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask >> j & 1:               # j deja vizitat
                    continue
                nxt = mask | (1 << j)
                dp[nxt][j] = min(dp[nxt][j], dp[mask][i] + dist[i][j])
    full = (1 << n) - 1
    return min(dp[full][i] + dist[i][0] for i in range(n))   # închid turul
```

**Exemple:** Shortest Path Visiting All Nodes (847), Partition to K Equal Sum Subsets (698),
Matchsticks to Square (473), Find the Shortest Superstring (943), TSP clasic.

**Capcane:** memoria — la `n = 20` sunt 1M de măști × 20 de poziții ≈ 20M de valori, la limita
acceptabilă; folosește liste simple (nu dicționar pe măști) și ignoră stările `INF`. Pentru a
enumera **submăștile** unei măști: `sub = mask; while sub: ...; sub = (sub - 1) & mask` (fără `sub`
gol, luat separat). Nu uita să închizi turul (`+ dist[i][0]`) la TSP, altfel închizi greșit.

---

### 24.5 Digit DP

**Când apare:** „câte numere din `[0, N]` au proprietatea X **pe cifre**" — cifre distincte, fără
cifra 4, sumă de cifre = k, divizibile cu 3, fără „11" consecutiv. Semnalul: `N` uriaș (10⁹+), dar
numărul de cifre e mic (≤ 18-19), deci starea se leagă de poziția cifrei, nu de valoarea lui N.
Răspuns pe interval: `f(R) - f(L - 1)`.

**Ideea-cheie:** construiești numărul **cifră cu cifră de la stânga la dreapta**, iar starea ține:
poziția, `tight` (true = prefixul e exact cel al lui N, deci cifra curentă e limitată de cifra lui N,
false = ai coborât deja sub N și restul cifrelor sunt libere), `started` (ai început numărul, ca să
nu numeri zerourile de la stânga) și ce mai cere problema (suma cifrelor, ultima cifră, mască de
cifre folosite). Memoizezi stările cu `tight = False` — subarborele „liber" se repetă identic, iar
acolo stă câștigul de complexitate.

**Schelet:**
```python
import functools

def count_sum_digits_div3(N):                   # câte numere din [1, N] au suma cifrelor divizibilă cu 3
    digits = list(map(int, str(N)))

    @functools.lru_cache(maxsize=None)
    def dp(pos, tight, started, total):
        if pos == len(digits):
            return 1 if started and total % 3 == 0 else 0
        limit = digits[pos] if tight else 9     # tight: nu depăși prefixul lui N
        count = 0
        for d in range(limit + 1):
            count += dp(pos + 1, tight and d == limit, started or d != 0, total + d)
        return count

    return dp(0, True, False, 0)
```

**Exemple:** Count Numbers with Unique Digits (357), Numbers At Most N Given Digit Set (902),
Non-negative Integers without Consecutive Ones (600), Count of Integers (varianta cu `[L, R]`),
Count Special Integers (2376).

**Capcane:** `tight` **trebuie** să facă parte din starea memoizată (sau să memoizezi doar cazul
`tight = False`); dacă îl ignori, numerele se numără greșit. Fără `started`, zerourile de la stânga
se comportă ca cifre reale (strică „cifre distincte" și „suma cifrelor"). `f(L - 1)` cere atenție la
`L = 0`. La `[L, R]` răspunsul e o diferență de două apeluri, nu o singură parcurgere cu două limite.

---

### 24.6 DP pe arbore (post-ordine)

**Când apare:** alegere optimă pe un arbore cu o constrângere **locală** părinte–copil: House
Robber III, Binary Tree Cameras, diametru/cel mai bun traseu, tăierea muchiilor, produs de subarbori.
Apare și ca „tree matching" pe arbore general (DFS + `dp` pe muchii).

**Ideea-cheie:** fiecare nod întoarce către părinte **câteva valori** care descriu cazurile în care
poate fi (de obicei „cu nodul luat" și „cu nodul neluat"); valorile se calculează din răspunsurile
copiilor în **post-ordine** (întâi copiii, apoi nodul). E un DP fără tabel — stările sunt pe stiva
recursiei.

**Schelet:**
```python
def rob_tree(root):
    # întoarce (câștigul dacă NU iau nodul, câștigul dacă ÎL iau)
    def dfs(node):
        if node is None:
            return (0, 0)
        left_skip, left_take = dfs(node.left)
        right_skip, right_take = dfs(node.right)
        take = node.val + left_skip + right_skip       # iau nodul → copiii nu se iau
        skip = max(left_skip, left_take) + max(right_skip, right_take)
        return (skip, take)

    return max(dfs(root))
```

**Exemple:** House Robber III (337), Binary Tree Cameras (968), Diameter of Binary Tree (543),
Maximum Product of Splitted Binary Tree (1339), Longest Path With Different Adjacent Characters (2246).

**Capcane:** stările trebuie să fie **complete** — dacă lipsește un caz (ex. copilul neluat când
părintele e luat), obții valori prea mari. Recursia pe un arbore degenerat depășește limita de stivă
în Python: urcă `sys.setrecursionlimit` sau scrie parcurgerea iterativ (post-ordine cu stivă). Pe
arbore general, `dp` se combină pe muchii și ai grijă la nodul de start al DFS-ului (un DFS din
rădăcină, fără `parent`).

---

### 24.7 State machine DP

**Când apare:** o succesiune de „zile"/pași în care poți fi într-una din câteva stări fixe, cu
câștig/penalizare la tranziții: Best Time to Buy and Sell Stock with Cooldown, cu Transaction Fee,
at most K transactions, dar și alte DP-uri cu stări discrete (freeze/hold).

**Ideea-cheie:** scrii explicit stările și tranzițiile valide, ca într-o mașină de stări. Pentru
stock cu cooldown: `rest` (nu dețin și pot cumpăra), `hold` (dețin), `sold` (am vândut azi → mâine
sunt în cooldown). În fiecare zi recalculezi **din valorile de ieri** (atribuire simultană), iar
răspunsul e maximul stărilor „fără acțiune". Cost O(n · numărul de stări), spațiu O(1).

**Schelet:**
```python
def max_profit_cooldown(prices):
    # rest = nu dețin și sunt liber; hold = dețin; sold = am vândut azi (mâine cooldown)
    rest, hold, sold = 0, -float("inf"), -float("inf")
    for p in prices:
        rest, hold, sold = (
            max(rest, sold),        # aștept sau ies din cooldown
            max(hold, rest - p),    # cumpăr azi doar dacă ieri eram liber
            hold + p,               # vând azi ce dețineam
        )
    return max(rest, sold)          # nu pot termina „deținând"
```

**Exemple:** Best Time to Buy and Sell Stock with Cooldown (309), with Transaction Fee (714),
Best Time to Buy and Sell Stock III / IV (123 / 188, `K` perechi de stări), House Robber (198 — două
stări: luat / neluat), Paint House.

**Capcane:** dacă folosești `hold` deja actualizat când calculezi `sold`, vinzi și cumperi în aceeași
zi — de aceea atribuirea simultană (sau copii ale valorilor vechi). Cooldown înseamnă „nu pot cumpăra
în ziua imediat următoare vânzării". La „cel mult K tranzacții", stările devin `2K` (sau matrice
`dp[k][stare]`) și trebuie inițializate cu `-inf` (nu toate sunt accesibile). Zero zile sau nicio
tranzacție profitabilă → 0.

---

---

## 25. Algoritmi pe stringuri (KMP, Rabin-Karp, Z, Manacher, Aho-Corasick)

### 25.1 KMP (tabel de prefix) — de ce e O(n + m)

**Când apare:** căutare de pattern în text (`strStr`), numărarea aparițiilor, perioade și repetiții
(Repeated Substring Pattern, „shortest palindrome"), potrivire pe text mare sau care se citește o
singură dată (streaming), unde nu-ți permiți să reiei potrivirea de la 0. Apare și când se cere
explicit O(n + m).

**Ideea-cheie:** `pi[i]` = lungimea celui mai lung **prefix propriu** al pattern-ului care este și
sufix al lui `pattern[:i+1]`. Când ai un mismatch după `k` caractere potrivite, nu repornești de la
0: ultimele `pi[k-1]` caractere sunt identice cu începutul pattern-ului, deci sari direct la
`k = pi[k-1]` și nu retestezi ce știi deja că se potrivește. Textul e parcurs o singură dată
(indexul `i` nu scade niciodată), iar `k` crește cu cel mult 1 per pas, deci în total scade de cel
mult n ori → O(n + m) amortizat. (Varianta naivă retestează poziții deja verificate → O(n · m).)

**Schelet:**
```python
def prefix_table(p):                            # pi[i] = cel mai lung prefix propriu care e și sufix
    pi = [0] * len(p)
    k = 0                                       # k = câte caractere se potrivesc acum
    for i in range(1, len(p)):
        while k and p[i] != p[k]:
            k = pi[k - 1]                       # fallback, fără să reiau de la 0
        if p[i] == p[k]:
            k += 1
        pi[i] = k
    return pi

def kmp_search(text, p):
    if not p:
        return 0                                # pattern gol → apare la indexul 0
    pi = prefix_table(p)
    k = 0
    for i, ch in enumerate(text):
        while k and ch != p[k]:
            k = pi[k - 1]                       # textul nu se întoarce niciodată
        if ch == p[k]:
            k += 1
        if k == len(p):
            return i - len(p) + 1               # prima apariție; pentru toate: k = pi[k - 1]
    return -1
```

**Exemple:** Find the Index of the First Occurrence in a String (28), Repeated Substring Pattern
(459: `n % (n - pi[n-1]) == 0`), Shortest Palindrome (214), Longest Happy Prefix (1392), Count
Prefixes of a Given String (2255).

**Capcane:** `pi[k-1]`, nu `pi[k]` — `k` numără caracterele potrivite, nu indexează caracterul
curent; `pi[0] = 0` mereu. Când cauți **toate** aparițiile nu reseta `k = 0` după un match (ratăzi
aparițiile care se suprapun, ex. `"aaaa"` în `"aaaaa"`), ci continuă cu `k = pi[k-1]`. Nu uita cazul
pattern gol → 0, iar `-1` înseamnă strict „nu apare nicăieri".

---

### 25.2 Rabin-Karp (hash rulant) și coliziuni

**Când apare:** când compari **multe ferestre de lungime fixă** sau cauți mai multe pattern-uri de
aceeași lungime: Repeated DNA Sequences (ferestre de 10), Longest Duplicate Substring (căutare
binară pe lungime + rolling hash), Distinct Echo Substrings, fingerprinting / detecție de plagiat,
Find Substring With Given Hash Value.

**Ideea-cheie:** interpretezi fereastra ca un număr în baza `b`: `h = c0·b^(m-1) + ... + c(m-1)`.
Când muți fereastra cu un pas, nu recalculezi: **scoți** caracterul care iese (scazi
`c_old · b^(m-1)`) și **adaugi** caracterul nou (`h = (h - c_old·b^(m-1))·b + c_new`) — O(1) per
poziție, O(n) pentru tot șirul. Pe un text scurt `h` încape într-un `int` (Python: precizie
arbitrară), pe text lung iei `% mod` cu un prim mare (sau `& (2⁶⁴ - 1)`) ca să rămână O(1) și să
nu explodeze numărul.

**Schelet:**
```python
def repeated_dna(s, m=10):
    if len(s) < m:
        return []
    code = {"A": 0, "C": 1, "G": 2, "T": 3}     # fiecare bază = o cifră în baza 4
    base = 4
    high = base ** (m - 1)                      # cât "cântărește" caracterul care iese din fereastră

    h = 0                                       # hash-ul primei ferestre, O(m)
    for i in range(m):
        h = h * base + code[s[i]]

    counts = {h: 1}
    for i in range(m, len(s)):                  # hash rulant: O(1) per pas
        h = (h - code[s[i - m]] * high) * base + code[s[i]]
        counts[h] = counts.get(h, 0) + 1

    found, h = set(), 0                         # a doua trecere: rețin ferestrele cu hash repetat
    for i in range(m):
        h = h * base + code[s[i]]
    if counts[h] > 1:
        found.add(s[:m])
    for i in range(m, len(s)):
        h = (h - code[s[i - m]] * high) * base + code[s[i]]
        if counts[h] > 1:
            found.add(s[i - m + 1:i + 1])
    return sorted(found)
```

**Exemple:** Repeated DNA Sequences (187), Longest Duplicate Substring (1044), Distinct Echo
Substrings (1147), Find Substring With Given Hash Value (2156).

**Capcane:** **coliziunile** — hash egal nu înseamnă neapărat string egal; fie folosești un modul
prim mare (probabilitate de coliziune neglijabilă), fie verifici candidații comparând efectiv
substringurile. În alte limbaje `%` pe negative dă rezultat negativ → adună `mod`. `pow(base, m-1)`
se calculează **o dată**, în afara buclei. Aici am numărat cu hash-uri, nu cu substringuri, tocmai
ca să evit O(n · m) la copierea ferestrelor. La „cel mai lung duplicat" nu uita că poți căuta binar
pe lungime (monotonie): dacă există duplicat de lungime `L`, există și de lungime `L-1`.

---

### 25.3 Z-function

**Când apare:** căutare de pattern (concatenezi `p + separator + text`), apariții de prefixe,
query-uri multiple pe același text, Sum of Prefix Scores, numărare de „borders", comparații de
sufixe la string sortat.

**Ideea-cheie:** `z[i]` = lungimea celui mai lung prefix al lui `s` care se potrivește cu începutul
sufixului `s[i:]` (LCP între `s` și `s[i:]`). Se calculează liniar ținând fereastra `[l, r]` a celui
mai din dreapta segment deja potrivit: dacă `i <= r`, atunci `z[i]` începe cu
`min(r - i + 1, z[i - l])` (moștenești din „oglinditul" lui `i`), apoi extinzi naiv doar dincolo de
`r`, iar `r` crește la fiecare extindere → O(n) total. Căutarea pattern-ului: în
`s = p + sep + text`, `z[i] >= len(p)` înseamnă apariție la `i - len(p) - 1`.

**Schelet:**
```python
def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0                                   # fereastra [l, r] a punctului cel mai din dreapta
    for i in range(1, n):
        if i <= r:                              # i e înăuntrul ferestrei cunoscute → moștenesc
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1                           # extind cât se potrivește
        if i + z[i] - 1 > r:                    # am depășit fereastra → o mut
            l, r = i, i + z[i] - 1
    return z

def find_pattern(text, p):
    if not p:
        return 0
    sep = "\x00"                                # separator care nu apare în text
    z = z_function(p + sep + text)
    for i in range(len(p) + 1, len(z)):
        if z[i] >= len(p):
            return i - len(p) - 1               # poziția din text
    return -1
```

**Exemple:** Find the Index of the First Occurrence in a String (28), Longest Happy Prefix (1392),
Sum of Scores of Built Strings (2223), Sum of Prefix Scores of Strings (2416 — trie, dar Z dă altă
perspectivă), String Matching in an Array (1408).

**Capcane:** separatorul nu trebuie să apară în text (altfel `z[i]` trece granița și numără
potriviri false); dacă nu ești sigur, folosește un caracter imposibil sau scade artificial limita la
`len(p)`. `z[0] = 0` prin definiție. Z-function și KMP-ul sunt echivalente ca informație
(`z` se poate calcula din `pi` și invers) — alege-l pe cel mai ușor de scris corect.

---

### 25.4 Manacher (palindromuri în O(n))

**Când apare:** cel mai lung palindrom dintr-un string, numărul de subpalindromuri, „shortest
palindrome", orice problemă cu palindromuri pe text mare. Expand-around-center e O(n²) și e acceptat
doar la `n` mic (≤ ~1000).

**Ideea-cheie:** transformi stringul în `#a#b#a#`, astfel încât **orice** palindrom (par sau impar)
devine de lungime impară cu un centru unic (un caracter real sau un `#`). Apoi calculezi `p[i]` =
raza palindromului centrat la `i`, refolosind „oglindirea" în cel mai din dreapta palindrom cunoscut
`[center, right]`: dacă `i < right`, atunci `p[i]` începe de la `min(right - i, p[2·center - i])`,
iar extinderea naivă se face doar dincolo de `right`; `right` doar crește → O(n) total. Raza
`p[i]` din stringul transformat este exact **lungimea** palindromului din stringul original.

**Schelet:**
```python
def manacher(s):
    t = "#" + "#".join(s) + "#"                 # toate palindromurile devin impare
    n = len(t)
    p = [0] * n                                 # p[i] = raza palindromului centrat la i
    center = right = 0
    for i in range(n):
        if i < right:                           # i cade în palindromul cunoscut [center, right]
            p[i] = min(right - i, p[2 * center - i])   # oglinditul lui i față de center
        while (i - p[i] - 1 >= 0 and i + p[i] + 1 < n
               and t[i - p[i] - 1] == t[i + p[i] + 1]):
            p[i] += 1                           # extind dincolo de frontieră
        if i + p[i] > right:                    # mut fereastra cunoscută
            center, right = i, i + p[i]
    best = max(range(n), key=lambda i: p[i])
    start = (best - p[best]) // 2               # poziția în stringul original
    return s[start:start + p[best]]             # raza = lungimea palindromului original
```

**Exemple:** Longest Palindromic Substring (5), Palindromic Substrings (647: suma razelor),
Shortest Palindrome (214, KMP peste `s + '#' + reverse(s)`), Maximum Product of the Length of Two
Palindromic Substrings (1960).

**Capcane:** indexarea la final — `start = (center - p[center]) // 2` e capcana clasică;
`p[0] = p[n-1] = 0` mereu. Când mai multe substringuri au lungimea maximă (ex. `"babad"` → `"bab"`
sau `"aba"`), alege convenția cerută de problemă; dacă vrei un răspuns unic, formulează testul astfel
încât maximul să fie unic. La `len(s) == 0`, ieși imediat cu `""` (altfel `max` pe listă goală crapă).

---

### 25.5 Aho-Corasick (multe pattern-uri deodată)

**Când apare:** când cauți **simultan mai multe pattern-uri** într-un text (Word Search II,
Stream of Characters, filtrare de cuvinte interzise, „câte din cele k cuvinte apar în text").
Dacă ai `k` pattern-uri, KMP de `k` ori costă O(k · n) — Aho-Corasick face totul într-o trecere.

**Ideea-cheie:** un **trie** peste toate pattern-urile + **linkuri de eșec** (`fail`), calculate cu
BFS: pentru un nod, `fail` e nodul celui mai lung sufix al șirului curent care e și prefix al unui
pattern — practic KMP generalizat pe un trie. Parcurgi textul o dată: la fiecare caracter cobori la
copil dacă există, altfel urci pe linkuri de eșec; nodurile atinse (inclusiv lanțul de `fail`)
dau toate pattern-urile care se termină la poziția respectivă. Complexitate
O(suma lungimilor pattern-urilor + n + numărul de potriviri).

**Schelet:**
```python
from collections import deque

def aho_corasick(patterns, text):
    go, fail, out = [{}], [0], [[]]              # nodul 0 = rădăcina
    for w in patterns:                           # 1) trie peste toate pattern-urile
        node = 0
        for ch in w:
            if ch not in go[node]:
                go.append({}); fail.append(0); out.append([])
                go[node][ch] = len(go) - 1
            node = go[node][ch]
        out[node].append(w)                      # pattern-ul se termină în acest nod

    q = deque(go[0].values())                    # 2) linkuri de eșec, în lățime
    while q:
        node = q.popleft()
        for ch, child in go[node].items():
            f = fail[node]
            while f and ch not in go[f]:         # urc pe linkuri de eșec
                f = fail[f]
            fail[child] = go[f].get(ch, 0)
            out[child] += out[fail[child]]       # moștenesc potrivirile sufixelor
            q.append(child)

    found, node = [], 0                          # 3) o singură trecere prin text
    for i, ch in enumerate(text):
        while node and ch not in go[node]:
            node = fail[node]
        node = go[node].get(ch, 0)
        for w in out[node]:
            found.append((i - len(w) + 1, w))    # (poziție, pattern)
    return found
```

**Exemple:** Word Search II (212 — trie; Aho-Corasick e varianta „mai multe pattern-uri în text
liniar"), Stream of Characters (1032), Implement Trie / Map Sum Pairs (fără `fail`), filtrare de
cuvinte (varianta clasică a algoritmului).

**Capcane:** `out` trebuie să moștenească lista de la `fail[child]` (altfel ratezi pattern-urile mai
scurte care sunt sufixe), iar linkurile se calculează **BFS**, nu DFS (ai nevoie ca `fail[node]` să
fie deja gata). Copiii rădăcinii au `fail = 0`. Costul depinde de numărul de potriviri — la pattern-uri
foarte frecvente în text ieșirea însăși e mare.
---

---

## 26. Structuri avansate: Segment Tree, Fenwick, Sparse Table

**Când apare:** „query pe interval" amestecat cu `update`, pe un array prea mare pentru O(n) per
operație — sumă/min/max pe subarray-uri, prefix sums pe date care se schimbă, RMQ pe date statice.
Semnalul clar: update-uri **și** query-uri în aceeași problemă, sau foarte multe query-uri pe
același array nemodificat.

**Ideea-cheie:** precalculezi agregate pe **porțiuni**, nu pe elemente, ca fiecare operație să
atingă O(log n) sau O(1) bucăți:
- **Segment Tree** — arbore peste array, fiecare nod = agregatul unei porțiuni `[lo, hi]`;
  update/query O(log n); general (sumă, min/max, gcd, lazy propagation pentru update pe interval).
- **Fenwick / BIT** — `tree[i]` = suma unei porțiuni de lungime `i & (-i)`; mai puțin cod și
  constantă mai mică, dar merge doar pentru operații **inversabile** (sumă, xor), nu la min/max.
- **Sparse Table** — `table[k][i]` = agregatul ferestrei de lungime `2^k` de la `i`; query O(1) din
  două ferestre care se suprapun; **fără update** și doar pentru operații idempotente.

Alegerea: update-uri + sumă → Fenwick (sau Segment Tree); update-uri + min/max → Segment Tree;
zero update-uri + multe query-uri → Sparse Table.

**Schelet:**
```python
# --- Fenwick: prefix sums cu update; intern 1-based, API 0-based ---
def bit_build(nums):
    n = len(nums)
    tree = [0] + list(nums)
    for i in range(1, n + 1):           # build O(n), nu n * O(log n)
        j = i + (i & -i)
        if j <= n:
            tree[j] += tree[i]
    return tree

def bit_add(tree, index, delta):        # nums[index] += delta, O(log n)
    i = index + 1                       # singurul loc unde aparatul e 1-based
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

# --- Segment tree, recapitulare (4*n noduri, indexate de la 1) ---
#   update(i, v): cobori până la frunza i, apoi la urcare refaci sumele
#   query(l, r):  combini O(log n) noduri complet acoperite (restul -> neutru)

# --- Sparse table static (min) ---
#   table[k][i] = min din fereastra de lungime 2^k care începe la i
#   query(l, r):  k = log2(r - l + 1)
#                 min(table[k][l], table[k][r - (1 << k) + 1])
```

**Exemple:** Range Sum Query - Mutable (Fenwick / Segment Tree), Range Sum Query - Immutable
(prefix sums simple), Count of Smaller Numbers After Self / numărarea inversiunilor (Fenwick peste
valori comprimate), Static RMQ / LCA cu tur Euler (Sparse Table).

**Capcane:**
- Fenwick e intern 1-based, API-ul 0-based: `i = index + 1` doar la graniță. Dacă uiți, `i & (-i)`
  pe 0 nu termină bucla corect → rezultat greșit sau buclă infinită.
- Fenwick **nu** merge la min/max — nu poți „scădea" un interval. Pentru min/max cu update ai
  nevoie de Segment Tree.
- Sparse Table nu acceptă update-uri, iar query-ul folosește două ferestre **suprapuse**: e corect
  la min/max/gcd (idempotente), greșit la sumă.
- Segment Tree: alocă `4 * n` noduri la varianta recursivă, iar intervalul disjunct întoarce
  elementul neutru (0 la sumă, `+inf` la min).
- La sume mari, limbajele cu întregi ficși cer 64 de biți (`long long`); în Python int-urile sunt
  nelimitate, deci nu-ți faci griji, dar la min/max inițializează cu `+inf`, nu cu `0`.

---

## 27. Tehnici avansate

**Când apare:** când tiparul de bază (sliding window simplu, sortare, BFS/DFS) dă complexitate
prea mare sau răspuns greșit: suprapuneri pe o axă, maxim/minim într-o fereastră glisantă, „al
k-lea element" fără sortare, strămoși comuni în arbore, subseturi cu n prea mare pentru 2ⁿ.

**Ideea-cheie:** fiecare tehnică de mai jos schimbă **ordinea sau structura** operațiilor —
procesezi evenimentele în ordine (sweep line), menții doar candidații utili (deque monoton),
arunci jumătate din array la fiecare pas (quickselect), precalculezi salturi (binary lifting) sau
tai spațiul de căutare în două jumătăți (meet-in-the-middle).

**Exemple:** Meeting Rooms II, Sliding Window Maximum, Kth Largest Element in an Array,
Lowest Common Ancestor, Subsets / Closest Subsequence Sum.

---

### 27.1 Sweep line cu evenimente sortate

**Când apare:** intervale care se suprapun (câte camere, câte mașini, câte resurse simultan),
puncte pe o axă, întrebări „câte segmente conțin punctul acesta".

**Ideea-cheie:** transformi fiecare interval în **două evenimente** (+1 la început, -1 la sfârșit),
le sortezi și faci o singură trecere, ținând un contor curent. Închizi intervalele înainte de a
deschide altele care încep exact în același punct (intervale **semi-deschise** `[start, end)`) ca
să nu numeri suprapuneri care doar se ating.

**Schelet:**
```python
def min_rooms(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))     # începe o întâlnire
        events.append((end, -1))      # se termină
    events.sort()                     # la timpi egali: -1 înaintea lui +1
    rooms = best = 0
    for _, delta in events:
        rooms += delta
        best = max(best, rooms)       # maximul simultan = răspunsul
    return best
```

**Exemple:** Meeting Rooms II, Car Pooling, My Calendar III, Number of Flowers in Full Bloom.

**Capcane:** ordinea la timpi egali (`-1` înainte de `+1`) decide dacă intervale care se ating
contează ca suprapuse; închizi evenimentul de sfârșit înainte de cel de început la același timp.

---

### 27.2 Monotonic deque (maxim/minim în fereastră)

**Când apare:** „maximul/minimul fiecărei sub-array de lungime k", sliding window unde ai nevoie de
extrem, nu de sumă.

**Ideea-cheie:** menții un deque de **indici cu valori strict descrescătoare**. Când intră o valoare
nouă `v`, arunci de la coadă tot ce e `<= v` (nu pot fi niciodată maxim cât timp `v` e în fereastră),
apoi adaugi `v`; de la cap scoți indicii ieșiți din fereastră. Fiecare indice intră și iese **o
singură dată**, deci `while`-ul interior e O(n) **amortizat**, nu O(n·k).

**Schelet:**
```python
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    dq, out = deque(), []                 # deque de indici, valori descrescătoare
    for i, v in enumerate(nums):
        while dq and nums[dq[-1]] <= v:   # arunc candidații mai mici
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:                # capul a ieșit din fereastră
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])       # capul e maximul ferestrei
    return out
```

**Exemple:** Sliding Window Maximum, Shortest Subarray with Sum at Least K (varianta pe minime),
Constrained Subsequence Sum.

**Capcane:** `<=` vs `<` la aruncare decide dacă păstrezi indici egali (ambele variante corecte,
dar consecvente); fereastra are `len(nums) - k + 1` rezultate. Un heap cu lazy deletion dă
O(n log n) — corect, dar aici se cere O(n).

---

### 27.3 Quickselect (statistici de ordine)

**Când apare:** „al k-lea cel mai mare/mic", mediană, top-k fără să sortezi tot.

**Ideea-cheie:** partiționezi ca la quicksort în jurul unui pivot: elementele mai mici în stânga,
mai mari în dreapta. Dacă poziția finală a pivotului e exact `len(nums) - k`, ai răspunsul; altfel
te duci doar în jumătatea care conține ținta. Media O(n), căci `n + n/2 + n/4 + ... = 2n`.
Sortarea completă ar fi O(n log n) și nu e scopul exercițiului.

**Schelet:**
```python
def find_kth_largest(nums, k):
    target = len(nums) - k        # poziția din array sortat crescător
    lo, hi = 0, len(nums) - 1
    while True:
        pivot = nums[hi]          # pivot fix (determinist), NU random
        store = lo
        for i in range(lo, hi):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[hi] = nums[hi], nums[store]
        if store == target:
            return nums[store]
        elif store < target:
            lo = store + 1        # ținta e în dreapta
        else:
            hi = store - 1        # ținta e în stânga
```

**Exemple:** Kth Largest Element in an Array, Kth Smallest Element in a Sorted Matrix,
Top K Frequent Elements (varianta fără heap).

**Capcane:** cu pivot prost (ex. ultimul element pe un array deja sortat/descrescător) partiționarea
degeneră și devine O(n²) — în practică se folosește **median-of-three** sau pivot aleator, dar
testele nu trebuie să depindă de alegerea pivotului. Quickselect modifică array-ul în loc (copiază
dacă inputul trebuie păstrat) și nu sortează restul, deci rezultatul e valoarea, nu aranjamentul.

---

### 27.4 Binary lifting (LCA și sărituri pe arbore)

**Când apare:** arbore **static** cu multe întrebări de tip „care e strămoșul comun al lui u și v",
„al k-lea strămoș", „pe ce muchie trece drumul dintre două noduri".

**Ideea-cheie:** precalculezi `up[j][v]` = strămoșul lui v la distanța `2^j`, cu recurența
`up[j][v] = up[j-1][up[j-1][v]]` — O(n log n) spațiu/timp. Pentru LCA: ridici nodul mai adânc la
aceeași adâncime (sărind biți), apoi, dacă nodurile diferă, le ridici pe ambele cu pași descrescători
până când tații coincid.

**Schelet:**
```python
LOG = 17                          # 2^17 > 1e5
up = [[0] * n for _ in range(LOG)]  # up[0][v] = tatăl lui v (up[0][rădăcină] = rădăcină)
for j in range(1, LOG):
    for v in range(n):
        up[j][v] = up[j - 1][up[j - 1][v]]

def lift(v, steps):               # urcă v cu `steps` muchii
    for j in range(LOG):
        if steps >> j & 1:
            v = up[j][v]
    return v

# lca(u, v): egalezi adâncimile, apoi cobori j de la LOG-1 la 0:
#   if up[j][u] != up[j][v]: u, v = up[j][u], up[j][v]
# răspuns: up[0][u]
```

**Exemple:** Lowest Common Ancestor of a Binary Tree, Kth Ancestor of a Tree Node,
Distance Between Two Nodes.

**Capcane:** `LOG` trebuie să acopere adâncimea maximă (`LOG > log2(n)`); rădăcina e propriul
strămoș (sentinelă) ca să nu ieși din arbore. Binary lifting cere arbore **static** — dacă se
modifică structura, ai nevoie de altceva (Euler tour + RMQ / Link-Cut).

---

### 27.5 Meet-in-the-middle (când n ≤ 40)

**Când apare:** submulțimi cu n până la ~40, unde 2ⁿ e prea mult, dar 2^(n/2) e ok: „există
submulțime cu sumă S", „numărul minim de operații", knapsack cu n mare și valori mari.

**Ideea-cheie:** tai problema în două jumătăți, enumeri toate submulțimile fiecăreia (2^(n/2) fiecare),
sortezi una dintre liste și, pentru fiecare element din cealaltă, cauți complementul cu **binary
search** (sau doi pointeri). Rezultă O(2^(n/2) · log 2^(n/2)) în loc de O(2ⁿ).

**Schelet:**
```python
import bisect

def has_subset_sum(nums, target):
    half = len(nums) // 2
    def sums(arr):                      # toate sumele de submulțimi (2^len)
        res = [0]
        for x in arr:
            res += [s + x for s in res]
        return res
    left, right = sums(nums[:half]), sorted(sums(nums[half:]))
    for s in left:                      # caut complementul în dreapta
        i = bisect.bisect_left(right, target - s)
        if i < len(right) and right[i] == target - s:
            return True
    return False
```

**Exemple:** Partition Array Into Two Arrays to Minimize Sum Difference, Closest Subsequence Sum,
Closest Dessert Cost.

**Capcane:** 2^20 ≈ 1e6 e limita practică (memorie!); pentru n > 40 nu merge — atunci e DP sau
greedy. Duplicatele din `left`/`right` nu strică nimic, dar poți folosi un `set` ca să micșorezi
lista.

---

## 28. Grafuri avansate II (SCC, punți, Euler, max flow)

### 28.1 Componente tare conexe (Kosaraju / Tarjan)

**Când apare:** graf **orientat** și te interesează „cine ajunge la cine" simetric: numărul de
componente tare conexe, condensarea grafului (DAG-ul de componente) + ordine topologică pe el,
detectarea ciclurilor, „2-SAT".

**Ideea-cheie (Kosaraju, cel mai ușor de scris):** 1) DFS pe graful normal și reții nodurile în
ordinea **terminării** (postordine); 2) construiești graful transpus; 3) DFS pe transpus, luând
nodurile în ordinea inversă a terminării — fiecare DFS dă exact o componentă tare conexă.
`O(V + E)`.

**Schelet:**
```python
def kosaraju(n, adj):                    # adj[u] = [v] (orientat)
    order, seen = [], [False] * n
    for s in range(n):                   # 1) ordine de terminare (iterativ, ca să nu rupem stiva)
        if seen[s]:
            continue
        seen[s] = True
        stack = [(s, 0)]
        while stack:
            u, i = stack.pop()
            if i < len(adj[u]):
                stack.append((u, i + 1))
                v = adj[u][i]
                if not seen[v]:
                    seen[v] = True
                    stack.append((v, 0))
            else:
                order.append(u)

    radj = [[] for _ in range(n)]        # 2) graful transpus
    for u in range(n):
        for v in adj[u]:
            radj[v].append(u)

    comp = [-1] * n
    count = 0
    for s in reversed(order):            # 3) DFS pe transpus în ordinea inversă
        if comp[s] != -1:
            continue
        comp[s] = count
        stack = [s]
        while stack:
            u = stack.pop()
            for v in radj[u]:
                if comp[v] == -1:
                    comp[v] = count
                    stack.append(v)
        count += 1
    return count, comp                   # numărul de componente + eticheta fiecărui nod
```

**Tarjan (o singură parcurgere):** același `tin`/`low` ca la punți, dar ții o stivă de noduri „deschise"
și scoți o componentă când `low[u] == tin[u]`. Mai rapid constant, mai greu de scris corect.

**Exemple:** Number of Strongly Connected Components, Critical Connections (încălzire pentru
low-link), Course Schedule (ciclu orientat), 2-SAT, „Minimum Number of Vertices to Reach All Nodes".

**Capcane:** pe `n` mare (peste ~10^4) recursia DFSează stiva → scrie DFS iterativ. La Kosaraju,
ordinea contează: dacă parcurgi transpusul în **ordinea** terminării (nu invers), obții componente
greșite. Un nod izolat e componentă în sine; graful cu 0 noduri → 0 componente.

---

### 28.2 Punți și puncte de articulație (low-link)

**Când apare:** „care muchii/noduri sunt critice pentru conectivitate" — rețele, drumuri, dependency
graphs; „remove the edge and the network splits".

**Ideea-cheie:** un DFS ține două valori per nod: `tin[u]` = timpul de descoperire și `low[u]` =
cel mai mic `tin` accesibil din subarborele lui `u` folosind eventual o muchie înapoi. Dacă pentru
copilul `v` al lui `u` avem `low[v] > tin[u]`, muchia `u - v` nu poate fi ocolită → e **punte**.
Dacă e rădăcină cu >= 2 copii, sau are un copil cu `low[v] >= tin[u]`, atunci `u` e **punct de
articulație**. `O(V + E)`.

**Schelet (recursiv, cu id de muchie ca să tratăm corect muchiile paralele):**
```python
def bridges(n, adj):                     # adj[u] = [(v, id_muchie)], neorientat
    tin = [-1] * n
    low = [0] * n
    timer = 0
    out = []

    def dfs(u, parent_edge):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v, eid in adj[u]:
            if eid == parent_edge:       # aceeași muchie înapoi (nu nodul părinte!)
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])      # muchie înapoi
            else:
                dfs(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:      # v nu are altă cale spre u → punte
                    out.append((u, v) if u < v else (v, u))

    for s in range(n):
        if tin[s] == -1:
            dfs(s, -1)
    return sorted(out)
```

**Exemple:** Critical Connections in a Network (1192), Bridges / Articulation Points clasice.

**Capcane:** comparația cu **id-ul muchiei**, nu cu nodul părinte — la muchii paralele (`u-v` de
două ori) „ignoră nodul părinte" declară greșit punte. Pentru puncte de articulație semnul e `>=`
(`low[v] >= tin[u]`), diferența de un singur caracter. Auto-buclele nu sunt niciodată punți. Dacă
vrei răspuns unic pentru teste, impune o ordine (perechea sortată intern + lista sortată).

---

### 28.3 Drum Euler (Hierholzer)

**Când apare:** „parcurge fiecare muchie exact o dată" — reconstruirea unui itinerariu, șir de
domino, Reconstruct Itinerary (332).

**Ideea-cheie:** condiții + Hierholzer. Un **ciclu** Euler există dacă graful e conex (ignorând
nodurile izolate) și toate nodurile au grad par; un **drum** Euler există dacă exact 0 sau 2 noduri
au grad impar (plecare din cel impar). Hierholzer: mergi cu un stack, consumă muchii, iar când un
nod nu mai are muchii îl scoți în circuit — la final inversezi lista. `O(E)`.

**Schelet:**
```python
def euler_path(n, adj):                  # adj[u] = [v], muchii orientate (neconsumate)
    adj = [list(x) for x in adj]
    start = next((u for u in range(n) if adj[u]), 0)
    stack, circuit = [start], []
    while stack:
        u = stack[-1]
        if adj[u]:
            stack.append(adj[u].pop())   # consumă muchia u -> v (nu o mai folosi)
        else:
            circuit.append(stack.pop())  # u e „gata" → intră în circuit
    return circuit[::-1]
```

**Exemple:** Reconstruct Itinerary (332), Valid Arrangement of Pairs, Cracking the Safe.

**Capcane:** verifică întâi condițiile de grad, altfel obții un drum partial. Pentru drum
orientat, ordinea vecinilor decide rezultatul ∈ multe drumuri valide → sortează dacă ceri o soluție
unică. Toate muchiile trebuie să fie în aceeași componentă (altfel nu există drum care le folosește
pe toate).

---

### 28.4 Max flow (Edmonds-Karp / Dinic) și matching bipartit

**Când apare:** capacitate pe muchii — „cât poate curge", disjuncție de drumuri, proiecte/închiriere
cu cereri, **matching bipartit** (cuplaj maxim) formulat ca flow.

**Ideea-cheie:** construiești graful rezidual (`cap[u][v]` scade, `cap[v][u]` crește). **Edmonds-Karp**
= BFS pe graful rezidual și mărește pe cel mai scurt drum: `O(V * E²)`. **Dinic** = BFS pe niveluri +
DFS pe niveluri cu blocarea muchiilor: `O(V² * E)`, în practică mult mai rapid. Max flow = min cut
(teorema max-flow/min-cut). **Matching bipartit** = max flow cu sursă → stânga (cap 1), muchii
(cap 1), dreapta → sink (cap 1); alternativ **Kuhn/DFS cu augmenting paths**, mult mai scurt de
scris: `O(V * E)`.

**Schelet (Edmonds-Karp, matrice de capacități):**
```python
from collections import deque

def max_flow(cap, s, t):
    n = len(cap)
    flow = 0
    while True:
        parent = [-1] * n
        parent[s] = s
        q = deque([s])
        while q and parent[t] == -1:          # BFS pe muchii cu capacitate reziduală
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u
                    q.append(v)
        if parent[t] == -1:                   # nu mai există drum → gata
            return flow
        push, v = float("inf"), t
        while v != s:                         # minimul rezidual pe drum
            push = min(push, cap[parent[v]][v])
            v = parent[v]
        v = t
        while v != s:                         # actualizează rezidualul
            cap[parent[v]][v] -= push
            cap[v][parent[v]] += push
            v = parent[v]
        flow += push
```

**Schelet (matching bipartit cu Kuhn):**
```python
def max_matching(n_left, n_right, adj):   # adj[u] = vecinii din dreapta
    match_right = [-1] * n_right

    def augment(u, seen):
        for v in adj[u]:
            if seen[v]:
                continue
            seen[v] = True
            if match_right[v] == -1 or augment(match_right[v], seen):
                match_right[v] = u            # v e liber sau îl remaniem pe cel curent
                return True
        return False

    size = 0
    for u in range(len(adj)):
        if augment(u, [False] * n_right):
            size += 1
    return size
```

**Exemple:** Maximum Bipartite Matching, Maximum Students Taking Exam, Course Schedule III
(varianta cu cuplaj), Min Cut / Max Flow clasice.

**Capcane:** matching-ul „cel mai mare" nu se obține cu greedy (ai nevoie de augmenting paths);
`seen` se resetează pentru fiecare nod din stânga. La max flow nu modela capacitățile pe muchii
neorientate fără să le adaugi în ambele sensuri. Recursia din Kuhn are adâncime până la `n_left`
→ la sute de noduri e ok, la mii scrii iterativ.

---

## 29. Subiecte de competiție

**Când apare:** aproape niciodată la interviu — sunt tehnici din concursuri (Codeforces, ICPC,
CSES), utile dacă vrei performanță pe constrângeri mari (n, q ≈ 10⁵–10⁶) sau geometrie exactă.

**Ideea-cheie:** fiecare rezolvă o clasă îngustă de probleme cu o structură precalculată (blocuri,
linii, hull) sau prin simulare exactă. Le recunoști după **formularea constrângerilor**, nu după
enunț. Mai jos e doar o hartă de orientare: ce rezolvă, când se aplică și de ce direcție să tragi
— fără cod, nu fac parte din scopul repo-ului.

**Exemple:** Count of Range Sum (varianta offline), subsequence/knapsack pe constrângeri mari,
umezirea unei matrice celulă cu celulă.

---

### 29.1 Mo's algorithm

**Când apare:** multe întrebări **offline** pe intervale într-un array **static** („câte valori
distincte în `[l, r]`", „frecvența maximă în interval"), unde nu există structură de date simplă
(persistent segment tree) sau nu vrei să o scrii.

**Ideea-cheie:** sortezi întrebările pe **blocuri de √n** după `l`, iar în interiorul blocului
alternativ crescător/descrescător după `r` (Hilbert order e varianta și mai bună). Mutând capetele
`[l, r]` pas cu pas între întrebări consecutive, costul total e O((n + q)·√n) în loc de O(n·q).
Condiția obligatorie: să poți **adăuga/șterge** un element în O(1).

**Capcane:** dacă ștergerea nu e O(1) (ex. max cu frecvențe), ai nevoie de Mo's cu rollback sau de
altă abordare; fără sortare pe blocuri, mutarea capetelor explodează.

---

### 29.2 Convex hull trick (CHT)

**Când apare:** DP de forma `dp[i] = min_j (m_j · x_i + b_j)` unde fiecare stare anterioară
contribuie cu o **dreaptă** și întrebarea se face într-un punct `x_i`; clasic la „optimizarea
pieilor", împărțirea optimă a unui array, probleme de cost liniar.

**Ideea-cheie:** înfășurătoarea inferioară a unor drepte (un „hull" convex) se poate menține cu o
stivă dacă pantele se adaugă sortate (varianta monotonă, O(1) amortizat per întrebare) sau cu un
Li Chao tree dacă adăugările/întrebările sunt arbitrare (O(log C) per operație). Condiția de
monotonie (pante sortate, sau interogări sortate) e ce decide varianta.

**Capcane:** nu confunda maximul cu minimul (schimbi semnele); atenție la **overflow** (produse de
~10^18) și la cazul cu pante egale (păstrezi doar dreapta mai bună).

---

### 29.3 Simulare

**Când apare:** enunțul descrie exact un proces (pași, stări, grid, cozi, reguli de joc) și
așteptarea e să îl execuți fidel: umezire/umplere de matrice, autómata celulară, simulare de
procese, numărare de pași până la o condiție.

**Ideea-cheie:** nu există truc algoritmic — contează **corectitudinea detaliilor**: ordinea
actualizărilor (folosește o copie a stării dacă toate celulele se actualizează simultan), limitele
grid-ului, condiția de oprire, reprezentarea coordonatelor (offset de 1 pentru margini) și evitarea
procesării nemărginite (adaugă limită de pași / stare vizitată).

**Capcane:** mutarea in-place când pasul depinde de vecini deja modificați; simulări cu stări care
se repetă (detectează ciclul ca la Happy Number); timpul de execuție — simulează „în salturi" dacă
poți, altfel riști TLE.

---

### 29.4 Geometrie computațională

**Când apare:** puncte multe și întrebări geometrice exacte: înfășurătoarea convexă, „câte puncte
sunt în interiorul poligonului", intersecția a două segmente, aria reuniunii de dreptunghiuri,
perechea cea mai apropiată.

**Ideea-cheie:** totul se construiește pe **produse vectoriale întregi** (vezi 23.5): monotone chain
pentru convex hull (O(n log n), sortare după x apoi y), ray casting / winding number pentru „punct
în poligon", cross products cu semne pentru intersecția de segmente, sweep line pentru aria
reuniunii. Rotating calipers dă diametrul / dreptunghiul minim al unui hull în O(n).

**Capcane:** niciodată `float` pentru decizii geometrice (compară cu epsilon doar dacă inputul e
real); puncte **coliniare** și **duplicate** strică hull-ul dacă nu le tratezi explicit; cazurile
degenerate (segmente care se ating la capăt, poligon cu 1–2 puncte) trebuie acoperite separat.

---

## Tabel rezumativ — tehnică vs întrebarea-pereche

| Tehnică | Întrebarea-pereche | Complexitate tipică |
|---|---|---|
| Two Pointers | perechi/triplete, listă sortată? | O(n) |
| Sliding Window | subarray/substring cu constrângere? | O(n) |
| Fast & Slow | ciclu / middle în listă? | O(n) |
| Merge Intervals | intervale care se suprapun? | O(n log n) |
| Cyclic Sort | valori 1..n, missing/duplicate? | O(n) |
| In-place Reversal | reverse listă? | O(n) |
| Tree BFS | niveluri / shortest în tree? | O(n) |
| Tree DFS | path / sum / validate? | O(n) |
| Two Heaps | mediană / top k din stream? | O(log n) per op |
| Subsets/Combinations | *toate* posibilitățile? | 2ⁿ / n! |
| Modified BS | array rotit / căutare pe răspuns? | O(log n) |
| Topological Sort | dependențe / ordinea cursurilor? | O(V+E) |
| Union Find | componente conexe? | ≈O(1) per op |
| DP | max/min/numărare cu subprobleme? | O(n·m) |
| Greedy | alegere locală optimă global? | O(n log n) |
| Backtracking | toate soluțiile, input mic? | 2ⁿ / n! |
| BFS/DFS | parcurgere graf, conexe, cel mai scurt? | O(V+E) |
| Trie | prefixe / dicționar de cuvinte? | O(L) per operație |
| Design (LRU, Min Stack) | combini structuri deja știute? | O(1) per operație |
| Bit manipulation | XOR / măști / numărare de biți? | O(1) sau O(nr. de biți) |
| Matrice / grid 2D | spirală, rotire, parcurgere de grid? | O(m·n) |
| Grafuri avansate I | drum minim ponderat / MST? | O(E log V) |
| Math & geometrie | ciur, cmmdc, modular, geometrie? | O(log n) / O(n log log n) |
| DP avansat | knapsack / LIS / interval / măști? | O(n·W) / O(n log n) / O(2ⁿ·n) |
| Algoritmi pe stringuri | potrivire de pattern-uri în text? | O(n + m) |
| Structuri avansate | query + update pe intervale? | O(log n) per operație |
| Tehnici avansate | sweep line / deque monoton / quickselect? | O(n log n) sau O(n) amortizat |
| Grafuri avansate II | SCC / punți / max flow? | O(V+E) … O(V·E²) |
| Competiție (opțional) | Mo's, CHT, geometrie computațională? | — |
