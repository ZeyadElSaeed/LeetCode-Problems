# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def equalNodes(root1, root2):
            if (root1 == None and root2 == None):
                return True
            elif ( root1 == None or root2 == None):
                return False
            elif ( root1.val != root2.val):
                return False
            else:
                return (root1.val == root2.val) and (equalNodes(root1.left, root2.left)) and (equalNodes(root1.right, root2.right))
            
        return equalNodes(p, q)
        