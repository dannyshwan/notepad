class Solution:
   def searchMatrix(self, matrix, target):
      """
      :type matrix: List[List[int]]
      :type target: int
      :rtype: bool
      """
        
      for row in matrix:
         for item in row:
            if item == target:
               return True
            elif item > target:
               break
      return False