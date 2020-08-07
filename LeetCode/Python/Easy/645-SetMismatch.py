class Solution:
   def findErrorNums(self, nums: List[int]) -> List[int]:
       
      mismatch = [None,None]
      temp = sorted(nums)
      
      if len(temp) not in temp:
          mismatch[1] = len(temp)
      
      for i in range(len(temp)-1):
         
         if i+1 not in temp:
             mismatch[1] = i+1
   
         if temp[i+1] - temp[i] == 0:
             mismatch[0] = temp[i]
         
         if mismatch[0] and mismatch[1]:
             return mismatch