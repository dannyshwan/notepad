class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      retVal = []
      window = nums[0:k]
      maxVal = max(window)
      
      retVal.append(maxVal)
      
      for i in range(k,len(nums)):
          
         window.pop(0)
         window.append(nums[i])
         
         if maxVal not in window:
            maxVal = max(window)
             
         elif maxVal < nums[i]:
            maxVal = nums[i]
         
         retVal.append(maxVal)
      
      return retVal