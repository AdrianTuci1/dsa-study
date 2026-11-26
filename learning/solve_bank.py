"""Problem bank for the Solve workspace.

Each problem has a statement, examples, constraints and one or more solution
variants (the "answer variants" shown behind the solution toggle).

The content server (`study/serve.py`) reads this file directly and serves it
from `/api/content`. `build_study.py` validates every problem and every code
snippet (it must be valid Python).

Add a problem:
    problem(
        "my-problem", "My Problem", "01 Arrays & Hashing", "Medium",
        "Statement with `inline code`.",
        [{"input": "...", "output": "...", "why": "..."}],
        ["constraint"],
        [variant("Approach", "O(n)", "Why it works.", \"\"\"
            def solve(...):
                ...
        \"\"\")],
    )
"""

import textwrap


def code(text):
    """Normalise an indented snippet into flush-left source."""
    return textwrap.dedent(text).strip("\n")


def variant(name, complexity, note, snippet):
    return {
        "name": name,
        "complexity": complexity,
        "note": note,
        "code": code(snippet),
    }


def problem(pid, title, concept, difficulty, statement, examples, constraints, variants):
    return {
        "id": pid,
        "title": title,
        "concept": concept,
        "difficulty": difficulty,
        "statement": statement,
        "examples": examples,
        "constraints": constraints,
        "variants": variants,
    }


PROBLEMS = [
    # ------------------------------------------------------------------
    problem(
        "two-sum", "Two Sum", "01 Arrays & Hashing", "Easy",
        "Given an array of integers `nums` and an integer `target`, return the "
        "indices of the two numbers that add up to `target`, as `[i, j]` with "
        "`i < j`. Every input has exactly one answer and one element may not be "
        "used twice.",
        [
            {"input": "nums = [2, 7, 11, 15], target = 9", "output": "[0, 1]", "why": "2 + 7 = 9."},
            {"input": "nums = [3, 2, 4], target = 6", "output": "[1, 2]", "why": "2 + 4 = 6."},
        ],
        ["2 <= len(nums) <= 10^4", "-10^9 <= nums[i] <= 10^9", "Exactly one valid answer exists."],
        [
            variant(
                "Brute force", "O(n^2) time, O(1) space",
                "Check every pair once. It is the baseline the interviewer expects you to name before optimising.",
                """
                def two_sum(nums, target):
                    for i in range(len(nums)):
                        for j in range(i + 1, len(nums)):
                            if nums[i] + nums[j] == target:
                                return [i, j]
                    return []
                """,
            ),
            variant(
                "Hash map", "O(n) time, O(n) space",
                "Store each value with its index. Check for the complement before inserting the current value, so an element cannot pair with itself.",
                """
                def two_sum(nums, target):
                    seen = {}
                    for i, x in enumerate(nums):
                        need = target - x
                        if need in seen:
                            return [seen[need], i]
                        seen[x] = i
                    return []
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "valid-anagram", "Valid Anagram", "01 Arrays & Hashing", "Easy",
        "Given two strings `s` and `t`, return `True` if `t` is an anagram of "
        "`s`: the same characters with the same multiplicities, in any order.",
        [
            {"input": 's = "anagram", t = "nagaram"', "output": "True", "why": "Same five letters, same counts."},
            {"input": 's = "rat", t = "car"', "output": "False", "why": "Different letters."},
        ],
        ["1 <= len(s), len(t) <= 5 * 10^4", "Both strings contain lowercase English letters."],
        [
            variant(
                "Sort both", "O(n log n) time, O(n) space",
                "Two strings are anagrams exactly when their sorted characters are equal.",
                """
                def is_anagram(s, t):
                    return sorted(s) == sorted(t)
                """,
            ),
            variant(
                "Count characters", "O(n) time, O(1) space (26 letters)",
                "Count up on `s` and down on `t`. Any missing character, or any count that goes negative, means they differ.",
                """
                def is_anagram(s, t):
                    if len(s) != len(t):
                        return False
                    counts = {}
                    for ch in s:
                        counts[ch] = counts.get(ch, 0) + 1
                    for ch in t:
                        if counts.get(ch, 0) == 0:
                            return False
                        counts[ch] -= 1
                    return True
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "longest-consecutive", "Longest Consecutive Sequence", "01 Arrays & Hashing", "Medium",
        "Given an unsorted list `nums`, return the length of the longest run of "
        "consecutive integers present in the list. Values do not need to be "
        "adjacent in the input.",
        [
            {"input": "nums = [100, 4, 200, 1, 3, 2]", "output": "4", "why": "The run 1, 2, 3, 4."},
            {"input": "nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]", "output": "9", "why": "0 through 8."},
        ],
        ["0 <= len(nums) <= 10^5", "-10^9 <= nums[i] <= 10^9"],
        [
            variant(
                "Sort first", "O(n log n) time, O(n) space",
                "Deduplicate, sort, then scan adjacent pairs and keep the longest run.",
                """
                def longest_consecutive(nums):
                    if not nums:
                        return 0
                    values = sorted(set(nums))
                    best = 1
                    run = 1
                    for i in range(1, len(values)):
                        if values[i] == values[i - 1] + 1:
                            run += 1
                        else:
                            run = 1
                        best = max(best, run)
                    return best
                """,
            ),
            variant(
                "Hash set + run starts", "O(n) time, O(n) space",
                "A value starts a run only when `x - 1` is missing. From each start, walk upward; every value is visited a constant number of times.",
                """
                def longest_consecutive(nums):
                    present = set(nums)
                    best = 0
                    for x in present:
                        if x - 1 not in present:
                            length = 1
                            while x + length in present:
                                length += 1
                            best = max(best, length)
                    return best
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "three-sum", "3Sum", "02 Two Pointers", "Medium",
        "Given an integer array `nums`, return all unique triplets "
        "`[a, b, c]` such that `a + b + c == 0`. The answer must not contain "
        "duplicate triplets, and the order of the triplets does not matter.",
        [
            {"input": "nums = [-1, 0, 1, 2, -1, -4]", "output": "[[-1, -1, 2], [-1, 0, 1]]", "why": "Those are the only two triplets."},
            {"input": "nums = []", "output": "[]", "why": "No triplet exists."},
        ],
        ["0 <= len(nums) <= 3000", "-10^5 <= nums[i] <= 10^5"],
        [
            variant(
                "Sort + two pointers", "O(n^2) time, O(1) extra space",
                "Fix the smallest value, then move two pointers inward. Skip duplicate values at all three positions.",
                """
                def three_sum(nums):
                    nums.sort()
                    res = []
                    n = len(nums)
                    for i in range(n - 2):
                        if i > 0 and nums[i] == nums[i - 1]:
                            continue
                        left, right = i + 1, n - 1
                        while left < right:
                            total = nums[i] + nums[left] + nums[right]
                            if total == 0:
                                res.append([nums[i], nums[left], nums[right]])
                                left += 1
                                right -= 1
                                while left < right and nums[left] == nums[left - 1]:
                                    left += 1
                                while left < right and nums[right] == nums[right + 1]:
                                    right -= 1
                            elif total < 0:
                                left += 1
                            else:
                                right -= 1
                    return res
                """,
            ),
            variant(
                "Sort + seen set", "O(n^2) time, O(n) space",
                "For each fixed first value, scan the rest and look up the complement in a set. Normalise each triplet before storing it to drop duplicates.",
                """
                def three_sum(nums):
                    nums.sort()
                    res = []
                    n = len(nums)
                    for i in range(n - 2):
                        if i > 0 and nums[i] == nums[i - 1]:
                            continue
                        seen = set()
                        found = set()
                        for j in range(i + 1, n):
                            need = -nums[i] - nums[j]
                            if need in seen:
                                triplet = tuple(sorted((nums[i], need, nums[j])))
                                if triplet not in found:
                                    found.add(triplet)
                                    res.append(list(triplet))
                            seen.add(nums[j])
                    return res
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "longest-substring", "Longest Substring Without Repeating Characters",
        "03 Sliding Window", "Medium",
        "Given a string `s`, return the length of the longest substring that "
        "contains no repeated characters. A substring is contiguous.",
        [
            {"input": 's = "abcabcbb"', "output": "3", "why": 'The substring "abc".'},
            {"input": 's = "pwwkew"', "output": "3", "why": 'The substring "wke".'},
        ],
        ["0 <= len(s) <= 5 * 10^4", "`s` contains printable ASCII characters."],
        [
            variant(
                "Brute force", "O(n^2) time, O(n) space",
                "For every start, extend until a character repeats. Simple, but it redoes the same work many times.",
                """
                def length_of_longest_substring(s):
                    best = 0
                    for i in range(len(s)):
                        seen = set()
                        for j in range(i, len(s)):
                            if s[j] in seen:
                                break
                            seen.add(s[j])
                        best = max(best, len(seen))
                    return best
                """,
            ),
            variant(
                "Sliding window", "O(n) time, O(k) space",
                "Remember the last index of each character. When a repeat falls inside the window, jump `left` just past it.",
                """
                def length_of_longest_substring(s):
                    last = {}
                    left = 0
                    best = 0
                    for right, ch in enumerate(s):
                        if ch in last and last[ch] >= left:
                            left = last[ch] + 1
                        last[ch] = right
                        best = max(best, right - left + 1)
                    return best
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "valid-parentheses", "Valid Parentheses", "08 Stack", "Easy",
        "Given a string `s` containing only `()[]{}`, return `True` if every "
        "opening bracket is closed by the matching type in the correct order.",
        [
            {"input": 's = "()[]{}"', "output": "True", "why": "Every pair closes immediately."},
            {"input": 's = "([)]"', "output": "False", "why": "The pairs cross."},
        ],
        ["1 <= len(s) <= 10^4", "`s` contains only bracket characters."],
        [
            variant(
                "Stack + mapping", "O(n) time, O(n) space",
                "Push openings. On a closing bracket, the stack top must be its partner; the stack must be empty at the end.",
                """
                def is_valid(s):
                    pairs = {")": "(", "]": "[", "}": "{"}
                    stack = []
                    for ch in s:
                        if ch in pairs:
                            if not stack or stack.pop() != pairs[ch]:
                                return False
                        else:
                            stack.append(ch)
                    return not stack
                """,
            ),
            variant(
                "Repeated replacement", "O(n^2) time, O(n) space",
                "Remove every adjacent matching pair until nothing changes. A valid string becomes empty.",
                """
                def is_valid(s):
                    while "()" in s or "[]" in s or "{}" in s:
                        s = s.replace("()", "").replace("[]", "").replace("{}", "")
                    return s == ""
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "binary-search", "Binary Search", "09 Binary Search", "Easy",
        "Given a sorted array `nums` of distinct integers and a `target`, "
        "return the index of `target`, or `-1` if it is not present. The "
        "algorithm must run in `O(log n)`.",
        [
            {"input": "nums = [-1, 0, 3, 5, 9, 12], target = 9", "output": "4", "why": "9 is at index 4."},
            {"input": "nums = [-1, 0, 3, 5, 9, 12], target = 2", "output": "-1", "why": "2 is not in the array."},
        ],
        ["1 <= len(nums) <= 10^4", "`nums` is sorted in strictly increasing order."],
        [
            variant(
                "Iterative", "O(log n) time, O(1) space",
                "Keep a closed interval `[lo, hi]`. Compare the middle, then discard the half that cannot contain the target.",
                """
                def search(nums, target):
                    lo, hi = 0, len(nums) - 1
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        if nums[mid] == target:
                            return mid
                        if nums[mid] < target:
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    return -1
                """,
            ),
            variant(
                "Recursive", "O(log n) time, O(log n) space",
                "The same interval, expressed as a recursive call on the surviving half.",
                """
                def search(nums, target):
                    def binary(lo, hi):
                        if lo > hi:
                            return -1
                        mid = (lo + hi) // 2
                        if nums[mid] == target:
                            return mid
                        if nums[mid] < target:
                            return binary(mid + 1, hi)
                        return binary(lo, mid - 1)

                    return binary(0, len(nums) - 1)
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "reverse-linked-list", "Reverse Linked List", "07 In-Place Linked List Reversal", "Easy",
        "Given the head of a singly linked list, reverse it in place and "
        "return the new head. A node has `val` and `next` fields.",
        [
            {"input": "head = 1 -> 2 -> 3 -> 4 -> 5", "output": "5 -> 4 -> 3 -> 2 -> 1", "why": "Every next pointer is flipped."},
            {"input": "head = None", "output": "None", "why": "The empty list stays empty."},
        ],
        ["0 <= number of nodes <= 5000", "-5000 <= node.val <= 5000"],
        [
            variant(
                "Iterative", "O(n) time, O(1) space",
                "Walk once with `prev`, `cur` and `nxt`. Redirect `cur.next` backwards, then advance.",
                """
                def reverse_list(head):
                    prev = None
                    cur = head
                    while cur:
                        nxt = cur.next
                        cur.next = prev
                        prev = cur
                        cur = nxt
                    return prev
                """,
            ),
            variant(
                "Recursive", "O(n) time, O(n) stack space",
                "Reverse the tail, then make the next node point back at the current one. The base case is the last node.",
                """
                def reverse_list(head):
                    if head is None or head.next is None:
                        return head
                    new_head = reverse_list(head.next)
                    head.next.next = head
                    head.next = None
                    return new_head
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "number-of-islands", "Number of Islands", "14 Graph BFS/DFS", "Medium",
        "Given an `m x n` grid of `'1'` (land) and `'0'` (water), return the "
        "number of islands. An island is a group of land cells connected "
        "horizontally or vertically.",
        [
            {"input": 'grid = [["1","1","0"],["0","1","0"],["0","0","1"]]', "output": "2", "why": "One two-cell island and one single-cell island."},
            {"input": 'grid = [["0","0"],["0","0"]]', "output": "0", "why": "There is no land."},
        ],
        ["1 <= rows, cols <= 300", "Cells are the characters '1' or '0'."],
        [
            variant(
                "DFS flood fill", "O(rows * cols) time, O(rows * cols) stack",
                "Every time an unvisited land cell is found, sink the whole island by turning visited land into water.",
                """
                def num_islands(grid):
                    if not grid:
                        return 0
                    rows, cols = len(grid), len(grid[0])

                    def sink(r, c):
                        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                            return
                        grid[r][c] = "0"
                        sink(r + 1, c)
                        sink(r - 1, c)
                        sink(r, c + 1)
                        sink(r, c - 1)

                    count = 0
                    for r in range(rows):
                        for c in range(cols):
                            if grid[r][c] == "1":
                                count += 1
                                sink(r, c)
                    return count
                """,
            ),
            variant(
                "BFS flood fill", "O(rows * cols) time, O(min(rows, cols)) queue",
                "Same idea with an explicit queue. Mark a cell as water when it is enqueued, not when it is popped.",
                """
                from collections import deque

                def num_islands(grid):
                    if not grid:
                        return 0
                    rows, cols = len(grid), len(grid[0])
                    count = 0
                    for r in range(rows):
                        for c in range(cols):
                            if grid[r][c] != "1":
                                continue
                            count += 1
                            grid[r][c] = "0"
                            queue = deque([(r, c)])
                            while queue:
                                cr, cc = queue.popleft()
                                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                    nr, nc = cr + dr, cc + dc
                                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                        grid[nr][nc] = "0"
                                        queue.append((nr, nc))
                    return count
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "house-robber", "House Robber", "17 Dynamic Programming", "Medium",
        "Given a list of non-negative integers `nums` where `nums[i]` is the "
        "money in house `i`, return the maximum amount you can rob without "
        "robbing two adjacent houses.",
        [
            {"input": "nums = [1, 2, 3, 1]", "output": "4", "why": "Rob houses 0 and 2."},
            {"input": "nums = [2, 7, 9, 3, 1]", "output": "12", "why": "Rob houses 0, 2 and 4."},
        ],
        ["1 <= len(nums) <= 100", "0 <= nums[i] <= 400"],
        [
            variant(
                "DP array", "O(n) time, O(n) space",
                "`dp[i]` is the best loot from the first `i + 1` houses. Either skip house `i`, or take it and add `dp[i - 2]`.",
                """
                def rob(nums):
                    if not nums:
                        return 0
                    dp = [0] * len(nums)
                    dp[0] = nums[0]
                    for i in range(1, len(nums)):
                        take = nums[i] + (dp[i - 2] if i >= 2 else 0)
                        dp[i] = max(dp[i - 1], take)
                    return dp[-1]
                """,
            ),
            variant(
                "Two variables", "O(n) time, O(1) space",
                "The recurrence only reads the previous two values, so two variables replace the array.",
                """
                def rob(nums):
                    two_back = one_back = 0
                    for money in nums:
                        two_back, one_back = one_back, max(one_back, two_back + money)
                    return one_back
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "coin-change", "Coin Change", "17 Dynamic Programming", "Medium",
        "Given coin denominations `coins` and an integer `amount`, return the "
        "fewest coins needed to make exactly `amount`, or `-1` if it is "
        "impossible. You have an unlimited supply of each coin.",
        [
            {"input": "coins = [1, 2, 5], amount = 11", "output": "3", "why": "5 + 5 + 1."},
            {"input": "coins = [2], amount = 3", "output": "-1", "why": "An odd amount cannot be made from 2s."},
        ],
        ["1 <= len(coins) <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"],
        [
            variant(
                "Bottom-up", "O(amount * len(coins)) time, O(amount) space",
                "`dp[x]` is the minimum number of coins for `x`. Build every amount from smaller ones; start at infinity so unreachable amounts stay impossible.",
                """
                def coin_change(coins, amount):
                    dp = [float("inf")] * (amount + 1)
                    dp[0] = 0
                    for value in range(1, amount + 1):
                        for coin in coins:
                            if coin <= value:
                                dp[value] = min(dp[value], dp[value - coin] + 1)
                    return -1 if dp[amount] == float("inf") else dp[amount]
                """,
            ),
            variant(
                "Memoised DFS", "O(amount * len(coins)) time, O(amount) space",
                "Top-down: `best(remaining)` tries every coin and caches the answer. It expresses the same recurrence as the table.",
                """
                def coin_change(coins, amount):
                    memo = {}

                    def best(remaining):
                        if remaining == 0:
                            return 0
                        if remaining < 0:
                            return float("inf")
                        if remaining in memo:
                            return memo[remaining]
                        result = min(
                            (best(remaining - coin) + 1 for coin in coins),
                            default=float("inf"),
                        )
                        memo[remaining] = result
                        return result

                    answer = best(amount)
                    return -1 if answer == float("inf") else answer
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "course-schedule", "Course Schedule", "15 Topological Sort", "Medium",
        "There are `numCourses` courses labelled `0 .. numCourses-1`. Each "
        "prerequisite pair `[a, b]` means you must take `b` before `a`. "
        "Return `True` if you can finish every course.",
        [
            {"input": "numCourses = 2, prerequisites = [[1, 0]]", "output": "True", "why": "Take 0, then 1."},
            {"input": "numCourses = 2, prerequisites = [[1, 0], [0, 1]]", "output": "False", "why": "The two courses depend on each other."},
        ],
        ["1 <= numCourses <= 2000", "0 <= len(prerequisites) <= 5000"],
        [
            variant(
                "Kahn (BFS)", "O(V + E) time, O(V + E) space",
                "Count indegrees, queue every course with none, and peel them off. If fewer than `numCourses` courses come out, a cycle remains.",
                """
                from collections import deque

                def can_finish(num_courses, prerequisites):
                    graph = [[] for _ in range(num_courses)]
                    indegree = [0] * num_courses
                    for course, before in prerequisites:
                        graph[before].append(course)
                        indegree[course] += 1

                    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
                    seen = 0
                    while queue:
                        node = queue.popleft()
                        seen += 1
                        for nxt in graph[node]:
                            indegree[nxt] -= 1
                            if indegree[nxt] == 0:
                                queue.append(nxt)
                    return seen == num_courses
                """,
            ),
            variant(
                "DFS with colours", "O(V + E) time, O(V + E) space",
                "White = unvisited, grey = on the current stack, black = finished. An edge to a grey node is a cycle.",
                """
                def can_finish(num_courses, prerequisites):
                    graph = [[] for _ in range(num_courses)]
                    for course, before in prerequisites:
                        graph[before].append(course)
                    state = [0] * num_courses  # 0 new, 1 visiting, 2 done

                    def visit(node):
                        if state[node] == 1:
                            return False
                        if state[node] == 2:
                            return True
                        state[node] = 1
                        for nxt in graph[node]:
                            if not visit(nxt):
                                return False
                        state[node] = 2
                        return True

                    return all(visit(node) for node in range(num_courses))
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "merge-intervals", "Merge Intervals", "05 Merge Intervals", "Medium",
        "Given a list of intervals `[start, end]`, merge every pair that "
        "overlaps or touches, and return the non-overlapping intervals sorted "
        "by start.",
        [
            {"input": "intervals = [[1,3],[2,6],[8,10],[15,18]]", "output": "[[1,6],[8,10],[15,18]]", "why": "[1,3] and [2,6] overlap."},
            {"input": "intervals = [[1,4],[4,5]]", "output": "[[1,5]]", "why": "Touching intervals count as overlapping."},
        ],
        ["1 <= len(intervals) <= 10^4", "0 <= start <= end <= 10^4"],
        [
            variant(
                "Sort + merge", "O(n log n) time, O(n) space",
                "Sort by start. An interval joins the last merged one when it starts at or before the current end.",
                """
                def merge(intervals):
                    intervals.sort(key=lambda pair: pair[0])
                    merged = []
                    for start, end in intervals:
                        if merged and start <= merged[-1][1]:
                            merged[-1][1] = max(merged[-1][1], end)
                        else:
                            merged.append([start, end])
                    return merged
                """,
            ),
            variant(
                "Sweep line", "O(n log n) time, O(n) space",
                "Turn every interval into a start event (+1) and an end event (-1). Sort points and count the active intervals. Sorting starts before ends at the same point merges touching intervals.",
                """
                def merge(intervals):
                    events = []
                    for start, end in intervals:
                        events.append((start, 1))
                        events.append((end, -1))
                    events.sort(key=lambda event: (event[0], -event[1]))

                    merged = []
                    active = 0
                    start = None
                    for point, delta in events:
                        if active == 0:
                            start = point
                        active += delta
                        if active == 0:
                            merged.append([start, point])
                    return merged
                """,
            ),
        ],
    ),
    # ------------------------------------------------------------------
    problem(
        "kth-largest", "Kth Largest Element in an Array", "12 Two Heaps", "Medium",
        "Given an integer array `nums` and an integer `k`, return the "
        "`k`-th largest element, counting duplicates. This is the element "
        "that would be at index `len(nums) - k` after sorting.",
        [
            {"input": "nums = [3, 2, 1, 5, 6, 4], k = 2", "output": "5", "why": "Sorted: 1, 2, 3, 4, 5, 6."},
            {"input": "nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4", "output": "4", "why": "Sorted: 1, 2, 2, 3, 3, 4, 5, 5, 6."},
        ],
        ["1 <= len(nums) <= 10^5", "-10^4 <= nums[i] <= 10^4", "1 <= k <= len(nums)"],
        [
            variant(
                "Min-heap of size k", "O(n log k) time, O(k) space",
                "Keep the k largest values seen so far. The smallest of them, the heap root, is the k-th largest overall.",
                """
                import heapq

                def find_kth_largest(nums, k):
                    heap = []
                    for x in nums:
                        heapq.heappush(heap, x)
                        if len(heap) > k:
                            heapq.heappop(heap)
                    return heap[0]
                """,
            ),
            variant(
                "Quickselect", "O(n) average time, O(1) extra space",
                "Partition around a pivot and recurse only into the side that contains index `len(nums) - k`. This mutates the input.",
                """
                import random

                def find_kth_largest(nums, k):
                    target = len(nums) - k

                    def select(left, right):
                        pivot = nums[random.randint(left, right)]
                        i, j = left, right
                        while i <= j:
                            while nums[i] < pivot:
                                i += 1
                            while nums[j] > pivot:
                                j -= 1
                            if i <= j:
                                nums[i], nums[j] = nums[j], nums[i]
                                i += 1
                                j -= 1
                        if target <= j:
                            return select(left, j)
                        if target >= i:
                            return select(i, right)
                        return nums[target]

                    return select(0, len(nums) - 1)
                """,
            ),
        ],
    ),
]
