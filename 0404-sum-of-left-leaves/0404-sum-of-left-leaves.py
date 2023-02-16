# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        sum_leaves = [0]
        def sumLeftNodes( node, isLeft):
            if not node:
                return
            if not node.right and not node.left and isLeft:
                sum_leaves[0] += node.val
                return
            sumLeftNodes( node.right, False)
            sumLeftNodes( node.left, True)
        
        sumLeftNodes(root, False)
        return sum_leaves[0]
        
            
            
                
                
        