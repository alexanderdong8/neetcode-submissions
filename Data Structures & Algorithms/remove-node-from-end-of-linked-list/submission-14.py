# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while (curr):
            length += 1
            curr = curr.next
        if length == 1:
            return None
        target = length - n
        curr2 = head
        count = 0
        prev = None
        while True:
            print(length, count, target)
            if count == target:
                if count == 0:
                    return curr2.next       
                prev.next = curr2.next
                break
            prev = curr2
            curr2 = curr2.next
            count += 1
        
        return head