# You are given the head of a singly linked-list. The list can be represented as:

# L0 > L1 > ... > L n - 1 > L n - 2

# Reorder the list to be on the following form:

# L0 > Ln > L1 > L n - 1 > L2 > L n - 2 .....

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return head
    
    #1: find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    #split the list into two halves
    first_half = head
    second_half = slow.next
    slow.next = None

    #2: reverse the second half of the linked list
    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second_half = prev

    p1, p2 = first_half, second_half
    while p2:
        next_p1 = p1.next
        next_p2 = p2.next
        p1.next = p2
        p2.next = next_p1
        p1 = next_p1
        p2 = next_p2

    return head



# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(head1)
print(printLinkedList(head1))
# [1, 4, 2, 3]