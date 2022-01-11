class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openSt = []
        toRemove = set()
        ans = []
        for i,c in enumerate(s):
            
            if c == '(':
                openSt.append(i)
            elif c == ')':
                if openSt:
                    openSt.pop()
                else:
                    toRemove.add(i)
        
        for i in openSt:
            toRemove.add(i)
            
        for i, c in enumerate(s):
            if i not in toRemove:
                ans.append(c)
        
        return "".join(ans)