class Solution:
   def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
      mins = {}
      lucky = []
        
      for row in matrix:
         mins[min(row)] = row.index(min(row))
        
      lucky = list(mins.keys())
        
      for minNum in mins.keys():
         for row in matrix:
            if row[mins.get(minNum)] > minNum:
               lucky.remove(minNum)
               break
            
      return lucky  