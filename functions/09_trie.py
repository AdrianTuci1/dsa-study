"""
TRIE — funcții (fără OOP)

Fără clasă de nod! Un trie = DICȚIONARE IMBRICATE. Fiecare nod e un dict
{ caracter: sub-dict }, iar sfârșitul unui cuvânt e marcat cu cheia specială "$".

    root = {
        "c": {"a": {"r": {"$": True, "e": {"$": True}}}},
        "d": {"o": {"g": {"$": True}}},
    }

Toate operațiile primesc `root` ca argument. Complexitate O(L), L = lungime cuvânt.
"""

END = "$"          # marker: aici se termină un cuvânt


def trie_new():
    return {}


def trie_insert(root, word):
    node = root
    for ch in word:
        node = node.setdefault(ch, {})
    node[END] = True


def trie_search(root, word):
    """True doar dacă `word` a fost inserat întreg."""
    node = root
    for ch in word:
        if ch not in node:
            return False
        node = node[ch]
    return END in node


def trie_starts_with(root, prefix):
    """True dacă există vreun cuvânt care începe cu `prefix`."""
    node = root
    for ch in prefix:
        if ch not in node:
            return False
        node = node[ch]
    return True


def trie_words(root, prefix=""):
    """Toate cuvintele care încep cu `prefix` (autocomplete)."""
    node = root
    for ch in prefix:
        if ch not in node:
            return []
        node = node[ch]
    result = []

    def walk(cur, path):
        if END in cur:
            result.append(prefix + path)
        for ch, sub in cur.items():
            if ch != END:
                walk(sub, path + ch)

    walk(node, "")
    return result


def trie_search_wildcard(root, pattern):
    """Caută cu '.' ca wildcard (orice caracter). Folosit la Word Search II."""
    def walk(node, i):
        if i == len(pattern):
            return END in node
        ch = pattern[i]
        if ch == ".":
            return any(walk(sub, i + 1) for key, sub in node.items() if key != END)
        if ch not in node:
            return False
        return walk(node[ch], i + 1)

    return walk(root, 0)


if __name__ == "__main__":
    root = trie_new()
    for w in ["car", "care", "cart", "dog"]:
        trie_insert(root, w)

    print("search('car')       ->", trie_search(root, "car"))       # True
    print("search('ca')        ->", trie_search(root, "ca"))        # False
    print("starts_with('ca')   ->", trie_starts_with(root, "ca"))   # True
    print("starts_with('z')    ->", trie_starts_with(root, "z"))    # False
    print("autocomplete 'car'  ->", trie_words(root, "car"))        # ['car','care','cart']
    print("wildcard 'c.r'      ->", trie_search_wildcard(root, "c.r"))   # True
    print("wildcard '.og'      ->", trie_search_wildcard(root, ".og"))   # True
