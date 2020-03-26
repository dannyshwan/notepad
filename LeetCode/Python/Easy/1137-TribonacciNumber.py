class Solution:
   def tribonacci(self, n: int) -> int:
        
      T = [0,1,1]
        
      if n < 3:
         return 0 if n == 0 else 1
      
      i = 3
      triboNum = 0
      
      while i <= n:
          
         triboNum = sum(T)
         T.pop(0)
         T.append(triboNum)
         i += 1
      
      return triboNum