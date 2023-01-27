"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy_dict = { None: None}
        
        cur = head
        while cur:
            copy = Node(x = cur.val)
            old_copy_dict[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = old_copy_dict[cur]
            copy.next = old_copy_dict[cur.next]
            copy.random = old_copy_dict[cur.random]
            cur = cur.next
            
        return old_copy_dict[head]
        