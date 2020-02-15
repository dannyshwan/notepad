# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def deleteDuplicates(self, head: ListNode) -> ListNode:
       
      ptr = head
      target = ptr
      
      while ptr != None:
          
         if ptr.val != target.val:
            target.next = ptr
            target = ptr
         
         if not ptr.next:
            target.next = None
      
         ptr = ptr.next
      
      return head