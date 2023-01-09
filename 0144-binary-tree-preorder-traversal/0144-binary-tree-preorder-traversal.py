# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = list()

        def recursion(node):
            if node == None:
                return
            answer.append(node.val)
            recursion(node.left)
            recursion(node.right)
            
        recursion(root)    
        return answer
        