# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur( node, min_value, max_value ):
            if not node:
                return True
            
            if not (min_value < node.val < max_value):
                return False
            else:
                return recur(node.left, min_value, node.val) and recur(node.right, node.val, max_value)
            
        
        return recur(root, float('-inf'), float('inf'))
        