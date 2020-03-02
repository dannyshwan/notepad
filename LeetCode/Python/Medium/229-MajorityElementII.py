'''
Not O(1) space though, need to rethink
'''
class Solution:
   def majorityElement(self, nums: List[int]) -> List[int]:
        
      majority = list(set(nums))
        
      for i in range(len(majority)):
         if nums.count(majority[i]) <= (len(nums)/3):
            majority[i] = 'remove'
        
      return [value for value in majority if value != 'remove']