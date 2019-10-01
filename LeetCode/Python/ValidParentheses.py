def isValid(self, s: str) -> bool:
   stack = []
   map = {
      "(": ")",
      "{": "}",
      "[": "]"
   }
        
   #All valid parentheses strings are even in length, return false if odd
   if len(s)%2 != 0:
      return False
        
   for char in s:
            
      if char in map.keys():
         stack.append(char)
            
      else:
         if stack and map[stack[-1]] == char:
            stack.pop()
         else:
            return False
            
   return True if not stack else False