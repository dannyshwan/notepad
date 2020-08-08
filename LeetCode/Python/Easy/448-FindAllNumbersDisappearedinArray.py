class Solution:
   def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      numsAsSet = set(nums)
      listOfUniques = set(list(range(1,len(nums)+1)))
      
      retList = listOfUniques.difference(numsAsSet)
      return list(retList)