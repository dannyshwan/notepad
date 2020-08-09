# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def minDepth(self, root: TreeNode) -> int:
       
      depthLeft = float("inf")
      depthRight = float("inf")
      
      if root:
         if not root.left and not root.right:
            return 1
         if root.left:
            depthLeft = 1 + self.minDepth(root.left)
         if root.right:
            depthRight = 1 + self.minDepth(root.right)
         return min(depthLeft, depthRight)
      
      return 0