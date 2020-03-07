class Solution:
   def rotateString(self, A: str, B: str) -> bool:
        
      #Assuming B is a shifted version of A, B should be in A if you add A and itself together
      return len(A) == len(B) and B in (A+A)   