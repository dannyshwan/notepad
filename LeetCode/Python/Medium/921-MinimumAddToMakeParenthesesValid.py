class Solution:
  def minAddToMakeValid(self, s: str) -> int:
    stack = []
    changes = 0
    
    for bracket in s:
      if bracket == ")" and not stack:
        changes += 1
      elif bracket == ")":
        stack.pop()
      else:
        stack.append(bracket)
            
    changes += len(stack)
    return changes