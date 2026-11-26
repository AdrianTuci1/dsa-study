"""
CONCEPT: Fast & Slow Pointers (linked-list cycle / middle)

Solve the 3 problems below by replacing each `raise NotImplementedError`
with your own solution. Statements are in English.

Run this file to check your work:

    python3 practice/04_fast_slow_pointers.py

The file prints [ ] for problems not solved yet, [v] for passing tests,
and [x] for failing tests.
"""
from _harness import run, summary


# ---------------------------------------------------------------------------
# Problem 1 - Linked List Cycle  (LeetCode 141)
#
# You receive the node values of a singly linked list as a plain list, plus an
# index `pos`. Build the linked list inside the function, then connect the
# last node back to the node at index `pos` when `pos >= 0` (a negative `pos`
# means no cycle). Return True if the resulting list contains a cycle and
# False otherwise. Use two pointers moving at different speeds.
#
# Example 1:
#   Input: values = [3, 2, 0, -4], pos = 1
#   Output: True
#   Explanation: the tail connects back to the node holding 2
# Example 2:
#   Input: values = [1, 2], pos = -1
#   Output: False
#
# Constraints:
#   - 0 <= len(values) <= 10^4
#   - -1 <= pos < len(values)
# ---------------------------------------------------------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def p1_has_cycle(values, pos):
    if not values:
        return False
    
    nodes = [Node[v] for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
        if pos >= 0:
            nodes[-1].next = nodes[pos]

        slow = fast = nodes[0]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    


# ---------------------------------------------------------------------------
# Problem 2 - Middle of the Linked List  (LeetCode 876)
#
# You receive the node values of a singly linked list as a plain list. Build
# the linked list inside the function and return the value of its middle node.
# When the list has two middle nodes (even length), return the second one. If
# the list is empty, return -1. Use a slow pointer that moves one step for
# every two steps of the fast pointer.
#
# Example 1:
#   Input: values = [1, 2, 3, 4, 5]
#   Output: 3
# Example 2:
#   Input: values = [1, 2, 3, 4]
#   Output: 3
#   Explanation: the two middle nodes are 2 and 3, so return the second
#
# Constraints:
#   - 0 <= len(values) <= 100
#   - -100 <= values[i] <= 100
# ---------------------------------------------------------------------------
def p2_middle_node(values):
    if not values:
        return -1
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    
    slow = fast = nodes[0]
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val



# ---------------------------------------------------------------------------
# Problem 3 - Find the Duplicate Number  (LeetCode 287)
#
# Given a list of n + 1 integers where every value lies in the range [1, n],
# exactly one value is duplicated (it may appear more than twice). Return that
# duplicated value. The input is a plain list, so treat each value as a "next"
# pointer and apply the fast & slow pointer idea directly to the indices.
#
# Example 1:
#   Input: nums = [1, 3, 4, 2, 2]
#   Output: 2
# Example 2:
#   Input: nums = [3, 1, 3, 4, 2]
#   Output: 3
#
# Constraints:
#   - 2 <= len(nums) <= 10^5
#   - 1 <= nums[i] <= len(nums) - 1
#   - only one value is repeated
# ---------------------------------------------------------------------------
def p3_find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow



if __name__ == "__main__":
    tests = [
        ("P1 has_cycle", p1_has_cycle, ([3, 2, 0, -4], 1), True),
        ("P1 has_cycle", p1_has_cycle, ([1, 2], -1), False),
        ("P1 has_cycle", p1_has_cycle, ([1], 0), True),
        ("P1 has_cycle", p1_has_cycle, ([7], -1), False),
        ("P1 has_cycle", p1_has_cycle, ([], -1), False),

        ("P2 middle_node", p2_middle_node, ([1, 2, 3, 4, 5],), 3),
        ("P2 middle_node", p2_middle_node, ([1, 2, 3, 4],), 3),
        ("P2 middle_node", p2_middle_node, ([1, 2],), 2),
        ("P2 middle_node", p2_middle_node, ([7],), 7),
        ("P2 middle_node", p2_middle_node, ([],), -1),

        ("P3 find_duplicate", p3_find_duplicate, ([1, 3, 4, 2, 2],), 2),
        ("P3 find_duplicate", p3_find_duplicate, ([3, 1, 3, 4, 2],), 3),
        ("P3 find_duplicate", p3_find_duplicate, ([1, 1],), 1),
        ("P3 find_duplicate", p3_find_duplicate, ([2, 2, 2, 2, 2],), 2),
        ("P3 find_duplicate", p3_find_duplicate, ([1, 4, 4, 2, 4],), 4),
    ]
    summary([run(label, fn, args, expected) for label, fn, args, expected in tests])
