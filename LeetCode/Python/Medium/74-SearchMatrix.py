class Solution:
   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
      if matrix and matrix[0]:
         for row in matrix:

            if target > row[-1]: continue

            l = 0
            h = len(row) -1

            while l <= h:
               mid = l + h-l//2

               if row[mid] == target: 
                  return True

               elif row[mid] < target: 
                  l = mid + 1

               else:
                  h = mid - 1 
            
      return False