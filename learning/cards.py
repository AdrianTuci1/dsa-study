"""Banca de carduri pentru learning area — întrebare / răspuns (recall activ).

Fiecare card are:
    id      - unic, folosit ca cheie în progresul salvat
    concept - grupa (folosită de filtrul `--concept`)
    front   - întrebarea (ce vezi înainte să răspunzi)
    back    - răspunsul scurt, cu codul-cheie
    hint    - indiciu opțional, afișat la cerere

Răspunsurile sunt scurte intenționat: înveți *skeletonul* și *triggerul*, nu
proza. Teoria lungă e în TEHNICI.md.

Adaugi un card? Lipește un `card(...)` nou în listă și rulează:
    python3 learning/trainer.py --verify
"""


def card(cid, concept, front, back, hint=""):
    return {
        "id": cid,
        "concept": concept,
        "front": front,
        "back": back,
        "hint": hint,
    }


CARDS = [
    # =====================================================================
    # 01. Array & Hashing
    # =====================================================================
    card(
        "01-01", "01 Array & Hashing",
        "Two Sum: ce verifici la fiecare element și ce stochezi în hash map?",
        "Verifici `target - x` ÎNAINTE de a insera `x`; stochezi `valoare -> index`. "
        "Un singur pass, O(n).",
        "de ce index și nu doar valoarea? ca să întorci [i, j]",
    ),
    card(
        "01-02", "01 Array & Hashing",
        "Valid Anagram: 3 metode și complexitățile?",
        "1) sort + compare O(n log n); 2) dict/Counter de frecvențe O(n); "
        "3) vector de 26 dacă alfabetul e fix O(n).",
    ),
    card(
        "01-03", "01 Array & Hashing",
        "Product of Array Except Self fără împărțire: schema?",
        "output[i] = prefix[i-1] * suffix[i+1]. Un pass stânga->dreapta pentru "
        "prefix, apoi unul dreapta->stânga care înmulțește suffixul direct în "
        "output. O(n) timp, O(1) extra (output-ul nu se pune).",
    ),
    card(
        "01-04", "01 Array & Hashing",
        "Longest Consecutive Sequence în O(n): ideea?",
        "Pui tot în `set`. Pornești numărătoarea doar dacă `x-1` NU e în set "
        "(x e început de run), apoi `while x+length in set`. Fiecare element e "
        "vizitat de câteva ori -> O(n).",
    ),
    card(
        "01-05", "01 Array & Hashing",
        "Top K Frequent Elements în O(n): ce folosești în loc de heap?",
        "Bucket sort pe frecvență: `bucket[frecv].append(val)`, apoi iei de la "
        "frecvența maximă în jos. O(n). Cu heap: O(n log k).",
    ),

    # =====================================================================
    # 02. Two Pointers
    # =====================================================================
    card(
        "02-01", "02 Two Pointers",
        "Când recunoști că merge two pointers?",
        "Array sortat (sau sortabil) + cauți o pereche/tripletă sau un interval; "
        "sau vrei O(1) spațiu pentru compactare in-place.",
        "dacă ai nevoie de toate perechile, iar O(n^2) e prea mult",
    ),
    card(
        "02-02", "02 Two Pointers",
        "3Sum: algoritmul și de ce nu dă duplicate?",
        "Sortezi; fixezi `i`; doi pointeri `l=i+1`, `r=n-1`; sum == 0 -> adaugi. "
        "Sari peste duplicate la `i`, `l` și `r` (`while l < r and nums[l] == nums[l+1]: l += 1`). "
        "O(n^2).",
    ),
    card(
        "02-03", "02 Two Pointers",
        "Container With Most Water: pe care pointer îl miști?",
        "Aria = min(h[l], h[r]) * (r - l). Miști pointerul cu înălțimea mai "
        "mică: cealaltă variantă nu poate crește aria.",
    ),
    card(
        "02-04", "02 Two Pointers",
        "Valid Palindrome: cum sari peste caracterele ne-alfanumerice?",
        "`while l < r and not s[l].isalnum(): l += 1` (la fel pentru r), apoi "
        "compari `s[l].lower() != s[r].lower()`.",
    ),

    # =====================================================================
    # 03. Sliding Window
    # =====================================================================
    card(
        "03-01", "03 Sliding Window",
        "Fereastră de dimensiune fixă k: cum o calculezi eficient?",
        "Suma primelor k; apoi pentru fiecare pas: `sum += a[r] - a[r-k]`. "
        "O(n), fără să recalculezi fereastra.",
    ),
    card(
        "03-02", "03 Sliding Window",
        "Fereastră variabilă: șablonul general?",
        "Extinzi `r`, adaugi în structura de stare; `while` fereastra e "
        "invalidă: scoți `l`, `l += 1`; actualizezi răspunsul cât timp e validă. "
        "Fiecare index intră/iese o dată -> O(n).",
    ),
    card(
        "03-03", "03 Sliding Window",
        "Minimum Window Substring: ce compari ca să știi că fereastra e validă?",
        "Două dict-uri `need` și `window` + contorul `have` (câte caractere din "
        "need sunt satisfăcute). Când `have == need`, fereastra e validă: "
        "înregistrezi și încerci să micșorezi din stânga.",
    ),
    card(
        "03-04", "03 Sliding Window",
        "Longest Repeating Character Replacement: ce caracteristică a ferestrei folosești?",
        "Fereastra e validă dacă `len(window) - max_freq <= k`. Nu trebuie să "
        "recalculezi max_freq la micșorare (max_freq poate doar crește în "
        "varianta clasică).",
    ),

    # =====================================================================
    # 04. Fast & Slow Pointers
    # =====================================================================
    card(
        "04-01", "04 Fast & Slow",
        "Linked List Cycle: cum detectezi și cum găsești intrarea în ciclu?",
        "`slow = slow.next`, `fast = fast.next.next`; dacă se întâlnesc -> ciclu. "
        "Apoi pui `slow = head` și mergi cu ambii câte un pas până se întâlnesc: "
        "acel nod e intrarea în ciclu.",
    ),
    card(
        "04-02", "04 Fast & Slow",
        "Mijlocul listei cu doi pointeri: condiția de oprire?",
        "`while fast and fast.next:` -> `slow` ajunge la mijloc. Pentru n par, "
        "al doilea mijloc (util la reorder list).",
    ),
    card(
        "04-03", "04 Fast & Slow",
        "De ce fast & slow e O(1) spațiu și O(n) timp?",
        "Nu aloci visited set; fast parcurge cel mult 2n pași, slow n. Ciclul "
        "forțează întâlnirea în cel mult `ciclu` pași.",
    ),

    # =====================================================================
    # 05. Merge Intervals
    # =====================================================================
    card(
        "05-01", "05 Merge Intervals",
        "Merge Intervals: sortare și condiție de suprapunere?",
        "Sortezi după start. Pentru fiecare interval: dacă `start <= last_end` "
        "-> `last_end = max(last_end, end)`; altfel îl adaugi ca interval nou. "
        "O(n log n).",
    ),
    card(
        "05-02", "05 Merge Intervals",
        "Insert Interval: cele 3 faze?",
        "1) adaugi intervalele care se termină înainte de noul start; "
        "2) contopești toate care se suprapun cu noul interval (extinzi "
        "start/end); 3) adaugi restul.",
    ),

    # =====================================================================
    # 06. Cyclic Sort
    # =====================================================================
    card(
        "06-01", "06 Cyclic Sort",
        "Cyclic Sort: bucla de plasare?",
        "`while nums[i] != i + 1 and 1 <= nums[i] <= n: nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]` "
        "— fiecare element ajunge la loc o dată -> O(n).",
        "atenție la ordinea de atribuire când faci swap cu index calculat",
    ),
    card(
        "06-02", "06 Cyclic Sort",
        "Cum găsești numărul lipsă / duplicat după plasare?",
        "Primul `i` cu `nums[i] != i + 1` -> lipsă `i + 1`; dacă `nums[i]` "
        "indică un index deja corect -> duplicat.",
    ),

    # =====================================================================
    # 07. In-place reversal
    # =====================================================================
    card(
        "07-01", "07 In-place Linked List Reversal",
        "Reversare listă: cei 3 pointeri și bucla?",
        "`prev = None`, `cur = head`; cât timp `cur`: `nxt = cur.next`, "
        "`cur.next = prev`, `prev = cur`, `cur = nxt`. Returnezi `prev`.",
    ),
    card(
        "07-02", "07 In-place Linked List Reversal",
        "Reverse K-Group: ce verifici înainte să inversezi un grup?",
        "Numără dacă mai există k noduri; dacă nu, lași coada neatinsă. "
        "Inversezi grupul, îl lipești înapoi și continui.",
    ),

    # =====================================================================
    # 08. Stack
    # =====================================================================
    card(
        "08-01", "08 Stack",
        "Valid Parentheses: algoritmul?",
        "Push pe stivă pentru deschise; la închisă, `pop` și verifici perechea; "
        "la final stiva trebuie goală. O(n).",
    ),
    card(
        "08-02", "08 Stack",
        "Monotonic stack pentru `next greater element`: cum arată?",
        "Stivă de indici cu valori descrescătoare: cât timp `a[stack[-1]] < a[i]` "
        "-> `result[stack.pop()] = a[i]`; apoi `push(i)`. Fiecare element e "
        "pus/scos o dată -> O(n).",
    ),
    card(
        "08-03", "08 Stack",
        "Min Stack în O(1): două variante?",
        "Stivă paralelă de minime (`mins.append(min(v, mins[-1]))`) sau perechi "
        "`(value, min_so_far)`. Ambele O(1) pe operație.",
    ),

    # =====================================================================
    # 09. Binary Search
    # =====================================================================
    card(
        "09-01", "09 Binary Search",
        "Șablonul lower-bound (primul index cu `ok(i) == True`)?",
        "`lo, hi = 0, n`; `while lo < hi: mid = (lo + hi) // 2`; dacă `ok(mid)`: "
        "`hi = mid` altfel `lo = mid + 1`; răspuns `lo` (poate fi n).",
        "invariant: răspunsul e mereu în [lo, hi]",
    ),
    card(
        "09-02", "09 Binary Search",
        "Search in Rotated Sorted Array: cum decizi ce jumătate e sortată?",
        "Compari `nums[mid]` cu `nums[lo]` ca să afli care jumătate e sortată, "
        "apoi verifici dacă targetul e în intervalul ei.",
    ),
    card(
        "09-03", "09 Binary Search",
        "Când folosești `binary search on answer`?",
        "Când funcția `feasible(x)` e monotonă (dacă merge cu x, merge și cu "
        "x+1) și cauți cel mai mic x fezabil: capacitate, viteză, zile.",
    ),

    # =====================================================================
    # 10. Tree BFS
    # =====================================================================
    card(
        "10-01", "10 Tree BFS",
        "Level Order Traversal: șablonul?",
        "`q = deque([root])`; cât timp q: `for _ in range(len(q)):` scoți nodul, "
        "adaugi copiii; nivelul curent e o listă separată.",
        "`len(q)` se fixează ÎNAINTE de bucla for",
    ),
    card(
        "10-02", "10 Tree BFS",
        "Right Side View: ce iei din fiecare nivel?",
        "Ultimul nod din fiecare nivel (sau primul, dacă privești din stânga). "
        "BFS pe niveluri.",
    ),

    # =====================================================================
    # 11. Tree DFS
    # =====================================================================
    card(
        "11-01", "11 Tree DFS",
        "Preorder / inorder / postorder: ordinea și la ce folosesc?",
        "Pre: nod, stânga, dreapta (copiere/serializare); In: stânga, nod, "
        "dreapta (BST -> sortat); Post: stânga, dreapta, nod (agregări, "
        "înălțimi).",
    ),
    card(
        "11-02", "11 Tree DFS",
        "Maximum Path Sum: ce returnezi din recursie și ce actualizezi global?",
        "Returnezi `node.val + max(0, left, right)` (o singură ramură, ca să "
        "poți continua în sus); actualizezi global `node.val + max(0,left) + max(0,right)` "
        "(ambele ramuri, pentru un drum care se închide aici).",
    ),
    card(
        "11-03", "11 Tree DFS",
        "Cum validezi un BST?",
        "Recursie cu limite `(low, high)`: `low < node.val < high`; stânga "
        "primește `(low, node.val)`, dreapta `(node.val, high)`.",
    ),

    # =====================================================================
    # 12. Two Heaps
    # =====================================================================
    card(
        "12-01", "12 Two Heaps",
        "Median din stream: structura și rebalansarea?",
        "Max-heap pentru jumătatea mică (valori negate), min-heap pentru cea "
        "mare. Inserare în unul, apoi mut un vârf în celălalt dacă diferența de "
        "mărime > 1. Median = vârf / media vârfurilor.",
    ),
    card(
        "12-02", "12 Two Heaps",
        "Kth Largest în stream: ce heap și ce dimensiune?",
        "Min-heap de dimensiune k; vârful e al k-lea cel mai mare. "
        "O(log k) per inserare.",
    ),

    # =====================================================================
    # 13. Backtracking
    # =====================================================================
    card(
        "13-01", "13 Backtracking",
        "Șablonul backtracking?",
        "`def bt(start, path): if cond: res.append(path[:]); return` ; pentru "
        "fiecare candidat valid: `path.append(x)`, `bt(...)`, `path.pop()`.",
        "choose -> explore -> unchoose",
    ),
    card(
        "13-02", "13 Backtracking",
        "Ce înseamnă pruning și când poți face `break`?",
        "Tai ramuri care nu mai pot duce la soluție. Dacă inputul e sortat, "
        "poți `break` când suma depășește targetul (restul e și mai mare).",
    ),
    card(
        "13-03", "13 Backtracking",
        "De ce `res.append(path[:])` și nu `res.append(path)`?",
        "`path` e același obiect mutat de `append/pop`; fără copie toate "
        "rezultatele ar arăta identic (ultima stare). `[:]` salvează o copie la "
        "momentul respectiv.",
    ),

    # =====================================================================
    # 14. Graph BFS / DFS
    # =====================================================================
    card(
        "14-01", "14 Graph BFS/DFS",
        "Unde marchezi un nod ca vizitat și de ce contează?",
        "La BFS: când îl pui în coadă (altfel îl adaugi de mai multe ori). "
        "La DFS: la intrare. Fără asta -> muncă exponențială/recursie infinită.",
    ),
    card(
        "14-02", "14 Graph BFS/DFS",
        "Number of Islands: cum marchezi insula?",
        "DFS/BFS din fiecare `1` găsit, transformând celulele în `0` (in-place) "
        "sau cu visited. Numărul de porniri = numărul de insule.",
    ),
    card(
        "14-03", "14 Graph BFS/DFS",
        "Clone Graph: ce map ții?",
        "`old -> new`; creezi copia nodului când îl vezi prima dată, apoi "
        "populezi vecinii recursiv. Map-ul previne ciclurile infinite.",
    ),

    # =====================================================================
    # 15. Topological Sort
    # =====================================================================
    card(
        "15-01", "15 Topological Sort",
        "Kahn (BFS) pentru topological sort: pașii?",
        "Calculezi `indegree`; pui în coadă toate nodurile cu indegree 0; scoți "
        "un nod, îl adaugi în ordine, decrementezi vecinii și pui în coadă ce "
        "ajunge la 0. Dacă ordinea are < n noduri -> există ciclu.",
    ),
    card(
        "15-02", "15 Topological Sort",
        "DFS cu 3 culori pentru detectarea ciclului?",
        "alb = nevizitat, gri = în stiva curentă, negru = terminat. Muchie "
        "către un nod gri -> ciclu. Postordine inversată = ordine topologică.",
    ),

    # =====================================================================
    # 16. Union Find
    # =====================================================================
    card(
        "16-01", "16 Union Find",
        "Find cu path compression și union by size?",
        "`find(x)`: dacă `parent[x] != x`, `parent[x] = find(parent[x])`; returnezi "
        "`parent[x]`. Union: atașezi rădăcina arborelui mai mic la cel mare. "
        "Aproape O(1) amortizat.",
    ),
    card(
        "16-02", "16 Union Find",
        "Graph Valid Tree: cele două condiții?",
        "Exact `n - 1` muchii ȘI nicio muchie nu unește două noduri deja în "
        "aceeași componentă (altfel ciclu).",
    ),

    # =====================================================================
    # 17. Dynamic Programming
    # =====================================================================
    card(
        "17-01", "17 Dynamic Programming",
        "Când e DP și când e greedy?",
        "DP când decizia locală depinde de stări viitoare / ai nevoie de toate "
        "combinațiile; greedy când o alegere locală optimă se dovedește global "
        "optimă (exchange argument).",
    ),
    card(
        "17-02", "17 Dynamic Programming",
        "House Robber: recurența?",
        "`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`; două variabile, O(n) timp / "
        "O(1) spațiu. `dp[-1] = dp[-2] = 0`.",
    ),
    card(
        "17-03", "17 Dynamic Programming",
        "Unique Paths: recurența și optimizarea de spațiu?",
        "`dp[r][c] = dp[r-1][c] + dp[r][c-1]`, prima linie/coloană = 1. "
        "Rolling array pe o linie, stânga->dreapta: O(mn) timp, O(n) spațiu.",
    ),
    card(
        "17-04", "17 Dynamic Programming",
        "Longest Common Subsequence: recurența?",
        "Dacă `a[i-1] == b[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`; altfel "
        "`max(dp[i-1][j], dp[i][j-1])`. Se poate face cu 2 linii.",
    ),
    card(
        "17-05", "17 Dynamic Programming",
        "Coin Change: ce înseamnă `dp[x]` și cum se inițializează?",
        "`dp[x]` = numărul minim de monede pentru suma x; `dp[0] = 0`, restul "
        "`inf`; pentru fiecare monedă și sumă: `dp[s] = min(dp[s], dp[s-c] + 1)`.",
        "se poate și cu bucla pe sumă în exterior (unbounded knapsack)",
    ),

    # =====================================================================
    # 18. Greedy
    # =====================================================================
    card(
        "18-01", "18 Greedy",
        "Jump Game: ce înseamnă `reach`?",
        "Cel mai departe index accesibil. Dacă `i > reach` -> imposibil; "
        "`reach = max(reach, i + nums[i])`. O(n), O(1).",
    ),
    card(
        "18-02", "18 Greedy",
        "Gas Station: condiția de existență și alegerea startului?",
        "Există circuit dacă `sum(gas) >= sum(cost)`. Dacă da, startul e stația "
        "de după ultimul punct în care rezervorul a devenit negativ.",
    ),
    card(
        "18-03", "18 Greedy",
        "Best Time to Buy and Sell Stock II: de ce suma diferențelor pozitive?",
        "Tranzacții nelimitate: fiecare urcare poate fi încasată. Vânzarea "
        "înainte de o scădere și recumpărarea mai jos nu e niciodată mai rea.",
    ),

    # =====================================================================
    # 19. Tries
    # =====================================================================
    card(
        "19-01", "19 Tries",
        "Structura unui trie?",
        "Nod = dict `copil_character -> nod` + flag `end` (cheie sentinel). "
        "Insert/search/startsWith parcurg caracterele: O(len(word)).",
    ),
    card(
        "19-02", "19 Tries",
        "Word Search II: de ce trie + DFS pe board?",
        "Trie-ul taie imediat ramurile care nu duc la niciun cuvânt; DFS pe "
        "celule cu marcare `#` pentru a nu refolosi celula. Altfel, cauți fiecare "
        "cuvânt separat -> prea lent.",
    ),
    card(
        "19-03", "19 Tries",
        "Wildcard '.' în search: cum adaptezi trie-ul?",
        "La '.', ramifici pe toți copiii (DFS/backtracking), nu doar pe unul. "
        "Restul e identic; la final verifici flag-ul `end`.",
    ),

    # =====================================================================
    # 20. Design
    # =====================================================================
    card(
        "20-01", "20 Design",
        "LRU Cache: varianta Python și cea „de interviu”?",
        "Python: `OrderedDict`, `move_to_end(key)` la get/put, "
        "`popitem(last=False)` la evict. Interviu: hash map + listă dublu "
        "înlănțuită (O(1) mutare la capăt).",
    ),
    card(
        "20-02", "20 Design",
        "Min Stack: de ce nu poți ține doar `min()` la getMin?",
        "După `pop` trebuie să revii la minimul anterior, deci ai nevoie de "
        "istoric: stivă paralelă de minime sau perechi `(value, min_so_far)`.",
    ),
    card(
        "20-03", "20 Design",
        "Queue din două stive: de ce e O(1) amortizat?",
        "`push` în inbox; `pop/peek` doar când outbox e gol, torni tot din "
        "inbox în outbox. Fiecare element e mutat cel mult o dată.",
    ),

    # =====================================================================
    # 21. Bit Manipulation
    # =====================================================================
    card(
        "21-01", "21 Bit Manipulation",
        "Single Number: de ce XOR?",
        "`x ^ x = 0`, `x ^ 0 = x`, XOR e comutativ/asociativ -> perechile se "
        "anulează, rămâne valoarea unică. O(n) timp, O(1) spațiu.",
    ),
    card(
        "21-02", "21 Bit Manipulation",
        "Ce face `n & (n - 1)`?",
        "Șterge cel mai puțin semnificativ bit de 1. De aici: numărul de biți 1 "
        "(`while n: n &= n-1; count += 1`) și testul de putere a lui 2 "
        "(`n > 0 and n & (n-1) == 0`).",
    ),
    card(
        "21-03", "21 Bit Manipulation",
        "Reverse Bits 32: algoritmul?",
        "De 32 de ori: `result = (result << 1) | (n & 1)`, `n >>= 1`. Bitul i "
        "ajunge la 31 - i.",
    ),
    card(
        "21-04", "21 Bit Manipulation",
        "Măști utile: cum testezi/setezi/ștergi bitul k?",
        "test: `(x >> k) & 1`; set: `x | (1 << k)`; clear: `x & ~(1 << k)`; "
        "toggle: `x ^ (1 << k)`.",
    ),

    # =====================================================================
    # 22. Matrix
    # =====================================================================
    card(
        "22-01", "22 Matrix",
        "Spiral Matrix: schema cu 4 pereți?",
        "`top, bottom, left, right`; parcurgi sus, dreapta, jos, stânga și "
        "strângi pereții. După primele două laturi re-verifici "
        "`top <= bottom` / `left <= right` (o linie/coloană rămasă).",
    ),
    card(
        "22-02", "22 Matrix",
        "Rotate Image 90° clockwise in place: transformarea?",
        "Transpose (`zip(*m)`) + reverse fiecare rând, adică "
        "`m[:] = [list(r) for r in zip(*m[::-1])]`. `m[:] =` păstrează obiectul.",
    ),
    card(
        "22-03", "22 Matrix",
        "Set Matrix Zeroes cu O(1) extra spațiu: trucul?",
        "Prima linie și prima coloană devin marcatori. Ții separat două booleene "
        "pentru dacă prima linie/coloană trebuie zeroizate (altfel marcatorii "
        "distrug informația).",
    ),

    # =====================================================================
    # 23. Grafuri avansate I
    # =====================================================================
    card(
        "23-01", "23 Grafuri avansate I",
        "Dijkstra cu heap: structura și de ce nu merge cu ponderi negative?",
        "`dist[] = inf`, `dist[src] = 0`, heap `(dist, nod)`; scoți minimul, "
        "ignori intrările învechite (`d > dist[u]`), relaxezi vecinii. Cu ponderi "
        "negative, un nod finalizat poate fi îmbunătățit ulterior -> folosește "
        "Bellman-Ford.",
    ),
    card(
        "23-02", "23 Grafuri avansate I",
        "Bellman-Ford cu „cel mult K opriri”: de ce copiezi distanțele?",
        "O rundă = un zbor în plus. Dacă relaxezi în aceeași rundă, poți folosi "
        "un drum de K+2 muchii. Rulezi `k + 1` runde, relaxând dintr-o copie.",
    ),
    card(
        "23-03", "23 Grafuri avansate I",
        "MST: Prim sau Kruskal?",
        "Prim O(n^2) pe graf dense (matrice de distanțe, fără sortarea a n^2 "
        "muchii); Kruskal O(E log E) + DSU pe graf rare. Ambele greedy.",
    ),

    # =====================================================================
    # 24. Math & Geometry
    # =====================================================================
    card(
        "24-01", "24 Math & Geometry",
        "Ciurul lui Eratostene: pașii și complexitatea?",
        "`sieve[0..1] = False`; pentru p de la 2 cât timp `p*p < n`, dacă "
        "`sieve[p]`, marchezi `p*p, p*p+p, ...` ca false. O(n log log n).",
    ),
    card(
        "24-02", "24 Math & Geometry",
        "Fast exponentiation: recurența / bucla?",
        "`x^n = (x^2)^(n/2)` dacă n par, altfel `x * x^(n-1)`. Iterativ: cât timp "
        "n, dacă `n & 1` înmulțești rezultatul cu baza, apoi `base *= base`, "
        "`n >>= 1`. O(log n).",
    ),
    card(
        "24-03", "24 Math & Geometry",
        "Happy Number: de ce Floyd și nu `set`?",
        "Suma pătratelor cifrelor e o funcție pe întregi -> graf funcțional cu "
        "ciclu. Floyd găsește ciclul cu O(1) spațiu; happy dacă ciclul e `1`.",
    ),
    card(
        "24-04", "24 Math & Geometry",
        "GCD: algoritmul Euclid?",
        "`gcd(a, b) = gcd(b, a % b)` până când b == 0 -> a. Pentru listă: "
        "`reduce(gcd, nums)`. `lcm(a, b) = a // gcd(a, b) * b`.",
    ),

    # =====================================================================
    # 25. DP avansat
    # =====================================================================
    card(
        "25-01", "25 DP avansat",
        "0/1 Knapsack cu 1-D: de ce bucla pe capacitate merge descrescător?",
        "Dacă mergi crescător, `dp[c-w]` a fost deja actualizat pentru itemul "
        "curent -> ai lua itemul de mai multe ori. Descrescător citești doar "
        "rândul anterior -> 0/1. O(nW) timp, O(W) spațiu.",
    ),
    card(
        "25-02", "25 DP avansat",
        "LIS în O(n log n): ce ții în `tails` și de ce `bisect_left`?",
        "`tails[k]` = cea mai mică coadă posibilă a unei subsecvențe crescătoare "
        "de lungime k+1. Înlocuiești primul element `>= x` cu x (sau adaugi x). "
        "`tails` NU e o subsecvență validă, doar lungimea ei contează.",
        "pentru strict crescător: bisect_left; pentru nedescrescător: bisect_right",
    ),
    card(
        "25-03", "25 DP avansat",
        "Edit Distance: recurența și cazurile de bază?",
        "Egalitate -> `dp[i-1][j-1]`; altfel `1 + min(dp[i-1][j]` delete, "
        "`dp[i][j-1]` insert, `dp[i-1][j-1]` replace)`. Rândul 0 = 0..n, "
        "coloana 0 = 0..m.",
    ),
    card(
        "25-04", "25 DP avansat",
        "Ce e interval DP și cum arată ordinea buclelor?",
        "`dp[i][j]` pentru un interval; iterezi după LUNGIMEA intervalului "
        "(crescător), apoi punctul de tăiere k. Ex: burst balloons, "
        "longest palindromic subsequence, matrix chain.",
    ),

    # =====================================================================
    # 26. Stringuri
    # =====================================================================
    card(
        "26-01", "26 Stringuri",
        "KMP: ce e tabelul de prefix și de ce dă O(n + m)?",
        "`lps[i]` = lungimea celui mai lung prefix propriu care e și sufix al "
        "patternului până la i. La nepotrivire, sari la `lps[j-1]` în loc să "
        "reporni de la 0 -> fiecare caracter e comparat O(1) amortizat.",
    ),
    card(
        "26-02", "26 Stringuri",
        "Rabin-Karp: cum obții hash-ul ferestrei în O(1)?",
        "Hash rulant: `h = h * base + c` (mod M); la fereastra următoare scazi "
        "`c_out * base^(L-1)` și adaugi `c_in`. Verifici egalitatea reală doar "
        "când hash-urile coincid (coliziuni).",
    ),

    # =====================================================================
    # 27. Structuri avansate
    # =====================================================================
    card(
        "27-01", "27 Structuri avansate",
        "Fenwick (BIT): ce faci cu `i & -i`?",
        "`i & -i` izolează cel mai puțin semnificativ bit de 1, adică săritura "
        "în arborele de sume: la update `i += i & -i`, la query `i -= i & -i`. "
        "O(log n).",
    ),
    card(
        "27-02", "27 Structuri avansate",
        "Segment tree vs sparse table: când le folosești?",
        "Segment tree: update-uri și query-uri, O(log n) ambele. Sparse table: "
        "doar static (fără update), query O(1) după O(n log n) preprocessing; "
        "merge doar funcții idempotente (min, max, gcd).",
    ),

    # =====================================================================
    # 28. Tehnici avansate
    # =====================================================================
    card(
        "28-01", "28 Tehnici avansate",
        "Monotonic deque pentru sliding window maximum: ce ții în deque?",
        "Indici cu valori descrescătoare; înainte de a adăuga x, scoți din spate "
        "tot ce e `<= x`; din față scoți indicii ieșiți din fereastră. "
        "Maximul e `a[dq[0]]`. O(n) total.",
    ),
    card(
        "28-02", "28 Tehnici avansate",
        "Quickselect: complexitate și de ce e mai bun decât sortarea?",
        "Partiționezi ca la quicksort dar continui doar în partea care conține "
        "poziția k -> O(n) mediu, O(n^2) worst. Sortarea ar fi O(n log n).",
    ),

    # =====================================================================
    # 29. Grafuri avansate II
    # =====================================================================
    card(
        "29-01", "29 Grafuri avansate II",
        "Tarjan SCC: ce e `low-link`?",
        "`low[u]` = cel mai mic `disc` accesibil din subarborele lui u folosind "
        "muchii de arbore + una înapoi. Dacă `low[u] == disc[u]`, u e rădăcina "
        "unei componente tare conexe (scoți stiva până la u).",
    ),
    card(
        "29-02", "29 Grafuri avansate II",
        "Cum găsești punțile (bridges) într-un graf?",
        "DFS cu `disc`/`low`; muchia (u, v) e punte dacă `low[v] > disc[u]`. "
        "Funcționează și pentru puncte de articulație (condiții pe copii).",
    ),
    card(
        "29-03", "29 Grafuri avansate II",
        "Matching bipartit maxim: ce algoritm și complexitate?",
        "Hopcroft-Karp O(E sqrt(V)) (sau Kuhn O(VE) mai simplu). Alternezi "
        "drumuri de augmentare între cele două partiții.",
    ),

    # =====================================================================
    # 00. Python esențial pentru DSA
    # =====================================================================
    card(
        "py-01", "00 Python esențial",
        "Ce face `a[:1]` și ce face `a[1]`?",
        "`a[:1]` = felie de la 0 până la 1 (exclusiv) -> LISTĂ cu primul "
        "element. `a[1]` = elementul de pe poziția 1. `[:1]` nu înseamnă "
        "„elementul 1”.",
    ),
    card(
        "py-02", "00 Python esențial",
        "Cum se citește `a[1][:]`?",
        "De la stânga la dreapta: întâi `a[1]` (al doilea element), apoi `[:]` "
        "pe el -> copie superficială a acelui element. Pe listă dă listă nouă; "
        "pe string dă același string.",
    ),
    card(
        "py-03", "00 Python esențial",
        "`b = a[:]` vs `b = a`: ce copiază fiecare?",
        "`b = a` -> două nume pentru același obiect (alias). `b = a[:]` -> listă "
        "nouă, DAR cu aceleași elemente (copie superficială). Pentru matrice: "
        "`[row[:] for row in a]`.",
    ),
    card(
        "py-04", "00 Python esențial",
        "De ce `res.append(path[:])` în backtracking?",
        "`path` e mutat de append/pop; fără `[:]` toate rezultatele sunt "
        "referințe la aceeași listă și arăta identic la final.",
    ),
    card(
        "py-05", "00 Python esențial",
        "`deque` vs `list` pentru coadă: de ce `deque`?",
        "`list.pop(0)` e O(n) (mută toate elementele); `deque.popleft()` e O(1). "
        "Pentru BFS și sliding window folosește `collections.deque`.",
    ),
    card(
        "py-06", "00 Python esențial",
        "`heapq` e min-heap: cum obții max-heap?",
        "Adaugi valori negate: `heappush(h, -x)`, maximul e `-h[0]`. Pentru "
        "pereche (prioritate, valoare) heap-ul compară lexicografic.",
    ),
    card(
        "py-07", "00 Python esențial",
        "`bisect_left` vs `bisect_right`: când le folosești?",
        "Ambele O(log n). `bisect_left` = primul index cu `a[i] >= x` "
        "(înlocuire pentru strict crescător); `bisect_right` = primul cu "
        "`a[i] > x` (pentru secvențe nedescrescătoare).",
    ),
    card(
        "py-08", "00 Python esențial",
        "Ce fac `Counter`, `defaultdict` și `enumerate`?",
        "`Counter(iterable)` numără frecvențele (`.most_common(k)`); "
        "`defaultdict(list/int)` elimină `if key not in d`; "
        "`enumerate(a)` dă `(index, valoare)`.",
    ),
    card(
        "py-09", "00 Python esențial",
        "Cum inversezi o listă / un string?",
        "`a[::-1]` (felie cu pas -1) dă o copie inversată; `a.reverse()` "
        "inversează in place și returnează None; `reversed(a)` dă iterator.",
    ),
    card(
        "py-10", "00 Python esențial",
        "Cum copiezi o listă de liste (matrice) corect?",
        "`[row[:] for row in a]` sau `[list(row) for row in a]` sau "
        "`copy.deepcopy(a)` dacă elementele sunt mutabile. `a[:]` copiază doar "
        "nivelul exterior.",
    ),
]

# Cuvinte-cheie pentru filtrul `--concept` (un concept poate avea mai multe).
# Astfel `--concept dp` prinde atât "17 Dynamic Programming" cât și "25 DP avansat",
# fără să depindă de diacritice sau de formularea din titlu.
CONCEPT_KEYS = {
    "00 Python esențial": "python slicing copy list dict essentials",
    "01 Array & Hashing": "array hashing hashmap hash freq",
    "02 Two Pointers": "two pointers palindrome 3sum",
    "03 Sliding Window": "sliding window substring",
    "04 Fast & Slow": "fast slow cycle linked list tortoise",
    "05 Merge Intervals": "merge intervals",
    "06 Cyclic Sort": "cyclic sort missing duplicate",
    "07 In-place Linked List Reversal": "reverse linked list inplace k-group",
    "08 Stack": "stack monotonic parentheses",
    "09 Binary Search": "binary search rotated lower bound answer",
    "10 Tree BFS": "tree bfs level order queue",
    "11 Tree DFS": "tree dfs recursion inorder bst",
    "12 Two Heaps": "heap heaps median priority queue",
    "13 Backtracking": "backtracking subsets combinations permutations",
    "14 Graph BFS/DFS": "graph bfs dfs islands grid",
    "15 Topological Sort": "topological sort kahn indegree dependencies",
    "16 Union Find": "union find dsu disjoint set components",
    "17 Dynamic Programming": "dp dynamic programming 1d 2d recurrence",
    "18 Greedy": "greedy",
    "19 Tries": "trie prefix tree",
    "20 Design": "design lru cache min stack queue",
    "21 Bit Manipulation": "bit manipulation xor masks bits",
    "22 Matrix": "matrix grid spiral rotate zeroes 2d",
    "23 Grafuri avansate I": "graph advanced dijkstra bellman ford mst prim kruskal shortest path",
    "24 Math & Geometry": "math geometry sieve primes pow gcd happy",
    "25 DP avansat": "dp advanced knapsack lis edit distance interval bitmask",
    "26 Stringuri": "string kmp rabin karp manacher z",
    "27 Structuri avansate": "segment tree fenwick sparse table bit",
    "28 Tehnici avansate": "deque monotonic quickselect sweep line",
    "29 Grafuri avansate II": "graph scc tarjan bridges matching bipartite",
}


def verify():
    """Verifică banca de carduri. Returnează lista de probleme (goală = ok)."""
    problems = []
    seen = set()
    for c in CARDS:
        cid = c.get("id", "")
        if not cid:
            problems.append("card fără id: %r" % (c.get("front", "")[:40],))
        elif cid in seen:
            problems.append("id duplicat: %s" % cid)
        seen.add(cid)
        for field in ("concept", "front", "back"):
            if not c.get(field):
                problems.append("%s: câmpul %s e gol" % (cid, field))
        if c.get("concept") and c["concept"] not in CONCEPT_KEYS:
            problems.append("%s: conceptul %r nu are intrare în CONCEPT_KEYS"
                            % (cid, c["concept"]))
    if not CARDS:
        problems.append("banca de carduri e goală")
    return problems


if __name__ == "__main__":
    problems = verify()
    counts = {}
    for c in CARDS:
        counts[c["concept"]] = counts.get(c["concept"], 0) + 1
    print("Carduri: %d, concepte: %d" % (len(CARDS), len(counts)))
    for concept in sorted(counts):
        print("  %-28s %2d" % (concept, counts[concept]))
    if problems:
        print("\nProbleme:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    print("\nOK")
