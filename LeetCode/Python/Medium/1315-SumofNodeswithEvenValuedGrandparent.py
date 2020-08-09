# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def sumEvenGrandparent(self, root: TreeNode) -> int:
       
      finalSum = 0  
      even = (root.val%2 == 0)
      if root.left: 
         if even:
            if root.left.left:
               finalSum += root.left.left.val
            if root.left.right:
               finalSum += root.left.right.val
                 
         finalSum += self.sumEvenGrandparent(root.left)
              
      if root.right: 
         if even:
            if root.right.left:
               finalSum += root.right.left.val
            if root.right.right:
               finalSum += root.right.right.val
                 
         finalSum += self.sumEvenGrandparent(root.right)
              
      return finalSum