# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dict = {}
        
        slow = head
        fast = head
        
        try:
            if not head.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
            while slow != fast:
                slow = slow.next
                fast = fast.next.next

        except:
            return False
        
        return True