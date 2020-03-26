import math
class Solution:
   def sumFourDivisors(self, nums: List[int]) -> int:
      total = 0
        
      for n in nums:
            
         total += self.fourDivisors(n)
        
      return total
            
   def fourDivisors(self, n) -> int:
        
      divisors = []
      i = 1
        
      while i <= math.sqrt(n):
            
         if n % i == 0:
                
            if len(divisors) > 4:
               return 0
                
            elif n / i == i:
               divisors.append(i)
                
            else:
               divisors.append(i)
               divisors.append(n/i)
            
         i += 1
        
      if len(divisors) != 4:
         return 0
        
      else:
         return int(sum(divisors))