# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def reverseList(self, head: ListNode) -> ListNode:
        
      ptr = head
      prev = None
      if not head:
         return head
        
      while ptr.next:
         head = head.next
         ptr.next = prev
         prev = ptr
         ptr = head
        
      head.next = prev
        
      return head