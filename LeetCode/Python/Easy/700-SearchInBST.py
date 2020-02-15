# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
   def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
      return self.dfs(root, val)
    
   def dfs(self, root, val):
        
      if not root:
         return
        
      elif root.val == val:
         return root
        
      else:
         if val > root.val:
            return self.dfs(root.right, val)
         else:
            return self.dfs(root.left, val)