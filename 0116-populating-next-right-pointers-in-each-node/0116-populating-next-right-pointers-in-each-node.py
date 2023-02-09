"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_q = []
        nextLevel_q = []
        level_q.append(root)
        
        while level_q:
            while level_q:
                node = level_q.pop(0)
                if not node:
                    continue
                if node.left:
                    nextLevel_q.append(node.left) 
                if node.right:
                    nextLevel_q.append(node.right)           
                node.next = None if not level_q else level_q[0]

            level_q = nextLevel_q.copy()
            nextLevel_q = []
            
        return root
        
        