def isSubstring(s1: str, s2: str) -> bool:
   s1Chars = sorted(s1)
   s2Chars = sorted(s2)
   return True if s1Chars == s2Chars else False

print(isSubstring("waterbottle", "erbottlewat"))