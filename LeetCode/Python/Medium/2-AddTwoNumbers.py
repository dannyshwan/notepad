class ListNode:
   def __init__(self, x):
      self.val = x
      self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
   retVal = ListNode(-1)
   ptr = retVal
   carry = 0
   endWithCarry = False
        
   if l1 == None:
      return l2
        
   if l2 == None:
      return l1
        
   while l1 or l2 or carry:
        
      l1Value = l1.val if l1 else 0
      l2Value = l2.val if l2 else 0
      temp = l1Value + l2Value + carry
      carry = temp//10
      temp = temp%10
            
      ptr.next = ListNode(temp)
      ptr = ptr.next
            
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
            
   return retVal.next