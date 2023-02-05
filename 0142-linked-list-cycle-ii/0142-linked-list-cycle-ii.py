# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        #detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            # There is a cycle
            if slow == fast:
                cur = head
                while cur != slow:
                    cur = cur.next
                    slow = slow.next
                return cur
        
            
            
        