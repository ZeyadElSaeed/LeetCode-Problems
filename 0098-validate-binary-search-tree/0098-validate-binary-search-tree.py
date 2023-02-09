# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # using inorder list to evaluate the order of the values
        def inorder(node, inorder_list):
            if not node:
                return
            inorder(node.left, inorder_list)
            inorder_list.append(node.val)
            inorder(node.right, inorder_list)
            
        def evaluate_inorder(node):
            inorder_list = []
            inorder(node, inorder_list)
            for i in range(1,len(inorder_list)):
                if inorder_list[i-1] >= inorder_list[i]:
                    return False
            return True
                     
                
        # recursive solution with min, max values
        def recursion( node, min_value, max_value ):
            if not node:
                return True
            
            if not (min_value < node.val < max_value):
                return False
            else:
                return recursion(node.left, min_value, node.val) and recursion(node.right, node.val, max_value)
        
        def evaluate_recursion(node):
            return recursion(node, float('-inf'), float('inf') )
            
        return evaluate_inorder(root)
        