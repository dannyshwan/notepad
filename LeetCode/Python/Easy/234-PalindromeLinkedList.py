# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
   def isPalindrome(self, head: ListNode) -> bool:
      values = []
        
      if head:
         ptr = head
      else:
         return True
        
      while ptr.next:
         values.append(ptr.val)
         ptr = ptr.next
        
      values.append(ptr.val)
        
      stack1 = values[:len(values)//2]
      stack2 = values[len(values)//2:]
        
      if len(values)%2 != 0: stack2.pop(0)
        
      while stack1 and stack2:
         if stack1[-1] != stack2[0]:
            return False
            
         stack1.pop()
         stack2.pop(0)
        
      return True