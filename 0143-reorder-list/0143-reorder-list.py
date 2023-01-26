# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle Node
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #reverse the second half
        current = slow.next
        previous = slow.next = None
        
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        
        #Merge the two halfs
        first, second = head, previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
            