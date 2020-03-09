'''
LOL trash implementation oof 
'''
class MinStack:

   def __init__(self):
      """
      initialize your data structure here.
      """
      self.stack = []
      self.min = {}
        

   def push(self, x: int) -> None:
      self.stack.append(x)
      self.min[x] = -1
        
   def pop(self) -> None:
      temp = self.top()
      self.stack.pop()

      if temp not in self.stack:
         del self.min[temp]
        
   def top(self) -> int:
      return self.stack[-1]

   def getMin(self) -> int:
      return min(self.min.keys())