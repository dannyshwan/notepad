class Solution:
   def checkIfExist(self, arr: List[int]) -> bool:
        
      for m in arr:
         n = m*2
            
         if n in arr:
                
            if (n != m) or (arr.count(n) > 1):
               return True
                
      return False