# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListIterative(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def reverseListRecursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    
    return result


# Example 1: Iterative
head1 = [1,2,3,4,5]
head1 = createLinkedList(head1)
reversed_head1 = reverseListIterative(head1)
print(linkedListToList(reversed_head1))

# [1, 1, 2, 3, 4, 4]