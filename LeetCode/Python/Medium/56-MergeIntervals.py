class Solution:
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
      toRemove = {}
      intervals.sort()
      
      for i in range(1,len(intervals)):
          
         if intervals[i-1][-1] >= intervals[i][0]:
            intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
            intervals[i][-1] = max(intervals[i][-1], intervals[i-1][-1])
            toRemove[i] = intervals[i-1]
      
      for key in toRemove:
         intervals.remove(toRemove[key])
              
      return intervals