class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
      maxLen = 0
      queue = []
        
      for char in s:
         while char in queue:
            maxLen = len(queue) if len(queue) > maxLen else maxLen
            queue.pop(0)
         
         queue.append(char)
      
      maxLen = len(queue) if len(queue) > maxLen else maxLen
          
      return maxLen