"""
STRUCTURA: TRIE (arbore de prefixe / Prefix Tree)

Ce este:
    Un arbore în care fiecare nod reprezintă un prefix, iar muchiile sunt caractere.
    Fiecare nod are un dicționar `children` (caracter -> nod) și un flag `is_word`.

Operații și complexitate: O(L), unde L = lungimea cuvântului
    insert(word)          O(L)
    search(word)          O(L)
    starts_with(prefix)   O(L)

Ideea-cheie:
    Foarte rapid la căutări de PREFIX (autocomplete) și la cuvinte cu wildcard.
    Spațiu: O(total caractere) — prefixele comune sunt partajate, deci nu
    duplicăm „car" în „car", „care", „carte".
"""


class TrieNode:
    def __init__(self):
        self.children = {}      # caracter -> TrieNode
        self.is_word = False    # True dacă un cuvânt se termină aici


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """True doar dacă `word` a fost inserat ca atare."""
        node = self._traverse(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        """True dacă există vreun cuvânt care începe cu `prefix`."""
        return self._traverse(prefix) is not None

    def _traverse(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def words_with_prefix(self, prefix):
        """Toate cuvintele care încep cu `prefix` (demo de autocomplete)."""
        node = self._traverse(prefix)
        if node is None:
            return []
        result = []

        def dfs(cur, path):
            if cur.is_word:
                result.append(prefix + path)
            for ch, nxt in cur.children.items():
                dfs(nxt, path + ch)

        dfs(node, "")
        return result

    def search_wildcard(self, pattern):
        """Caută cu '.' ca wildcard (orice caracter). Folosit la Word Search II."""
        def dfs(node, i):
            if i == len(pattern):
                return node.is_word
            ch = pattern[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    t = Trie()
    for w in ["car", "care", "cart", "dog"]:
        t.insert(w)

    print("search('car')        ->", t.search("car"))          # True
    print("search('ca')         ->", t.search("ca"))           # False (nu e cuvant)
    print("starts_with('ca')    ->", t.starts_with("ca"))      # True
    print("starts_with('cat')   ->", t.starts_with("cat"))     # True
    print("starts_with('z')     ->", t.starts_with("z"))       # False
    print("autocomplete 'car*'  ->", t.words_with_prefix("car"))  # ['car','care','cart']
    print("wildcard 'c.r'       ->", t.search_wildcard("c.r"))  # True
    print("wildcard '.og'       ->", t.search_wildcard(".og"))  # True
