# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get the length of the LinkedList
        def linkedListLen( node ):
            length = 0
            cur = head
            while cur:
                length += 1
                cur = cur.next
            return length
        
        length = linkedListLen(head)
        target_index = math.ceil(length//2) 
        cur = head
        while cur and target_index > 0:
            cur = cur.next
            target_index -= 1
        return cur
        
        