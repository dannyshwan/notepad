# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
       
      values = {}
      
      ptr = headA
      
      while ptr:
         values[ptr] = ptr
         ptr = ptr.next
      
      ptr = headB
      
      while ptr:
         if values.get(ptr):
            return ptr
          
         ptr = ptr.next
          
      return None