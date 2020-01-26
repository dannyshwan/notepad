class Solution:
   def majorityElement(self, nums: List[int]) -> int:
        
      setOfNums = set(nums)
        
      for n in setOfNums:
         if nums.count(n) > len(nums)/2:
            return n