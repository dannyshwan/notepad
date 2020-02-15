# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution:
   def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
      
      t = TreeNode(-1)
      return self.dfs(t1,t2,t)
        
        
   def dfs(self, tree1, tree2, finalTree):
        
      if tree1 and tree2:
         finalTree = TreeNode(tree1.val+tree2.val)
         finalTree.left = self.dfs(tree1.left, tree2.left, finalTree.left)
         finalTree.right = self.dfs(tree1.right, tree2.right, finalTree.right)
        
      elif tree1:
         finalTree = tree1
            
      else:
         finalTree = tree2
        
      return finalTree