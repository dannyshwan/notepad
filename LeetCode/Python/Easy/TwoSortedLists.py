'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

class ListNode:
   def __init__(self, x):
      self.val = x
      self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode):

   pointer1 = l1
   pointer2 = l2
   head = ListNode(-1)
   p = head
        
   if l1 == None:
      return l2
        
   if l2 == None:
      return l1
        
   while pointer1 and pointer2 != None: 
      
      if pointer1.val <= pointer2.val:
         p.next = ListNode(pointer1.val)
         pointer1 = pointer1.next
         p = p.next
    
            
      else:
         p.next = ListNode(pointer2.val)
         pointer2 = pointer2.next
         p = p.next
                
   if pointer1 == None:
      p.next = pointer2
        
   if pointer2 == None:
      p.next = pointer1
        
   return head.next   