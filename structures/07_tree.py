"""
STRUCTURA: TREE (arbore binar) și BST (arbore binar de căutare)

Ce este:
    Un arbore binar = noduri, fiecare cu maxim 2 copii (left, right).
    Un BST are în plus regula: tot ce e în stânga < nod < tot ce e în dreapta.

Traversări (toate O(n)):
    preorder   nod -> left -> right     (copiere, serializare)
    inorder    left -> nod -> right     (pe BST dă elementele SORTATE)
    postorder  left -> right -> nod     (ștergere, path sum)
    level-order (BFS)                   (nivel cu nivel, shortest path)

Operații BST (medie O(log n), dar O(n) dacă arborele e dezechilibrat):
    search / insert / delete

Ideea-cheie:
    Pe tree se rezolvă în general RECURSIV: rezolvi subarborele, apoi combini la nod.
    Pentru „nivel cu nivel" folosești o coadă (BFS).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------- Traversări ----------

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root):
    """BFS cu coadă — returnează o listă de niveluri."""
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


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    """Verifică proprietatea de BST ținând intervalul (low, high)."""
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_bst(root.left, low, root.val)
            and is_valid_bst(root.right, root.val, high))


# ---------- BST ----------

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            cur = cur.left if val < cur.val else cur.right
        return False

    def delete(self, val):
        def _delete(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                # caz 1/2: zero sau un copil
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # caz 3: doi copii -> înlocuim cu minimul din dreapta
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.val = succ.val
                node.right = _delete(node.right, succ.val)
            return node
        self.root = _delete(self.root, val)

    def inorder(self):
        return inorder(self.root)


if __name__ == "__main__":
    # Arbore binar:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("preorder  :", preorder(root))       # [1, 2, 4, 5, 3]
    print("inorder   :", inorder(root))        # [4, 2, 5, 1, 3]
    print("postorder :", postorder(root))      # [4, 5, 2, 3, 1]
    print("level-order:", level_order(root))   # [[1], [2, 3], [4, 5]]
    print("max_depth :", max_depth(root))      # 3

    bst = BST()
    for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(x)
    print("BST inorder:", bst.inorder())       # sortat
    print("search(6) ->", bst.search(6))
    print("is_valid_bst ->", is_valid_bst(bst.root))
    bst.delete(10)
    print("dupa delete(10):", bst.inorder())
