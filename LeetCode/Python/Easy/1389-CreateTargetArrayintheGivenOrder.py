class Solution:
   def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
      target = []
      checkIfOnlyZeros = set(index)
      if len(checkIfOnlyZeros) == 1:
         target = nums[::-1]
        
      else:
         for i in range(len(nums)):
            try:
               temp = index[i]
               if target[temp]:
                  target = target[:temp] + [nums[i]] + target[temp:]
            except IndexError:
                  target.append(nums[i])
                
      return target  