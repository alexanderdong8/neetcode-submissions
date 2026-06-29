# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        if not lists[0] or len(lists) == 1:
            return lists[0]

        dummy = ListNode()
        curr = dummy
        left, right = lists[0], lists[1]

        while left and right:
            if left.val <= right.val:
                curr.next = ListNode(left.val)
                curr = curr.next
                left = left.next
            else:
                curr.next = ListNode(right.val)
                curr = curr.next
                right = right.next
        
        if left:
            curr.next = left
            # curr.next = ListNode(left.val)
            # curr = curr.next
            # left = left.next
        if right:
            curr.next = right
            # curr.next = ListNode(right.val)
            # curr = curr.next
            # right = right.next



        for x in range(2, len(lists)):
            count = dummy.next
            while count:
                print(count.val)
                count = count.next
            print("-")
            dummyClone = dummy
            curr = dummy.next
            right = lists[x]
            prev = None
            while curr and right:
                if curr.val <= right.val:
                    prev = curr
                    curr = curr.next
                else:
                    if not prev:
                        print(right.val, "-", curr.val)
                        dummyClone.next = ListNode(right.val)
                        dummyClone.next.next = curr
                        prev = dummyClone.next
                    else:
                        prev.next = ListNode(right.val)
                        prev.next.next = curr
                    
                    right = right.next
        
            if right:
                print("nextpart")
                print(right.val, prev.val)
                prev.next = right
                # curr.next = ListNode(right.val)
                # curr = curr.next
                # right = right.next
        
        return dummy.next
