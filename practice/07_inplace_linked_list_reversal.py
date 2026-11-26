"""
CONCEPT: In-place Linked List Reversal

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Each function receives a plain list of node values. Build a singly linked
list from those values inside the function, reverse the links in place, and
return a plain value. Do not build a new reversed list with slicing.

Run this file to check your work:

    python3 practice/07_inplace_linked_list_reversal.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Reverse Linked List  (LeetCode 206)
#
# Given the values of a singly linked list, reverse the list by changing the
# next pointers, then return the resulting values in order. An empty list
# reverses to an empty list.
#
# Example 1:
#   Input: values = [1,2,3,4,5]
#   Output: [5,4,3,2,1]
# Example 2:
#   Input: values = [1,2]
#   Output: [2,1]
#
# Constraints:
#   - 0 <= len(values) <= 5000
#   - -5000 <= values[i] <= 5000
# ---------------------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def p1_reverse(values):
    # schelarie: lista simpla -> lista inlantuirata (conventia din structures/02_linked_list.py)
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    head = dummy.next

    # algoritmul: intorc fiecare sageata
    prev, curr = None, head
    while curr:
        nxt = curr.next      # 1. salveaza restul
        curr.next = prev     # 2. intoarce sageata
        prev = curr          # 3. avanseaza prev
        curr = nxt           # 4. avanseaza curr
    
    return [...] #valorile pornind din prev


# ---------------------------------------------------------------------------
# Problem 2 - Reverse Linked List II  (LeetCode 92)
#
# Given the values of a singly linked list and positions left and right
# (1-indexed), reverse only the nodes from position left to position right,
# then return the resulting values in order. Use one pass and in-place
# pointer changes.
#
# Example 1:
#   Input: values = [1,2,3,4,5], left = 2, right = 4
#   Output: [1,4,3,2,5]
# Example 2:
#   Input: values = [1,2,3], left = 1, right = 3
#   Output: [3,2,1]
#
# Constraints:
#   - 1 <= len(values) <= 5000
#   - left <= right, both are valid 1-indexed positions in the list
# ---------------------------------------------------------------------------
def p2_reverse_between(values, left, right):
    #schelarie
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    #1. ma pozitionez chiar inaintea ferestrei
    prev = dummy
    for _ in range(left - 1):

        #2. curr = primul nod din fereastra; el va ajunge ultimul si nu se misca niciodata
        curr = prev.next

    #3. de right - left ori, mut nodul de dupa curr in fruntea ferestrei
    for _ in range(right - left):
        nxt = curr.next #nodul pe care il mut
        curr.next = nxt.next #curr sare peste el (il scoate din lant)
        nxt.next = prev.next #il lipesc inaintea capului actual al ferestrei
        prev.next = nxt #si il declar noul cap al ferestrei
    
    #4. Capul listei e mereu dummy.next
    out, node = [], dummy.next
    while node:
        out.append(node.val)
        node = node.next
    return out


# ---------------------------------------------------------------------------
# Problem 3 - Swap Nodes in Pairs  (LeetCode 24)
#
# Given the values of a singly linked list, swap every two adjacent nodes and
# return the resulting values in order. If the list has an odd number of
# nodes, the last node stays in place. Do not swap the values themselves;
# rewire the nodes.
#
# Example 1:
#   Input: values = [1,2,3,4]
#   Output: [2,1,4,3]
# Example 2:
#   Input: values = [1,2,3]
#   Output: [2,1,3]
#
# Constraints:
#   - 0 <= len(values) <= 100
#   - 0 <= values[i] <= 100
# ---------------------------------------------------------------------------
def p3_swap_pairs(values):
    #schelarie
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    
    prev = dummy
    while prev.next and prev.next.next: #am nevoie de 2 noduri intregi
        first = prev.next
        second = first.next

        prev.next = second #1. exteriorul: perechea incepe cu second
        first.next = second.next #2. "first" preia restul listei
        second.next = first #3. second arata inapoi spre first
        prev = first #4. first e acum coada perechii

        out, node = [], dummy.next
        while node:
            out.append(node.val)
            node = node.next
        return out




if __name__ == "__main__":
    tests = [
        ("P1 reverse", p1_reverse, ([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1]),
        ("P1 reverse pair", p1_reverse, ([1, 2],), [2, 1]),
        ("P1 reverse single", p1_reverse, ([1],), [1]),
        ("P1 reverse empty", p1_reverse, ([],), []),
        ("P2 reverse_between", p2_reverse_between, ([1, 2, 3, 4, 5], 2, 4), [1, 4, 3, 2, 5]),
        ("P2 reverse_between full", p2_reverse_between, ([1, 2, 3], 1, 3), [3, 2, 1]),
        ("P2 reverse_between single", p2_reverse_between, ([5], 1, 1), [5]),
        ("P3 swap_pairs", p3_swap_pairs, ([1, 2, 3, 4],), [2, 1, 4, 3]),
        ("P3 swap_pairs odd", p3_swap_pairs, ([1, 2, 3],), [2, 1, 3]),
        ("P3 swap_pairs single", p3_swap_pairs, ([1],), [1]),
        ("P3 swap_pairs empty", p3_swap_pairs, ([],), []),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
