def ZeroMatrix(matrix: List[List[int]]) -> None:
   """
   Do not return anything, modify matrix in-place instead.
   (same as leetcode Q73)
   """
   m = len(matrix)
   n = len(matrix[0])
        
   indices = set([])
        
   for i in range(m):
            
      hasZero = False
            
      for j in range(n):
                
         if matrix[i][j] == 0:
            hasZero = True
            indices.add(j)
            
         if hasZero:
            matrix[i] = [0]*n

   for i in range(m):
            
      for index in indices:
         matrix[i][index] = 0