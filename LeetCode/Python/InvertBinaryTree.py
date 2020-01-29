# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
   def invertTree(self, root: TreeNode) -> TreeNode:
        
      if root:
         
         temp = root.left if root.left else None
            
         root.left = root.right
         root.right = temp

         if root.left: self.invertTree(root.left)
         if root.right: self.invertTree(root.right)
        
      return root