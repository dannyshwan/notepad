class Solution:
   def findLucky(self, arr: List[int]) -> int:
       
      arrSet = set(arr)
      lucky = 0
      
      for num in arrSet:
          
         if arr.count(num) == num:
            lucky = num
      
      return lucky if lucky != 0 else -1