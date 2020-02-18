class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
      substrings = []
        
      for i in range(len(s)):
         ptr = i
         dict = {}
         str = ""
            
         while ptr < len(s) and not dict.get(s[ptr]):
               dict[s[ptr]] = True
               str += s[ptr]
               ptr += 1
            
         substrings.append(len(str))   
                    
      return max(substrings) if substrings else 0