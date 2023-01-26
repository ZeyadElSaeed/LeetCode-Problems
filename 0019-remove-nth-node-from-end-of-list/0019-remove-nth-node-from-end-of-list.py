# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        count = 1
        curr = reverse(head)
        prev = temp_head = ListNode
        temp_head.next = curr
        while curr and count <= n:
            nxt = curr.next
            if count == n:
                prev.next = nxt
                curr.next = None
                break                    
            prev = curr
            curr = curr.next
            count += 1
        return (reverse(temp_head.next))
        