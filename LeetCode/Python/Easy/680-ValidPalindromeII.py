class Solution:
    def validPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1
        
        while ptr2 > ptr1:
            
            if s[ptr1] != s[ptr2]:
                modPtr1 = s[ptr1+1:ptr2+1]
                modPtr2 = s[ptr1:ptr2]
                
                return self.checkPalin(modPtr1) or self.checkPalin(modPtr2)
            
            ptr1 += 1
            ptr2 -= 1
            
        return True
            
        
    def checkPalin(self, s):
        
        return s[::-1] == s