# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
   def maxDepth(self, root: TreeNode) -> int:
        
      depth = 0
        
      if not root: 
         return depth
        
      return self.findDepth(root, depth)
    
   def findDepth(self, root, depth):
        
      if root:
         depth += 1
         return max(self.findDepth(root.left, depth), depth, self.findDepth(root.right, depth))
        
      return depth