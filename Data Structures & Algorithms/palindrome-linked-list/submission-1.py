# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        stack1 = []
        stack2 = []
        curr = head
        while curr:
            stack1.append(curr.val)
            stack2.append(curr.val)
            curr = curr.next

        while stack1:
            arr.append(stack1.pop())

        return arr == stack2