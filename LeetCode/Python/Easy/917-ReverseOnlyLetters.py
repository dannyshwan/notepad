import string

class Solution:
   def reverseOnlyLetters(self, S: str) -> str:
      stack = []
      reverse = ''
      nonCharLocation = {}
      LETTERS = string.ascii_lowercase + string.ascii_uppercase
        
      for i in range(len(S)):
            
         if S[i] not in LETTERS:
            nonCharLocation[i] = S[i]
            
         else:
            stack.append(S[i])
        
         for i in range(len(S)):
            if not nonCharLocation.get(i):
               reverse += stack.pop()
            
            else:
               reverse += nonCharLocation.get(i)
        
      return reverse