class TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution:
   def inorderTraversal(self, root: TreeNode) -> List[int]:
        
      retval = []
      if root:
         self.recursiveInOrderTraversal(retval, root)
        
      return retval
    
   def recursiveInOrderTraversal(self, retval, root):
        
      if not root.left and not root.right:
         retval.append(root.val)

      else:
         if root.left:
            self.recursiveInOrderTraversal(retval, root.left)
            
         retval.append(root.val)
            
         if root.right:
            self.recursiveInOrderTraversal(retval, root.right)