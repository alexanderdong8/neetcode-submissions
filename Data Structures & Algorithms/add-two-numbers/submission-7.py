# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        carry = 0
        head = ListNode()
        curr = head
        while l1 and l2:
            newVal = l1.val + l2.val + carry
            carry = newVal // 10
            newVal = newVal % 10
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            newVal = l1.val + carry
            carry = newVal // 10
            newVal = newVal % 10
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next

        while l2:
            newVal = l2.val + carry
            carry = newVal // 10
            newVal = newVal % 10
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = curr.next
            l2 = l2.next
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
        return head.next