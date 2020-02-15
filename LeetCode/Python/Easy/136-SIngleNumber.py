def singleNumber(self, nums) -> int:
   numberDict = {}

   for num in nums:
      try:
         numberDict.pop(num)
      except:
         numberDict[num] = 1

   return numberDict.popitem()[0]   