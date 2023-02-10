"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:  
        res = []
        def preorder_recursion( node ):
            if node: 
                res.append( node.val )
                for child in node.children:
                    preorder_recursion( child )
            
            
        preorder_recursion(root)
        return res
            
            
        