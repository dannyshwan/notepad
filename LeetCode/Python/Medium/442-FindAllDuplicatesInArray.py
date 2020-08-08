class Solution:
   def findDuplicates(self, nums: List[int]) -> List[int]:
       
      seen = {}
      retList = []
      
      for i in range(len(nums)):
          
         if seen.get(nums[i]):
            retList.append(nums[i])
         
         else:
            seen[nums[i]] = nums[i]
              
      return retList