# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
      node = []
      if not head.next:
         head = None
         return head
        
      ptr = head
        
      while ptr:
         node.append(ptr)
         ptr = ptr.next
        
      node[-1*n].next = None
        
      if n == 1:
         node[-1*n-1].next = None
        
      elif len(node) == n:
         head = node[-1*n+1]
            
      else:
         node[-1*n-1].next = node[-1*n+1]
            
      return head