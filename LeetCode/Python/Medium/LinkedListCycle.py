# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def hasCycle(self, head: ListNode) -> bool:
      dict = {}
        
      if head:
         while head is not None:
            if dict.get(head):
               return True

            else:
               dict[head] = 1

            head = head.next
      return False