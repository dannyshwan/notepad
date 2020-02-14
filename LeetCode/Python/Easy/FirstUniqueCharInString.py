class Solution:
   def firstUniqChar(self, s: str) -> int:
        
      dict = {}
      unique = -1
        
      for char in s:
         if dict.get(char):
            dict[char] += 1
         else:
            dict[char] = 1
        
      for key in dict:
            
         #The first unique will be the first key
         if dict.get(key) == 1:
            unique = key
            break
        
      if unique != -1:
         return s.find(unique)
        
      return unique