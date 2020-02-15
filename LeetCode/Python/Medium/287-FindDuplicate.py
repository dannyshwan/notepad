class Solution:
   def findDuplicate(self, nums: List[int]) -> int:
        
      dict = {}
        
      for n in nums:
         if dict.get(n):
            return n
         else:
            dict[n] = 1