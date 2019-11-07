class Solution:
   def numJewelsInStones(self, J: str, S: str) -> int:
      tempSet = set(S)
      dict = {}
      retVal = 0;
        
      for stone in tempSet:
         dict[stone] = S.count(stone)
            
      for jewel in J:
         if jewel in S: retVal += dict[jewel]
            
      return retVal