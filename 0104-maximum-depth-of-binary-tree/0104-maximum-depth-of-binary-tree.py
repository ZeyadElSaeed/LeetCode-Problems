# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]
        
        def findMax(node, prev_nodes):
            if not node:
                return
            max_depth[0] = max(max_depth[0], prev_nodes+1)
            findMax(node.right, prev_nodes+1)
            findMax(node.left, prev_nodes+1)
            
        findMax(root, 0)
        return max_depth[0]
            
        