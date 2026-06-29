# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        dummy = ListNode(0, None)
        res = dummy
        while (curr1 and curr2):

            if curr1.val <= curr2.val:
                dummy.next = curr1
                dummy = dummy.next
                curr1 = curr1.next

            else:
                dummy.next = curr2
                dummy = dummy.next
                curr2 = curr2.next
        
        if (curr1):
            dummy.next = curr1
            return res.next
        else:
            dummy.next = curr2
            return res.next
