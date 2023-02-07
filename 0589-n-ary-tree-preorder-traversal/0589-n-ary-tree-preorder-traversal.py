"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        def recur(node):
            if not node:
                return
            answer.append(node.val)
            for child in node.children:
                recur(child)
            
        recur(root)
        return answer
            
        