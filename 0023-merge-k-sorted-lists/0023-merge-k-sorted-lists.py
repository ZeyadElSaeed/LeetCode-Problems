# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def MergeTwoLists(list1, list2):
            head = ListNode()
            pt = head
            while list1 and list2:
                if list1.val < list2.val:
                    pt.next = list1
                    list1 = list1.next
                else:
                    pt.next = list2
                    list2 = list2.next
                pt = pt.next
            if list1:
                pt.next = list1
            elif list2:
                pt.next = list2
            return head.next
        
        answer = None
        for head in lists:
            answer = MergeTwoLists(answer , head)
        return answer
        