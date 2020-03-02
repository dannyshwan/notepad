class Solution:
   def sortColors(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      color = 0
        
      for i in range(len(nums)):
         if nums[i] != color:
            while nums[i] != color:
               try:
                  self.swap(nums,color,i)

               except ValueError:
                  color += 1
    
   def swap(self, nums, color, i):
        index = nums[i+1:].index(color)
        temp = nums[index+i+1]
        nums[index+i+1] = nums[i]
        nums[i] = temp