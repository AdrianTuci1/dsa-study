"""
CONCEPT: Tries

Soluții de referință — toate testele trec. Citește-le, apoi încearcă să le
rescrii din memorie fără să te uiți. Verifică astfel:

    python3 practice/19_tries.py

Output: [v] test trecut, [x] test picat, la final N/M passed.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Implement Trie (Prefix Tree)  (LeetCode 208)
#
# A trie (prefix tree) stores strings so that lookup by whole word and lookup
# by prefix are both fast. The operations come as two parallel lists: `ops`
# holds the operation names, `args` holds one argument list per call.
#
# The first op is always the constructor "Trie" with args [].
#   - insert(word): store the word; returns nothing.
#   - search(word): True if the exact word was inserted before.
#   - startsWith(prefix): True if some inserted word starts with `prefix`.
# Return a list with one result per operation: None for operations that return
# nothing, otherwise the value they return.
#
# Example 1:
#   Input: ops  = ["Trie", "insert", "search", "search", "startsWith", "startsWith"]
#          args = [[],     ["apple"], ["apple"], ["app"],  ["app"],      ["appl"]]
#   Output: [None, None, True, False, True, True]
#   Explanation: "apple" was inserted; "app" is a prefix but not a word.
# Example 2:
#   Input: ops  = ["Trie", "search", "insert", "search", "startsWith"]
#          args = [[],     ["a"],    ["a"],    ["a"],    ["a"]]
#   Output: [None, False, None, True, True]
#   Explanation: an empty trie contains nothing; after insert("a") both the
#   word "a" and the prefix "a" exist.
#
# Constraints:
#   - 1 <= len(ops) <= 1000
#   - 0 <= len(word), len(prefix) <= 20
#   - word and prefix consist of lowercase English letters
# ---------------------------------------------------------------------------
def p1_implement_trie(ops, args):
    """ops: list of operation names. args: list of argument lists, same length.
    Return a list with one result per operation: None for the constructor,
    otherwise the operation's return value (None when it returns nothing).

    Example:
      ops  = ["Trie", "insert", "search", "search", "startsWith"]
      args = [[],     ["apple"], ["apple"], ["app"],  ["app"]]
      -> [None, None, True, False, True]
    """
    END = "\0"  # sentinel key; no lowercase letter can collide with it
    root = {}

    def walk(word):
        """Node at the end of `word`, or None if the path breaks."""
        node = root
        for ch in word:
            node = node.get(ch)
            if node is None:
                return None
        return node

    out = []
    for op, a in zip(ops, args):
        if op == "Trie":
            out.append(None)
        elif op == "insert":
            node = root
            for ch in a[0]:
                node = node.setdefault(ch, {})
            node[END] = True  # a word may end here
            out.append(None)
        elif op == "search":
            node = walk(a[0])
            # A prefix that exists is not a word: END must be set too.
            out.append(node is not None and END in node)
        elif op == "startsWith":
            out.append(walk(a[0]) is not None)
    return out


# ---------------------------------------------------------------------------
# Problem 2 - Design Add and Search Words Data Structure  (LeetCode 211)
#
# Design a data structure that adds words and searches them, where a '.' in a
# search pattern matches any single letter.
#
# Operations:
#   - "WordDictionary" (constructor, args []): create an empty dictionary.
#   - addWord(word): store the word; returns nothing.
#   - search(pattern): True if some stored word matches the pattern exactly
#     (same length, '.' matches any one letter), False otherwise.
#
# Example 1:
#   Input: ops  = ["WordDictionary", "addWord", "addWord", "addWord",
#                  "search", "search", "search", "search"]
#          args = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], ["mad"], ["b.."]]
#   Output: [None, None, None, None, False, True, True, True]
#   Explanation: "pad" was never added; "b.." matches the added "bad".
# Example 2:
#   Input: ops  = ["WordDictionary", "addWord", "search", "search", "search"]
#          args = [[], ["abc"], [".bc"], ["ab."], [".b"]]
#   Output: [None, None, True, True, False]
#   Explanation: "." matches exactly one letter, so ".b" cannot match "abc".
#
# Constraints:
#   - 1 <= len(ops) <= 1000
#   - 0 <= len(word), len(pattern) <= 20
#   - word and pattern consist of lowercase English letters; pattern may use '.'
# ---------------------------------------------------------------------------
def p2_add_and_search(ops, args):
    """ops: list of operation names. args: list of argument lists, same length.
    Return a list with one result per operation: None for the constructor,
    otherwise the operation's return value (None when it returns nothing).
    """
    END = "\0"
    root = {}

    def add(word):
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node[END] = True

    def matches(node, pattern, i):
        """True if pattern[i:] can be completed from `node`."""
        if i == len(pattern):
            return END in node
        ch = pattern[i]
        if ch == ".":
            # Wildcard: try every child (but never the END marker).
            return any(
                key != END and matches(child, pattern, i + 1)
                for key, child in node.items()
            )
        child = node.get(ch)
        return child is not None and matches(child, pattern, i + 1)

    out = []
    for op, a in zip(ops, args):
        if op == "WordDictionary":
            out.append(None)
        elif op == "addWord":
            add(a[0])
            out.append(None)
        elif op == "search":
            out.append(matches(root, a[0], 0))
    return out


# ---------------------------------------------------------------------------
# Problem 3 - Word Search II  (LeetCode 212)
#
# Given an m x n board of single-character strings and a list of distinct
# words, return every word that can be formed by a path of horizontally or
# vertically adjacent cells. The same cell may not be used more than once
# while forming a word. Return the words in the order they appear in `words`.
#
# Example 1:
#   Input: board = [["o", "a", "a", "n"],
#                   ["e", "t", "a", "e"],
#                   ["i", "h", "k", "r"],
#                   ["i", "f", "l", "v"]]
#          words = ["oath", "pea", "eat", "rain"]
#   Output: ["oath", "eat"]
#   Explanation: "pea" and "rain" cannot be formed anywhere on the board.
# Example 2:
#   Input: board = [["a", "b"],
#                   ["c", "d"]]
#          words = ["abcb"]
#   Output: []
#   Explanation: "abcb" would have to reuse the 'b' cell.
#
# Constraints:
#   - 1 <= len(board), len(board[0]) <= 12
#   - 1 <= len(words) <= 100
#   - 1 <= len(words[i]) <= 10
#   - Cells are lowercase English letters; words are distinct and lowercase
# ---------------------------------------------------------------------------
def p3_find_words(board, words):
    # Build a trie of the words, then DFS from every cell while walking the
    # trie: a branch that leaves the trie is pruned immediately.
    END = "\0"
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node[END] = True

    rows = len(board)
    cols = len(board[0]) if rows else 0
    found = set()

    def dfs(r, c, node, path):
        ch = board[r][c]
        node = node.get(ch)
        if node is None:
            return  # this prefix is not in the trie
        path.append(ch)
        if END in node:
            found.add("".join(path))
        if node:  # there are longer words below this prefix
            board[r][c] = "#"  # block reusing this cell on the current path
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node, path)
            board[r][c] = ch
        path.pop()

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, [])
    return [w for w in words if w in found]


if __name__ == "__main__":
    tests = [
        # ---- Problem 1: Implement Trie ------------------------------------
        ("P1 trie example", p1_implement_trie,
         (["Trie", "insert", "search", "search", "startsWith", "startsWith"],
          [[], ["apple"], ["apple"], ["app"], ["app"], ["appl"]]),
         [None, None, True, False, True, True]),
        ("P1 trie single char", p1_implement_trie,
         (["Trie", "search", "startsWith", "insert", "search", "startsWith"],
          [[], ["a"], ["a"], ["a"], ["a"], ["a"]]),
         [None, False, False, None, True, True]),
        ("P1 trie empty word", p1_implement_trie,
         (["Trie", "search", "insert", "search", "startsWith"],
          [[], [""], [""], [""], [""]]),
         [None, False, None, True, True]),
        ("P1 trie duplicate insert", p1_implement_trie,
         (["Trie", "insert", "insert", "search", "search", "startsWith"],
          [[], ["app"], ["app"], ["app"], ["apps"], ["apps"]]),
         [None, None, None, True, False, False]),
        ("P1 trie shared prefixes", p1_implement_trie,
         (["Trie", "insert", "insert", "insert", "search", "search", "startsWith", "startsWith"],
          [[], ["car"], ["care"], ["cart"], ["car"], ["ca"], ["car"], ["care"]]),
         [None, None, None, None, True, False, True, True]),
        # ---- Problem 2: Add and Search Words ------------------------------
        ("P2 add_search example", p2_add_and_search,
         (["WordDictionary", "addWord", "addWord", "addWord",
           "search", "search", "search", "search"],
          [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], ["mad"], ["b.."]]),
         [None, None, None, None, False, True, True, True]),
        ("P2 add_search empty dict", p2_add_and_search,
         (["WordDictionary", "search", "search"],
          [[], ["a"], ["."]]),
         [None, False, False]),
        ("P2 add_search single char", p2_add_and_search,
         (["WordDictionary", "addWord", "search", "search", "search"],
          [[], ["a"], ["."], ["a"], [".."]]),
         [None, None, True, True, False]),
        ("P2 add_search wildcards", p2_add_and_search,
         (["WordDictionary", "addWord", "addWord", "search", "search", "search", "search"],
          [[], ["mad"], ["madness"], ["m.d"], ["mad.ess"], ["madnes"], ["madness"]]),
         [None, None, None, True, True, False, True]),
        ("P2 add_search trailing dot", p2_add_and_search,
         (["WordDictionary", "addWord", "search", "search", "search", "search", "search"],
          [[], ["abc"], [".bc"], ["ab."], [".b"], ["abc"], ["."]]),
         [None, None, True, True, False, True, False]),
        # ---- Problem 3: Word Search II ------------------------------------
        ("P3 word_search example", p3_find_words,
         ([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
          ["oath", "pea", "eat", "rain"]),
         ["oath", "eat"]),
        ("P3 word_search no cell reuse", p3_find_words,
         ([["a", "b"], ["c", "d"]], ["abcb", "abd", "acd"]),
         ["abd", "acd"]),
        ("P3 word_search single cell", p3_find_words,
         ([["a"]], ["a", "b", "aa"]),
         ["a"]),
        ("P3 word_search repeated letter", p3_find_words,
         ([["a", "a"]], ["aaa", "aa", "a"]),
         ["aa", "a"]),
        ("P3 word_search prefix words", p3_find_words,
         ([["c", "a", "r"], ["x", "x", "t"]], ["cart", "car", "cat", "art"]),
         ["cart", "car", "art"]),
        ("P3 word_search zigzag", p3_find_words,
         ([["a", "b"], ["b", "a"]], ["ababa", "abab", "aba"]),
         ["abab", "aba"]),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
