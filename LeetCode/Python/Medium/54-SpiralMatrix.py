class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       
      row = True
      top = True
      stack = []
      
      while matrix:
          
         if row:
             
            if top:
               stack.extend(matrix[0])
               matrix.pop(0)
            else:
               stack.extend(matrix[-1][::-1])
               matrix.pop(-1)
                
            row = not row
             
         
         else:
             
            if top:
               for i in range(len(matrix)):
                  stack.append(matrix[i][-1])
                  matrix[i].pop(-1)
            
            else:
               tmp = matrix[::-1]
               for i in range(len(tmp)):
                  stack.append(tmp[i][0])
                  tmp[i].pop(0)
               matrix = tmp[::-1]
                
            top = not top
            row = not row
         
         #cleanup
         matrix = [lst for lst in matrix if lst]
              
      return stack