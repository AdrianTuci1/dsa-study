# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init_(self, val=0):
        self.val = val
        self.next = None
    

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return false
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return True 
        
        return False 
    


head = [3,2,0,-4]
pos = 1

head = create_linked_list_with_cycle(head, pos)
solution = Solution()
result = solution.hasCycle(head)
print(result)

#True

