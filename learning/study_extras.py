"""Extra drill items for the DSA study app.

46 items: 18 multiple choice, 14 code fill-in, 14 trace.
Each item complements the flashcards: read code carefully, recall templates.
"""

EXTRA_ITEMS = [
    # ------------------------------------------------------------------
    # 00 Python Essentials
    # ------------------------------------------------------------------
    {
        "id": "ch-01",
        "concept": "00 Python Essentials",
        "type": "choice",
        "question": "a is a list of lists and you run b = a[:]. What did you just copy?",
        "options": [
            "Only the outer list; the inner lists are shared",
            "Every nested list, recursively",
            "A tuple of the inner lists",
            "Nothing; b is the same object as a",
        ],
        "answer": 0,
        "explain": "A slice copies the outer list, so b and a share the same inner lists.",
    },
    {
        "id": "trace-01",
        "concept": "00 Python Essentials",
        "type": "trace",
        "prompt": "What does a evaluate to after this code runs?",
        "setup": "a = [1, 2, 3]\nb = a\nb += [4]",
        "expr": "a",
        "explain": "The += operator mutates the list in place, so a and b remain the same object.",
    },
    # ------------------------------------------------------------------
    # 01 Arrays & Hashing
    # ------------------------------------------------------------------
    {
        "id": "ch-02",
        "concept": "01 Arrays & Hashing",
        "type": "choice",
        "question": "In one-pass Two Sum, when should the current value be inserted into the hash map?",
        "options": [
            "After checking for its complement",
            "Before checking for its complement",
            "Only after the loop ends",
            "Only when the complement is missing",
        ],
        "answer": 0,
        "explain": "Inserting first would let an element pair with itself when target is twice its value.",
    },
    {
        "id": "code-01",
        "concept": "01 Arrays & Hashing",
        "type": "code",
        "prompt": "Fill in the line that records the current value so later elements can pair with it.",
        "code": "seen = {}\nfor i, x in enumerate(nums):\n    need = target - x\n    if need in seen:\n        return [seen[need], i]\n    ___\nreturn []",
        "answers": ["seen[x] = i"],
        "explain": "The index is stored after the lookup so an element cannot match itself.",
    },
    # ------------------------------------------------------------------
    # 02 Two Pointers
    # ------------------------------------------------------------------
    {
        "id": "ch-03",
        "concept": "02 Two Pointers",
        "type": "choice",
        "question": "On a sorted array, nums[lo] + nums[hi] is smaller than the target. Which pointer should move?",
        "options": [
            "lo += 1",
            "hi -= 1",
            "Both pointers",
            "Neither pointer",
        ],
        "answer": 0,
        "explain": "Moving lo right is the only move that can increase the sum.",
    },
    {
        "id": "code-02",
        "concept": "02 Two Pointers",
        "type": "code",
        "prompt": "Fill in the pointer update in the container-with-most-water scan.",
        "code": "lo, hi = 0, len(h) - 1\nbest = 0\nwhile lo < hi:\n    best = max(best, (hi - lo) * min(h[lo], h[hi]))\n    if h[lo] < h[hi]:\n        ___\n    else:\n        hi -= 1\nreturn best",
        "answers": ["lo += 1"],
        "explain": "Moving the shorter wall inward is the only move that can raise the area.",
    },
    # ------------------------------------------------------------------
    # 03 Sliding Window
    # ------------------------------------------------------------------
    {
        "id": "ch-04",
        "concept": "03 Sliding Window",
        "type": "choice",
        "question": "In a variable-size sliding window, why is the shrink step a while loop rather than an if?",
        "options": [
            "Several left moves may be needed to make the window valid",
            "A while loop is faster than an if",
            "An if cannot change the left pointer",
            "The window must keep a fixed size",
        ],
        "answer": 0,
        "explain": "One removal is not always enough, so keep shrinking until the window is valid.",
    },
    {
        "id": "trace-02",
        "concept": "03 Sliding Window",
        "type": "trace",
        "prompt": "What is the largest window sum of length 3 found by this loop?",
        "setup": "nums = [2, 1, 5, 1, 3, 2]\nk = 3\nwindow = 0\nbest = 0\nfor i, x in enumerate(nums):\n    window += x\n    if i >= k:\n        window -= nums[i - k]\n    best = max(best, window)",
        "expr": "best",
        "explain": "The window slides by adding the new value and dropping the value k positions back; the best window is [1, 5, 3].",
    },
    {
        "id": "code-03",
        "concept": "03 Sliding Window",
        "type": "code",
        "prompt": "Fill in the line that moves the left edge past a repeated character.",
        "code": "last = {}\nleft = 0\nbest = 0\nfor right, ch in enumerate(s):\n    if ch in last and last[ch] >= left:\n        ___\n    last[ch] = right\n    best = max(best, right - left + 1)\nreturn best",
        "answers": ["left = last[ch] + 1"],
        "explain": "The window restarts just after the previous position of the repeated character.",
    },
    # ------------------------------------------------------------------
    # 04 Fast & Slow Pointers
    # ------------------------------------------------------------------
    {
        "id": "ch-05",
        "concept": "04 Fast & Slow Pointers",
        "type": "choice",
        "question": "Floyd's algorithm reports that slow and fast met at node M. How do you find the entry of the cycle?",
        "options": [
            "Reset one pointer to head and move both one step at a time",
            "Move fast two steps and slow one step from M",
            "Reverse the list from M",
            "The entry is always the node after M",
        ],
        "answer": 0,
        "explain": "The distance from head to the entry equals the distance from M to the entry.",
    },
    # ------------------------------------------------------------------
    # 05 Merge Intervals
    # ------------------------------------------------------------------
    {
        "id": "trace-03",
        "concept": "05 Merge Intervals",
        "type": "trace",
        "prompt": "What does merged contain after this pass?",
        "setup": "intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]\nmerged = []\nfor s, e in intervals:\n    if merged and s <= merged[-1][1]:\n        merged[-1][1] = max(merged[-1][1], e)\n    else:\n        merged.append([s, e])",
        "expr": "merged",
        "explain": "Overlapping intervals extend the last merged end; the gaps start new intervals.",
    },
    {
        "id": "code-04",
        "concept": "05 Merge Intervals",
        "type": "code",
        "prompt": "Fill in the line that absorbs the current interval into the new one.",
        "code": "def insert(intervals, new):\n    res, i, n = [], 0, len(intervals)\n    while i < n and intervals[i][1] < new[0]:\n        res.append(intervals[i])\n        i += 1\n    while i < n and intervals[i][0] <= new[1]:\n        ___\n        i += 1\n    res.append(new)\n    return res + intervals[i:]",
        "answers": [
            "new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]",
            "new[0], new[1] = min(new[0], intervals[i][0]), max(new[1], intervals[i][1])",
        ],
        "explain": "Each overlapping interval widens the new interval on its left or right side.",
    },
    # ------------------------------------------------------------------
    # 06 Cyclic Sort
    # ------------------------------------------------------------------
    {
        "id": "code-05",
        "concept": "06 Cyclic Sort",
        "type": "code",
        "prompt": "Fill in the line that puts the current value at its home index.",
        "code": "def cyclic_sort(nums):\n    i = 0\n    while i < len(nums):\n        j = nums[i] - 1\n        if nums[i] != nums[j]:\n            ___\n        else:\n            i += 1\n    return nums",
        "answers": ["nums[i], nums[j] = nums[j], nums[i]"],
        "explain": "The swap places the value correctly but does not advance i, so the new value is checked too.",
    },
    # ------------------------------------------------------------------
    # 07 In-Place Linked List Reversal
    # ------------------------------------------------------------------
    {
        "id": "trace-04",
        "concept": "07 In-Place Linked List Reversal",
        "type": "trace",
        "prompt": "After the loop, what are the first three values of the reversed list?",
        "setup": "nodes = [[v, None] for v in [1, 2, 3, 4]]\nfor a, b in zip(nodes, nodes[1:]):\n    a[1] = b\nprev, cur = None, nodes[0]\nwhile cur:\n    nxt = cur[1]\n    cur[1] = prev\n    prev, cur = cur, nxt",
        "expr": "[prev[0], prev[1][0], prev[1][1][0]]",
        "explain": "Each next pointer is redirected to the previous node, so the old tail becomes the new head.",
    },
    # ------------------------------------------------------------------
    # 08 Stack
    # ------------------------------------------------------------------
    {
        "id": "ch-06",
        "concept": "08 Stack",
        "type": "choice",
        "question": "While checking balanced brackets, when does a closing bracket pop the stack?",
        "options": [
            "When it matches the current top",
            "When the stack is empty",
            "When the previous character was also a closer",
            "It never pops; the stack is only appended",
        ],
        "answer": 0,
        "explain": "The top holds the most recent unmatched opener, which must be of the matching type.",
    },
    {
        "id": "trace-05",
        "concept": "08 Stack",
        "type": "trace",
        "prompt": "What does the stack hold after the loop?",
        "setup": "stack = []\nfor x in [5, 3, 8, 1]:\n    while stack and stack[-1] < x:\n        stack.pop()\n    stack.append(x)",
        "expr": "stack",
        "explain": "The stack keeps a decreasing sequence; smaller tops are removed before the new value is pushed.",
    },
    # ------------------------------------------------------------------
    # 09 Binary Search
    # ------------------------------------------------------------------
    {
        "id": "ch-07",
        "concept": "09 Binary Search",
        "type": "choice",
        "question": "bisect_left(a, x) and bisect_right(a, x) return different indices when:",
        "options": [
            "x already appears in a",
            "x is smaller than every element",
            "a is empty",
            "x is larger than every element",
        ],
        "answer": 0,
        "explain": "left gives the first position of x, right gives the position just after the last x.",
    },
    {
        "id": "code-06",
        "concept": "09 Binary Search",
        "type": "code",
        "prompt": "Fill in the upper-bound update. It must keep every value greater than x in the range.",
        "code": "lo, hi = 0, n\nwhile lo < hi:\n    mid = (lo + hi) // 2\n    if a[mid] <= x:\n        ___\n    else:\n        hi = mid",
        "answers": ["lo = mid + 1"],
        "explain": "Upper bound skips every value less than or equal to x, so lo ends just past the last x.",
    },
    # ------------------------------------------------------------------
    # 10 Tree BFS
    # ------------------------------------------------------------------
    {
        "id": "ch-08",
        "concept": "10 Tree BFS",
        "type": "choice",
        "question": "Why capture size = len(queue) before processing a level in tree BFS?",
        "options": [
            "The queue grows as children are added, so size marks the level boundary",
            "To keep the queue sorted by depth",
            "To skip the visited set",
            "Because len(queue) is expensive inside the loop",
        ],
        "answer": 0,
        "explain": "The captured size fixes how many nodes belong to the current level.",
    },
    # ------------------------------------------------------------------
    # 11 Tree DFS
    # ------------------------------------------------------------------
    {
        "id": "trace-06",
        "concept": "11 Tree DFS",
        "type": "trace",
        "prompt": "What is the depth of this tree?",
        "setup": "def depth(node):\n    if node is None:\n        return 0\n    return 1 + max(depth(node[1]), depth(node[2]))\ntree = (1, (2, (4, None, None), None), (3, None, None))",
        "expr": "depth(tree)",
        "explain": "Each call adds one level and follows the deeper child; the longest path is 1 -> 2 -> 4.",
    },
    {
        "id": "code-07",
        "concept": "11 Tree DFS",
        "type": "code",
        "prompt": "Fill in the inorder visit of the current node.",
        "code": "def inorder(node, out):\n    if not node:\n        return\n    inorder(node.left, out)\n    ___\n    inorder(node.right, out)",
        "answers": ["out.append(node.val)"],
        "explain": "Inorder visits the left subtree, then the node, then the right subtree.",
    },
    # ------------------------------------------------------------------
    # 12 Two Heaps
    # ------------------------------------------------------------------
    {
        "id": "ch-09",
        "concept": "12 Two Heaps",
        "type": "choice",
        "question": "What invariant keeps the two-heap median structure correct?",
        "options": [
            "Sizes differ by at most one and max(low) <= min(high)",
            "Both heaps always have equal size",
            "The low heap is a min-heap and the high heap is a max-heap",
            "The high heap stores the smaller half",
        ],
        "answer": 0,
        "explain": "Every value in the low half is no greater than any value in the high half.",
    },
    {
        "id": "trace-07",
        "concept": "12 Two Heaps",
        "type": "trace",
        "prompt": "What is the lower median reported by this code?",
        "setup": "lo, hi = [], []\nfor x in [2, 3, 1]:\n    lo.append(x)\n    lo.sort()\n    if len(lo) > len(hi) + 1:\n        hi.append(lo.pop())\n    if len(hi) > len(lo):\n        lo.append(hi.pop(0))",
        "expr": "lo[-1]",
        "explain": "The low heap keeps the smaller half plus at most one extra, so its maximum is the lower median.",
    },
    # ------------------------------------------------------------------
    # 13 Backtracking
    # ------------------------------------------------------------------
    {
        "id": "code-08",
        "concept": "13 Backtracking",
        "type": "code",
        "prompt": "Fill in the line that records the subset when the recursion reaches a leaf.",
        "code": "def subsets(nums):\n    res = []\n    def dfs(i, path):\n        if i == len(nums):\n            ___\n            return\n        dfs(i + 1, path)\n        path.append(nums[i])\n        dfs(i + 1, path)\n        path.pop()\n    dfs(0, [])\n    return res",
        "answers": ["res.append(path[:])"],
        "explain": "The slice stores a snapshot; appending path itself would store the list that is later mutated.",
    },
    {
        "id": "ch-10",
        "concept": "13 Backtracking",
        "type": "choice",
        "question": "In the backtracking template, why is the choice undone after the recursive call?",
        "options": [
            "To restore the state before trying the next choice",
            "To free the memory used by the recursion",
            "To keep the output in sorted order",
            "The recursive call already undoes it",
        ],
        "answer": 0,
        "explain": "The mutable state is shared across branches, so each branch must leave it as it found it.",
    },
    # ------------------------------------------------------------------
    # 14 Graph BFS/DFS
    # ------------------------------------------------------------------
    {
        "id": "trace-08",
        "concept": "14 Graph BFS/DFS",
        "type": "trace",
        "prompt": "In what order does the BFS visit the nodes?",
        "setup": "graph = {0: [1, 2], 1: [3], 2: [3], 3: []}\nseen, queue, order = {0}, [0], []\nwhile queue:\n    node = queue.pop(0)\n    order.append(node)\n    for nb in graph[node]:\n        if nb not in seen:\n            seen.add(nb)\n            queue.append(nb)",
        "expr": "order",
        "explain": "BFS processes nodes in FIFO order, so the start node and its neighbors come first.",
    },
    {
        "id": "ch-11",
        "concept": "14 Graph BFS/DFS",
        "type": "choice",
        "question": "Which traversal finds shortest paths in an unweighted graph?",
        "options": [
            "BFS",
            "DFS",
            "Both give the same distances",
            "Topological sort",
        ],
        "answer": 0,
        "explain": "BFS explores by distance layers, so a node is first reached by a shortest path.",
    },
    # ------------------------------------------------------------------
    # 15 Topological Sort
    # ------------------------------------------------------------------
    {
        "id": "code-09",
        "concept": "15 Topological Sort",
        "type": "code",
        "prompt": "Fill in the line that makes a node available once its last prerequisite is gone.",
        "code": "queue = [0]\norder = []\nwhile queue:\n    node = queue.pop(0)\n    order.append(node)\n    for nb in adj[node]:\n        indeg[nb] -= 1\n        if indeg[nb] == 0:\n            ___",
        "answers": ["queue.append(nb)"],
        "explain": "A node enters the queue only after all of its incoming edges have been removed.",
    },
    # ------------------------------------------------------------------
    # 16 Union-Find
    # ------------------------------------------------------------------
    {
        "id": "ch-12",
        "concept": "16 Union-Find",
        "type": "choice",
        "question": "What does path compression add to union-find?",
        "options": [
            "Nodes on a find path point straight at the root",
            "The parent array is kept sorted",
            "Unions always join equal-sized trees",
            "It counts the number of components",
        ],
        "answer": 0,
        "explain": "Flattening the path makes later finds almost constant time.",
    },
    {
        "id": "trace-09",
        "concept": "16 Union-Find",
        "type": "trace",
        "prompt": "What does find(3) return?",
        "setup": "parent = [0, 0, 1, 2]\ndef find(x):\n    while parent[x] != x:\n        x = parent[x]\n    return x",
        "expr": "find(3)",
        "explain": "The chain 3 -> 2 -> 1 -> 0 ends at the root 0.",
    },
    # ------------------------------------------------------------------
    # 17 Dynamic Programming
    # ------------------------------------------------------------------
    {
        "id": "code-10",
        "concept": "17 Dynamic Programming",
        "type": "code",
        "prompt": "Fill in the 0/1 knapsack transition inside the reverse capacity loop.",
        "code": "dp = [0] * (cap + 1)\nfor w, v in items:\n    for c in range(cap, w - 1, -1):\n        ___",
        "answers": ["dp[c] = max(dp[c], dp[c - w] + v)"],
        "explain": "Reverse order keeps dp[c - w] from the previous item, so each item is used at most once.",
    },
    {
        "id": "ch-13",
        "concept": "17 Dynamic Programming",
        "type": "choice",
        "question": "Why does the 1D 0/1 knapsack loop over capacity downward?",
        "options": [
            "So dp[c - w] still belongs to the previous item",
            "Because capacity values are negative",
            "To avoid sorting the items",
            "To use O(1) memory instead of O(n)",
        ],
        "answer": 0,
        "explain": "A forward loop would let the same item be chosen twice in one pass.",
    },
    # ------------------------------------------------------------------
    # 18 Greedy
    # ------------------------------------------------------------------
    {
        "id": "ch-14",
        "concept": "18 Greedy",
        "type": "choice",
        "question": "To maximize the number of non-overlapping intervals, which interval do you keep?",
        "options": [
            "The one with the earliest end time",
            "The one with the earliest start time",
            "The shortest one",
            "The one with the latest end time",
        ],
        "answer": 0,
        "explain": "Finishing earliest leaves the most room for the remaining intervals.",
    },
    # ------------------------------------------------------------------
    # 19 Tries
    # ------------------------------------------------------------------
    {
        "id": "code-11",
        "concept": "19 Tries",
        "type": "code",
        "prompt": "Fill in the line that descends into the child for the current character.",
        "code": "def insert(root, word):\n    node = root\n    for ch in word:\n        if ch not in node.children:\n            node.children[ch] = TrieNode()\n        ___\n    node.is_end = True",
        "answers": ["node = node.children[ch]"],
        "explain": "Without descending, the next character would be inserted at the same node.",
    },
    # ------------------------------------------------------------------
    # 20 Design
    # ------------------------------------------------------------------
    {
        "id": "ch-15",
        "concept": "20 Design",
        "type": "choice",
        "question": "Which pair of structures gives an LRU cache O(1) get and put?",
        "options": [
            "Hash map plus doubly linked list",
            "Sorted array plus binary search",
            "Two heaps",
            "Stack plus queue",
        ],
        "answer": 0,
        "explain": "The map locates a node and the list moves it to the front or drops the tail in O(1).",
    },
    # ------------------------------------------------------------------
    # 21 Bit Manipulation
    # ------------------------------------------------------------------
    {
        "id": "ch-16",
        "concept": "21 Bit Manipulation",
        "type": "choice",
        "question": "What does n & (n - 1) compute?",
        "options": [
            "n with its lowest set bit cleared",
            "n with its lowest zero bit set",
            "n with all bits reversed",
            "1 if n is even, 0 if n is odd",
        ],
        "answer": 0,
        "explain": "The subtraction flips the lowest set bit and the zeros below it, so the AND removes that bit.",
    },
    {
        "id": "trace-10",
        "concept": "21 Bit Manipulation",
        "type": "trace",
        "prompt": "What does x hold after the loop?",
        "setup": "nums = [4, 1, 2, 1, 2]\nx = 0\nfor n in nums:\n    x ^= n",
        "expr": "x",
        "explain": "Equal values cancel under XOR, leaving the value that appears once.",
    },
    # ------------------------------------------------------------------
    # 22 Matrix
    # ------------------------------------------------------------------
    {
        "id": "trace-11",
        "concept": "22 Matrix",
        "type": "trace",
        "prompt": "What is m after this transformation?",
        "setup": "m = [[1, 2], [3, 4]]\nm = [list(row) for row in zip(*m[::-1])]",
        "expr": "m",
        "explain": "Reversing the rows and then transposing is a 90 degree clockwise rotation.",
    },
    # ------------------------------------------------------------------
    # 23 Advanced Graphs I
    # ------------------------------------------------------------------
    {
        "id": "ch-17",
        "concept": "23 Advanced Graphs I",
        "type": "choice",
        "question": "Why can Dijkstra give wrong answers with negative edge weights?",
        "options": [
            "A node finalized early may later be reachable by a cheaper path",
            "It cannot process weighted edges",
            "It loops forever on every cycle",
            "It needs a topological order first",
        ],
        "answer": 0,
        "explain": "The greedy step assumes the smallest tentative distance can never improve later.",
    },
    # ------------------------------------------------------------------
    # 24 Math & Geometry
    # ------------------------------------------------------------------
    {
        "id": "trace-12",
        "concept": "24 Math & Geometry",
        "type": "trace",
        "prompt": "What does power(3, 5) return?",
        "setup": "def power(base, exp):\n    result = 1\n    while exp:\n        if exp & 1:\n            result *= base\n        base *= base\n        exp >>= 1\n    return result",
        "expr": "power(3, 5)",
        "explain": "Binary exponentiation multiplies the result only for set bits of the exponent.",
    },
    # ------------------------------------------------------------------
    # 25 Advanced DP
    # ------------------------------------------------------------------
    {
        "id": "code-12",
        "concept": "25 Advanced DP",
        "type": "code",
        "prompt": "Fill in the edit-distance transition for mismatched characters.",
        "code": "prev = list(range(len(w2) + 1))\nfor i, c1 in enumerate(w1, 1):\n    cur = [i] + [0] * len(w2)\n    for j, c2 in enumerate(w2, 1):\n        if c1 == c2:\n            cur[j] = prev[j - 1]\n        else:\n            ___\n    prev = cur\nreturn prev[-1]",
        "answers": ["cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])"],
        "explain": "A mismatch costs one edit on top of the best delete, insert, or replace option.",
    },
    {
        "id": "ch-18",
        "concept": "25 Advanced DP",
        "type": "choice",
        "question": "In coin change, what is dp[0] for the minimum-coin recurrence?",
        "options": [
            "0",
            "1",
            "Infinity",
            "-1",
        ],
        "answer": 0,
        "explain": "Zero coins make amount 0; other amounts start at infinity and are relaxed from dp[0].",
    },
    # ------------------------------------------------------------------
    # 26 String Algorithms
    # ------------------------------------------------------------------
    {
        "id": "code-13",
        "concept": "26 String Algorithms",
        "type": "code",
        "prompt": "Fill in the line that stores the prefix length for position i.",
        "code": "def build_lps(p):\n    lps = [0] * len(p)\n    k = 0\n    for i in range(1, len(p)):\n        while k > 0 and p[i] != p[k]:\n            k = lps[k - 1]\n        if p[i] == p[k]:\n            k += 1\n        ___\n    return lps",
        "answers": ["lps[i] = k"],
        "explain": "lps[i] is the longest proper prefix of p[:i + 1] that is also a suffix.",
    },
    # ------------------------------------------------------------------
    # 27 Advanced Structures
    # ------------------------------------------------------------------
    {
        "id": "trace-13",
        "concept": "27 Advanced Structures",
        "type": "trace",
        "prompt": "What does the Fenwick tree look like after these three updates?",
        "setup": "tree = [0] * 5\nfor i in (1, 2, 3):\n    j = i\n    while j < len(tree):\n        tree[j] += 1\n        j += j & -j",
        "expr": "tree",
        "explain": "Each update climbs by its lowest set bit, so a later prefix query only sums a few slots.",
    },
    # ------------------------------------------------------------------
    # 28 Advanced Techniques
    # ------------------------------------------------------------------
    {
        "id": "code-14",
        "concept": "28 Advanced Techniques",
        "type": "code",
        "prompt": "Fill in the binary-lifting transition for higher powers.",
        "code": "up = [[0] * LOG for _ in range(n)]\nfor v in range(n):\n    up[v][0] = parent[v]\nfor k in range(1, LOG):\n    for v in range(n):\n        ___",
        "answers": ["up[v][k] = up[up[v][k - 1]][k - 1]"],
        "explain": "The 2^k-th ancestor is the 2^(k-1)-th ancestor of the 2^(k-1)-th ancestor.",
    },
    # ------------------------------------------------------------------
    # 29 Advanced Graphs II
    # ------------------------------------------------------------------
    {
        "id": "trace-14",
        "concept": "29 Advanced Graphs II",
        "type": "trace",
        "prompt": "What is the shortest distance to node 2 using at most two edges?",
        "setup": "dist = [0, 999, 999]\nedges = [(0, 1, 1), (1, 2, 1)]\nfor _ in range(2):\n    nxt = dist[:]\n    for u, v, w in edges:\n        if dist[u] + w < nxt[v]:\n            nxt[v] = dist[u] + w\n    dist = nxt",
        "expr": "dist[2]",
        "explain": "Each round allows one more edge, and copying dist keeps a single edge from being reused within a round.",
    },
]
