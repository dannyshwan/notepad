class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dict = {}
      anagrams = []
        
      for i in range(len(strs)):
         temp = ''.join(sorted(strs[i]))
            
         if dict.get(temp):
            dict[temp].append(strs[i])
         else:
            dict[temp] = []
            dict[temp].append(strs[i])
        
      for key in dict:
         anagrams.append(dict[key])
            
      return anagrams