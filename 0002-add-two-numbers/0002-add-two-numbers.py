# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = res = ListNode()
        remain = 0
        
        while l1 and l2:
            total = l1.val + l2.val + remain
            remain = total // 10
            new_node = ListNode(val = total%10 )
            ptr.next = new_node
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + remain
            remain = total // 10
            new_node = ListNode(val = total%10 )
            ptr.next = new_node
            ptr = ptr.next
            l1 = l1.next
        while l2:
            total = l2.val + remain
            remain = total // 10
            new_node = ListNode(val = total%10 )
            ptr.next = new_node
            ptr = ptr.next
            l2 = l2.next
        if remain != 0:
            new_node = ListNode(val = remain )
            ptr.next = new_node 
            
        return res.next
            