class Solution:
   def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      numbers = set(nums)
      dict = {}
      smallerThan = []
        
      for n in numbers:
         dict[n] = nums.count(n)
        
      for number in nums:
         temp = 0
         for i in dict:
            if i < number:
               temp += dict[i]
         smallerThan.append(temp)
                    
      return smallerThan