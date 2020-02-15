# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def removeElements(self, head: ListNode, val: int) -> ListNode:
        
      ptr = head
      before = None
      
      while ptr != None:
          
          if ptr.val == val:
              
              if ptr != head:
                  before.next = ptr.next
              else:
                  head = ptr.next
                  
          else:
              before = ptr
                  
          ptr = ptr.next
      return head