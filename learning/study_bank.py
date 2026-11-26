"""English recall cards for the study app.

Each item is a short question/answer pair that trains pattern recognition:
the trigger ("when do I use this?") and the skeleton ("what do I write?").

The web app also uses these as spaced-repetition units. The content server
(`study/serve.py`) reads this file, merges it with `study_extras.py` and
serves it from `/api/content`; there is no build step.

Add an item, then reload the page. Validate with:
    python3 learning/build_study.py
"""

CONCEPTS = [
    "00 Python Essentials",
    "01 Arrays & Hashing",
    "02 Two Pointers",
    "03 Sliding Window",
    "04 Fast & Slow Pointers",
    "05 Merge Intervals",
    "06 Cyclic Sort",
    "07 In-Place Linked List Reversal",
    "08 Stack",
    "09 Binary Search",
    "10 Tree BFS",
    "11 Tree DFS",
    "12 Two Heaps",
    "13 Backtracking",
    "14 Graph BFS/DFS",
    "15 Topological Sort",
    "16 Union-Find",
    "17 Dynamic Programming",
    "18 Greedy",
    "19 Tries",
    "20 Design",
    "21 Bit Manipulation",
    "22 Matrix",
    "23 Advanced Graphs I",
    "24 Math & Geometry",
    "25 Advanced DP",
    "26 String Algorithms",
    "27 Advanced Structures",
    "28 Advanced Techniques",
    "29 Advanced Graphs II",
]


def recall(cid, concept, front, back, hint=""):
    return {
        "id": cid,
        "concept": concept,
        "type": "recall",
        "front": front,
        "back": back,
        "hint": hint,
    }


RECALL_ITEMS = [
    # ---------------------------------------------------------------- 00
    recall(
        "r-00-01", "00 Python Essentials",
        "What does `a[:1]` return, and how is it different from `a[1]`?",
        "`a[:1]` is a slice from 0 to 1, so it returns a NEW list containing the "
        "first element. `a[1]` returns the element at index 1. `[:1]` never means "
        "\"element 1\".",
        "a slice always returns the same type as the container",
    ),
    recall(
        "r-00-02", "00 Python Essentials",
        "How do you copy a matrix so that editing the copy does not touch the original?",
        "`[row[:] for row in m]` (or `[list(row) for row in m]`). `m[:]` copies only "
        "the outer list, so the rows are still shared.",
        "shallow copy copies one level",
    ),
    recall(
        "r-00-03", "00 Python Essentials",
        "Why write `res.append(path[:])` instead of `res.append(path)` in backtracking?",
        "`path` is the same list object that keeps being mutated by append/pop. "
        "Without the copy, every result in `res` points to that one list and shows "
        "its final state.",
    ),

    # ---------------------------------------------------------------- 01
    recall(
        "r-01-01", "01 Arrays & Hashing",
        "Two Sum: what do you check at each element, and what do you store?",
        "Check whether `target - x` is already in the hash map BEFORE inserting x. "
        "Store `value -> index` so you can return both indices in one pass.",
        "why store the index and not only the value?",
    ),
    recall(
        "r-01-02", "01 Arrays & Hashing",
        "Product of Array Except Self without division: what is the shape of the solution?",
        "`out[i] = prefix_before_i * suffix_after_i`. One left-to-right pass writes "
        "prefixes into `out`, then one right-to-left pass multiplies suffixes in. "
        "O(n) time, O(1) extra space.",
    ),
    recall(
        "r-01-03", "01 Arrays & Hashing",
        "Longest Consecutive Sequence in O(n): what is the key trick?",
        "Put every value in a set. Only start counting from x when `x - 1` is NOT "
        "in the set, then walk upward with `while x + length in set`. Each value is "
        "visited a constant number of times.",
    ),

    # ---------------------------------------------------------------- 02
    recall(
        "r-02-01", "02 Two Pointers",
        "When does the two-pointer pattern apply?",
        "When the array is sorted (or sortable) and you need a pair/triplet/interval, "
        "or when you need O(1) extra space to compact in place.",
        "sorted + need two indices that move toward each other or in the same direction",
    ),
    recall(
        "r-02-02", "02 Two Pointers",
        "3Sum: what is the algorithm and how do you avoid duplicate triplets?",
        "Sort, fix `i`, then use `l = i + 1` and `r = n - 1`. After a hit, skip "
        "duplicates at `i`, `l` and `r`. O(n^2) time, O(1) extra space.",
    ),

    # ---------------------------------------------------------------- 03
    recall(
        "r-03-01", "03 Sliding Window",
        "What is the general template for a variable-size window?",
        "Expand `r` and add to the window state. `while` the window is invalid, "
        "remove `l` and `l += 1`. Update the answer while the window is valid. "
        "Each index enters and leaves once, so O(n).",
        "the `while` is what makes it O(n); a nested `for` restart would be O(n^2)",
    ),
    recall(
        "r-03-02", "03 Sliding Window",
        "Minimum Window Substring: how do you know the window is valid?",
        "Keep `need` and `window` frequency maps plus a `have` counter of how many "
        "needed characters are satisfied. The window is valid when `have == need`; "
        "then record it and try to shrink from the left.",
    ),

    # ---------------------------------------------------------------- 04
    recall(
        "r-04-01", "04 Fast & Slow Pointers",
        "Linked List Cycle: how do you detect the cycle and find its entry?",
        "Move slow by 1 and fast by 2. If they meet, a cycle exists. Then reset slow "
        "to head and move both one step at a time; the meeting point is the cycle "
        "entry.",
    ),
    recall(
        "r-04-02", "04 Fast & Slow Pointers",
        "How do you find the middle of a linked list with two pointers?",
        "`while fast and fast.next: slow = slow.next; fast = fast.next.next`. "
        "For even length this returns the second middle node.",
    ),

    # ---------------------------------------------------------------- 05
    recall(
        "r-05-01", "05 Merge Intervals",
        "Merge Intervals: sort order and merge condition?",
        "Sort by start. For each interval, if its start is `<= last_end`, merge by "
        "`last_end = max(last_end, end)`; otherwise append it as a new interval. "
        "O(n log n) for the sort.",
    ),
    recall(
        "r-05-02", "05 Merge Intervals",
        "Insert Interval: what are the three phases?",
        "1) append intervals that end before the new one starts; 2) merge every "
        "interval overlapping the new one, extending its start/end; 3) append the "
        "rest.",
    ),

    # ---------------------------------------------------------------- 06
    recall(
        "r-06-01", "06 Cyclic Sort",
        "Cyclic Sort: what is the placement loop?",
        "`while nums[i] != i + 1 and 1 <= nums[i] <= n: swap nums[i] with "
        "nums[nums[i] - 1]`. Each value reaches its home position once, so O(n).",
        "careful with the swap order when the target index is computed",
    ),
    recall(
        "r-06-02", "06 Cyclic Sort",
        "After cyclic sort, how do you find the missing number and the duplicate?",
        "Scan for the first index where `nums[i] != i + 1`: its expected value "
        "`i + 1` is missing. If the value sitting there points to a position that "
        "is already correct, that value is the duplicate.",
    ),

    # ---------------------------------------------------------------- 07
    recall(
        "r-07-01", "07 In-Place Linked List Reversal",
        "Reverse a linked list in place: the three pointers and the loop?",
        "`prev = None; cur = head`; while cur: `nxt = cur.next; cur.next = prev; "
        "prev = cur; cur = nxt`. Return `prev`.",
    ),
    recall(
        "r-07-02", "07 In-Place Linked List Reversal",
        "Reverse Nodes in k-Group: what do you check before reversing a group?",
        "Walk k nodes ahead first. If fewer than k remain, leave the tail untouched. "
        "Otherwise reverse the group, reconnect it, and continue.",
    ),

    # ---------------------------------------------------------------- 08
    recall(
        "r-08-01", "08 Stack",
        "Valid Parentheses: the algorithm?",
        "Push opening brackets. On a closing bracket, pop and check that it matches. "
        "The string is valid only if the stack is empty at the end. O(n).",
    ),
    recall(
        "r-08-02", "08 Stack",
        "Monotonic stack for next greater element: why is it O(n)?",
        "Keep indices whose values are decreasing. Pop while the top value is smaller "
        "than the current one and record the current value as its next greater. Each "
        "index is pushed and popped at most once.",
    ),

    # ---------------------------------------------------------------- 09
    recall(
        "r-09-01", "09 Binary Search",
        "Lower-bound binary search: the invariant and the template?",
        "`lo, hi = 0, n`; while `lo < hi`: `mid = (lo + hi) // 2`; if `ok(mid)` then "
        "`hi = mid`, else `lo = mid + 1`. Answer is `lo`, which may be `n`.",
        "the answer always stays inside [lo, hi]",
    ),
    recall(
        "r-09-02", "09 Binary Search",
        "Search in Rotated Sorted Array: how do you choose the half?",
        "Compare `nums[mid]` with `nums[lo]` to decide which half is sorted, then "
        "check whether the target lies inside that sorted half.",
    ),

    # ---------------------------------------------------------------- 10
    recall(
        "r-10-01", "10 Tree BFS",
        "Level order traversal: the queue template?",
        "`q = deque([root])`; while q: capture `len(q)` and loop that many times, "
        "popping a node and appending its children. That inner loop is one level.",
        "capture len(q) BEFORE the inner loop",
    ),
    recall(
        "r-10-02", "10 Tree BFS",
        "Binary Tree Right Side View: what do you take from each level?",
        "The last node of each level (the first if you look from the left). A plain "
        "level-order BFS gives it directly.",
    ),

    # ---------------------------------------------------------------- 11
    recall(
        "r-11-01", "11 Tree DFS",
        "Maximum Path Sum: what does the recursion return vs. what does it update?",
        "Return `node.val + max(0, left, right)` (one branch, so the path can continue "
        "upward). Update a global best with `node.val + max(0, left) + max(0, right)` "
        "(both branches, path closes here).",
    ),
    recall(
        "r-11-02", "11 Tree DFS",
        "How do you validate a BST with recursion?",
        "Pass bounds `(low, high)` and require `low < node.val < high`. Left child "
        "gets `(low, node.val)`, right child gets `(node.val, high)`.",
    ),

    # ---------------------------------------------------------------- 12
    recall(
        "r-12-01", "12 Two Heaps",
        "Find Median from Data Stream: the two heaps and the rebalancing?",
        "Max-heap for the smaller half (store negated values) and min-heap for the "
        "larger half. Insert into one, then move a top across if the sizes differ by "
        "more than 1. The median is one top or the average of both tops.",
    ),
    recall(
        "r-12-02", "12 Two Heaps",
        "Kth Largest Element in a Stream: which heap and what size?",
        "A min-heap of at most k elements. Its top is the k-th largest. Each insert "
        "costs O(log k).",
    ),

    # ---------------------------------------------------------------- 13
    recall(
        "r-13-01", "13 Backtracking",
        "What is the backtracking template?",
        "If the path is a solution, append a copy and return. For each candidate: "
        "add it, recurse, then remove it. That is choose -> explore -> unchoose.",
    ),
    recall(
        "r-13-02", "13 Backtracking",
        "When can you `break` instead of `continue` while pruning?",
        "When the input is sorted and the current candidate already exceeds the "
        "target: every later candidate is at least as large, so the whole branch is "
        "dead.",
    ),

    # ---------------------------------------------------------------- 14
    recall(
        "r-14-01", "14 Graph BFS/DFS",
        "Where should you mark a node as visited, and why?",
        "BFS: when you enqueue it, otherwise the same node can be queued many times. "
        "DFS: when you enter it. Without this, work can blow up or recurse forever.",
    ),
    recall(
        "r-14-02", "14 Graph BFS/DFS",
        "Number of Islands: how do you mark an island?",
        "Run DFS/BFS from every unvisited '1' and turn each visited land cell into "
        "'0' (or use a visited set). The number of starts is the number of islands.",
    ),

    # ---------------------------------------------------------------- 15
    recall(
        "r-15-01", "15 Topological Sort",
        "Kahn's algorithm: the steps and the cycle check?",
        "Compute indegrees, queue all nodes with indegree 0, pop a node, append it to "
        "the order, and decrement its neighbours. If the order has fewer than n "
        "nodes, the graph has a cycle.",
    ),
    recall(
        "r-15-02", "15 Topological Sort",
        "DFS with three colours for cycle detection: what do the colours mean?",
        "White = unvisited, grey = on the current recursion stack, black = finished. "
        "An edge to a grey node is a cycle. Reverse postorder is a topological order.",
    ),

    # ---------------------------------------------------------------- 16
    recall(
        "r-16-01", "16 Union-Find",
        "Union-Find: `find` with path compression and union by size?",
        "`find(x)`: if `parent[x] != x`, set `parent[x] = find(parent[x])` and return "
        "it. Union: attach the root of the smaller tree under the larger root. Both "
        "give near-constant amortised time.",
    ),
    recall(
        "r-16-02", "16 Union-Find",
        "Graph Valid Tree: which two conditions must hold?",
        "Exactly `n - 1` edges, and no edge may connect two nodes already in the same "
        "component (that would create a cycle).",
    ),

    # ---------------------------------------------------------------- 17
    recall(
        "r-17-01", "17 Dynamic Programming",
        "How do you decide between DP and greedy?",
        "Use DP when a local choice depends on future states or you must consider "
        "combinations. Use greedy only when an exchange argument proves that a local "
        "optimum is globally optimal.",
    ),
    recall(
        "r-17-02", "17 Dynamic Programming",
        "House Robber: the recurrence?",
        "`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. Only the last two values are "
        "needed, so two variables give O(n) time and O(1) space.",
    ),
    recall(
        "r-17-03", "17 Dynamic Programming",
        "Longest Common Subsequence: the recurrence?",
        "If `a[i-1] == b[j-1]`, `dp[i][j] = dp[i-1][j-1] + 1`; otherwise "
        "`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`. Two rows are enough.",
    ),

    # ---------------------------------------------------------------- 18
    recall(
        "r-18-01", "18 Greedy",
        "Jump Game: what does `farthest` mean and when do you fail?",
        "`farthest` is the furthest index reachable so far. Walking left to right, if "
        "the current index is greater than it, you are stuck and return false.",
    ),
    recall(
        "r-18-02", "18 Greedy",
        "Gas Station: the existence condition and the start choice?",
        "A tour exists iff `sum(gas) >= sum(cost)`. If it does, the valid start is the "
        "station right after the last point where the tank went negative.",
    ),

    # ---------------------------------------------------------------- 19
    recall(
        "r-19-01", "19 Tries",
        "What is the structure of a trie node?",
        "A dictionary of child characters plus an end-of-word flag. Insert, search "
        "and startsWith all walk the characters, so each costs O(len(word)).",
    ),
    recall(
        "r-19-02", "19 Tries",
        "Word Search II: why combine a trie with DFS on the board?",
        "The trie prunes any prefix that cannot become a word, and DFS explores "
        "adjacent cells. Without the trie you would re-scan the board for every word, "
        "which is far slower.",
    ),

    # ---------------------------------------------------------------- 20
    recall(
        "r-20-01", "20 Design",
        "LRU Cache: the Python implementation and the interview implementation?",
        "Python: `OrderedDict`, `move_to_end(key)` on get and put, "
        "`popitem(last=False)` to evict. Interview: hash map plus a doubly linked "
        "list for O(1) moves.",
    ),
    recall(
        "r-20-02", "20 Design",
        "Min Stack: why can't you just call `min()` inside getMin?",
        "After a pop you must return to the previous minimum, so you need history. "
        "Keep a parallel stack of running minima, or store `(value, min_so_far)` "
        "pairs.",
    ),

    # ---------------------------------------------------------------- 21
    recall(
        "r-21-01", "21 Bit Manipulation",
        "Single Number: why does XOR work?",
        "`x ^ x = 0`, `x ^ 0 = x`, and XOR is commutative and associative, so every "
        "duplicated value cancels out and only the unique value remains. O(n) time, "
        "O(1) space.",
    ),
    recall(
        "r-21-02", "21 Bit Manipulation",
        "What does `n & (n - 1)` do?",
        "It clears the lowest set bit. It powers the bit-count loop "
        "(`while n: n &= n - 1; count += 1`) and the power-of-two test "
        "(`n > 0 and n & (n - 1) == 0`).",
    ),
    recall(
        "r-21-03", "21 Bit Manipulation",
        "Reverse Bits (32-bit): the algorithm?",
        "Repeat 32 times: `result = (result << 1) | (n & 1)` then `n >>= 1`. Bit i of "
        "the input ends up at position 31 - i.",
    ),

    # ---------------------------------------------------------------- 22
    recall(
        "r-22-01", "22 Matrix",
        "Spiral Matrix: the four-wall scheme?",
        "Keep top, bottom, left, right. Traverse the top row, right column, bottom "
        "row and left column, shrinking a wall after each. Re-check the walls before "
        "the last two sides so a single remaining row/column is not printed twice.",
    ),
    recall(
        "r-22-02", "22 Matrix",
        "Rotate Image 90 degrees clockwise in place: what transformation?",
        "Transpose, then reverse every row. With slices: "
        "`m[:] = [list(row) for row in zip(*m[::-1])]`. Using `m[:] =` keeps the same "
        "outer list object.",
    ),
    recall(
        "r-22-03", "22 Matrix",
        "Set Matrix Zeroes with O(1) extra space: the trick?",
        "Use the first row and first column as marker arrays. Track separately whether "
        "the first row and the first column themselves must be zeroed, otherwise "
        "writing markers destroys that information.",
    ),

    # ---------------------------------------------------------------- 23
    recall(
        "r-23-01", "23 Advanced Graphs I",
        "Dijkstra with a heap: the structure and why negative edges break it?",
        "`dist[] = inf`, `dist[src] = 0`, heap of `(dist, node)`. Pop the minimum, skip "
        "stale entries (`d > dist[u]`), relax neighbours. With negative edges a "
        "finalised node can still improve later, so use Bellman-Ford instead.",
    ),
    recall(
        "r-23-02", "23 Advanced Graphs I",
        "Bellman-Ford with at most K stops: why copy the distances each round?",
        "One round adds one more flight. Relaxing in place would allow using a K+2 "
        "edge path within K+1 rounds. Relax from a copy of the previous round's "
        "distances, for `k + 1` rounds.",
    ),
    recall(
        "r-23-03", "23 Advanced Graphs I",
        "MST: when do you use Prim and when Kruskal?",
        "Prim is O(n^2) and wins on dense graphs (no need to sort n^2 edges). Kruskal "
        "is O(E log E) with Union-Find and wins on sparse graphs.",
    ),

    # ---------------------------------------------------------------- 24
    recall(
        "r-24-01", "24 Math & Geometry",
        "Sieve of Eratosthenes: the steps and complexity?",
        "Mark 0 and 1 as not prime. For every p with `p * p < n`, if p is prime, mark "
        "`p*p, p*p+p, ...` as composite. Count the survivors. O(n log log n).",
    ),
    recall(
        "r-24-02", "24 Math & Geometry",
        "Fast exponentiation: the recurrence and the iterative loop?",
        "`x^n = (x^2)^(n/2)` when n is even, otherwise `x * x^(n-1)`. Iterative: "
        "while n, multiply the result by the base when `n & 1`, then square the base "
        "and shift n right. O(log n).",
    ),
    recall(
        "r-24-03", "24 Math & Geometry",
        "Happy Number: why does Floyd's cycle detection apply?",
        "The digit-square-sum is a function on integers, so iterating it forms a "
        "functional graph with a cycle. Floyd finds the cycle in O(1) space; the "
        "number is happy iff the cycle is the fixed point 1.",
    ),

    # ---------------------------------------------------------------- 25
    recall(
        "r-25-01", "25 Advanced DP",
        "0/1 Knapsack with a 1-D array: why must the capacity loop go downward?",
        "Going upward would read `dp[c - w]` after it was already updated for the "
        "current item, allowing the item to be taken multiple times. Going downward "
        "reads only the previous item's row.",
    ),
    recall(
        "r-25-02", "25 Advanced DP",
        "LIS in O(n log n): what is stored in `tails`, and why `bisect_left`?",
        "`tails[k]` is the smallest possible tail of an increasing subsequence of "
        "length k+1. Replace the first tail that is `>= x` (bisect_left) or append x. "
        "`tails` itself is not a valid subsequence, only its length matters.",
        "strictly increasing uses bisect_left; non-decreasing uses bisect_right",
    ),
    recall(
        "r-25-03", "25 Advanced DP",
        "Edit Distance: the recurrence and the base cases?",
        "If the last characters match, `dp[i][j] = dp[i-1][j-1]`; otherwise "
        "`1 + min(delete, insert, replace)`. Row 0 is 0..n, column 0 is 0..m.",
    ),

    # ---------------------------------------------------------------- 26
    recall(
        "r-26-01", "26 String Algorithms",
        "KMP: what is the prefix table and why does it give O(n + m)?",
        "`lps[i]` is the length of the longest proper prefix that is also a suffix of "
        "the pattern up to i. On a mismatch, jump to `lps[j-1]` instead of restarting, "
        "so each character is compared a constant number of times amortised.",
    ),
    recall(
        "r-26-02", "26 String Algorithms",
        "Rabin-Karp: how do you update the window hash in O(1)?",
        "Rolling hash: `h = (h * base + c) mod M`. To slide, subtract the outgoing "
        "character times `base^(L-1)` and add the incoming one. Verify actual "
        "equality only when hashes match.",
    ),

    # ---------------------------------------------------------------- 27
    recall(
        "r-27-01", "27 Advanced Structures",
        "Fenwick tree (BIT): what does `i & -i` give you?",
        "It isolates the lowest set bit, which is the jump distance in the tree: "
        "`i += i & -i` for updates, `i -= i & -i` for prefix queries. Both O(log n).",
    ),
    recall(
        "r-27-02", "27 Advanced Structures",
        "Segment tree vs. sparse table: when do you use each?",
        "Segment tree supports updates and queries in O(log n). Sparse table is "
        "static-only with O(1) queries after O(n log n) preprocessing, and needs an "
        "idempotent merge such as min, max or gcd.",
    ),

    # ---------------------------------------------------------------- 28
    recall(
        "r-28-01", "28 Advanced Techniques",
        "Monotonic deque for sliding window maximum: what does it store?",
        "Indices with decreasing values. Before pushing x, pop from the back while "
        "the back value is `<= x`; pop from the front while the front index is outside "
        "the window. The front is the maximum. O(n) total.",
    ),
    recall(
        "r-28-02", "28 Advanced Techniques",
        "Quickselect: complexity and why it beats sorting?",
        "Partition like quicksort but recurse only into the side containing position "
        "k: O(n) average, O(n^2) worst. Sorting would be O(n log n).",
    ),

    # ---------------------------------------------------------------- 29
    recall(
        "r-29-01", "29 Advanced Graphs II",
        "Tarjan SCC: what is a low-link value?",
        "`low[u]` is the smallest discovery time reachable from u's subtree using "
        "tree edges plus at most one back edge. If `low[u] == disc[u]`, u is the root "
        "of a strongly connected component; pop the stack down to u.",
    ),
    recall(
        "r-29-02", "29 Advanced Graphs II",
        "How do you find bridges in a graph?",
        "DFS with `disc` and `low`. Edge (u, v) is a bridge when `low[v] > disc[u]`. "
        "The same low-link idea finds articulation points with extra root/child "
        "conditions.",
    ),
]
