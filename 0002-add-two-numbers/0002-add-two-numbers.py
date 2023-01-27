# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = res = ListNode()
        remain = 0
        
        while l1 or l2 or remain:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0
            #calculation
            total = value_1 + value_2 + remain
            remain = total // 10
            new_node = ListNode(val = total%10 )
            ptr.next = new_node
            # update pointers
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return res.next
            