# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) != 1:
            newList = []

            for x in range(0, len(lists), 2):
                l1 = lists[x]
                l2 = lists[x + 1] if (x + 1) < len(lists) else None
                newList.append(self.mergeLists(l1, l2))
            lists = newList
        return lists[0]


    def mergeLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if (l1.val <= l2.val):
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next
            
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next