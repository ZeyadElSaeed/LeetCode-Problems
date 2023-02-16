# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def sumLeftNodes( node, isLeft):
            if not node:
                return 0
            if not node.right and not node.left:
                return node.val if isLeft else 0
            return sumLeftNodes( node.right, False) + sumLeftNodes( node.left, True)
            
        
        
        return sumLeftNodes(root, False)
        
            
            
                
                
        