# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = groupNext, groupPrev.next
            
            while curr != groupNext:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            nextNode = groupPrev.next
            groupPrev.next = kth
            groupPrev = nextNode

        return dummy.next
            


