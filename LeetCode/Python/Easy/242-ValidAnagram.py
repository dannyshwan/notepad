class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
      s2 = sorted(s)
      t2 = sorted(t)
      return s2 == t2