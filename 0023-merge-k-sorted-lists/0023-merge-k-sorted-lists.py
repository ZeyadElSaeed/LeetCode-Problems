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
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range( 0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append( MergeTwoLists(l1, l2) )
            lists = merged_lists
        return lists[0]
        