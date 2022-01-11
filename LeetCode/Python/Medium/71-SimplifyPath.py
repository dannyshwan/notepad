class Solution:
    def simplifyPath(self, path: str) -> str:
        pathSplit = [p for p in path.split('/') if p !="." and p!=""]
        stack = []
        for path in pathSplit:
            if path == "..":
                if stack:
                    stack.pop()
                
            else:
                stack.append(path)
                
        return "/" + "/".join(stack)