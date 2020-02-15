class Solution:
   def singleNumber(self, nums: List[int]) -> int:
      dict = {}
        
      for n in nums:
         if dict.get(n):
            dict[n] = dict.get(n) + 1
         else:
            dict[n] = 1
                
      return self.getKey(dict)
                
    
   def getKey(self, dict) -> int:
        
      for tuples in dict.items():
         if tuples[1] == 1:
            return tuples[0]