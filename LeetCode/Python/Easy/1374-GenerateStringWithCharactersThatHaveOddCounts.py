import random
import string

class Solution:
   def generateTheString(self, n: int) -> str:
      genStr = ''
      letters = string.ascii_lowercase
      spaceRemaining = n
        
      while spaceRemaining != 0:
         if spaceRemaining > 1:
            num = random.randrange(1,spaceRemaining,2)
         else:
            num = 1
                
         char = random.choice(letters)
            
         while genStr.find(char) != -1:
               char= random.choice(letters)
            
         genStr += (char*num)
            
         spaceRemaining = spaceRemaining - num
        
      return genStr