'''
Improved solution compared to the one done in JS
'''
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        
      dict = {}
        
      for i in range(len(nums)):
         dict[nums[i]] = i
        
      for j in range(len(nums)):
            
         temp = target - nums[j]     
         if dict.get(temp) and nums[dict[temp]] + nums[j] == target:
                
            if dict[temp] != j: return [j, dict[temp]]