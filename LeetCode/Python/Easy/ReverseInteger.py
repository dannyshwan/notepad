'''
idk why I did this one
'''
class Solution:
   def reverse(self, x: int) -> int:
            
      rev = 0
            
      if x > 0:
         rev = int(str(x)[::-1])
            
      else:
         negative = str(x)[0]
         temp = str(x)[1:]
                
         rev = int(negative + temp[::-1])
         
      if -2**31 <= rev <= 2**31-1:
         return rev
        
      return 0