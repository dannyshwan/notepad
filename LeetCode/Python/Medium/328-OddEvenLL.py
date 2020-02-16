# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
   def oddEvenList(self, head: ListNode) -> ListNode:
        
      if head and head.next:
         odd = ListNode(head.val)
         even = ListNode(head.next.val)

         ptr = head.next.next
         counter = 1

         head = odd
         startOfEven = even

         while ptr:

            if counter%2 == 0:
               even.next = ptr
               even = even.next

            else:
               odd.next = ptr
               odd = odd.next

            ptr = ptr.next
            counter += 1

         even.next = None
         odd.next = startOfEven
        
      return head