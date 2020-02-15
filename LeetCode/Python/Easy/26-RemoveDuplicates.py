'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
'''
def removeDuplicates(self, nums: List[int]) -> int:
        
   for n in nums:
      indexOfN = nums.index(n)
      numOfN = nums.count(n)
            
      del nums[indexOfN+1:indexOfN+numOfN]