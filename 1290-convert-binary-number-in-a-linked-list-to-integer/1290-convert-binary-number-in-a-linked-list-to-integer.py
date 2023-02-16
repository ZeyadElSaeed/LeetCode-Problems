# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = -1
        answer = 0
        cur = head
        # count the number of binary char 0-indexed
        while cur:
            n += 1
            cur = cur.next
        # calculate the binary using n and each node's value
        while head:
            answer += (2**n)*head.val
            head = head.next
            n -= 1
        return answer