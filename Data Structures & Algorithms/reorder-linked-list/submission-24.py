# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (not head or not head.next):
            return

        slow = head
        fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        reverse = slow.next
        slow.next = None
        prev = None
        while (reverse):
            reverseNext = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = reverseNext
        

        curr1 = head
        curr2 = prev

        while (curr2):
            curr1Next = curr1.next
            curr1.next = curr2
            curr1 = curr1Next

            curr2Next = curr2.next
            curr2.next = curr1
            curr2 = curr2Next
        