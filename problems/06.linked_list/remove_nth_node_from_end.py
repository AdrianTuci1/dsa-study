# Given the head of a linked list, remove the nth
#  node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def removeNthFromEnd(head, n):
    #create dummy node to handle the case of removing the head node
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    #advance the first pointer by n+1 nodes
    for _ in range(n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next



# Example 1
head1 = createLinkedList([1, 2, 3, 4, 5])
n1 = 2
new_head1 = removeNthFromEnd(head1, n1)
print(convertToList(new_head1))
# [1, 2, 3, 5]


