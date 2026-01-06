# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      
        def is_mirror(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:

            if left_node == None and right_node == None:
                return True
          
            if left_node == None or right_node == None:
                return False
          
            if left_node.val != right_node.val:
                return False
          
            return (is_mirror(left_node.left, right_node.right) and 
                    is_mirror(left_node.right, right_node.left))
      
        if root is None:
            return True
          
        return is_mirror(root.left, root.right)