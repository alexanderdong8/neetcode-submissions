"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        real_to_copy = {None : None}

        curr = head

        while (curr):
            real_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while (curr):
            random = curr.random
            nextt = curr.next
            randomNodeCopy = real_to_copy[random]
            nextNode = real_to_copy[nextt]
            
            
            copy = real_to_copy[curr]
            copy.next = nextNode
            copy.random = randomNodeCopy
            curr = curr.next
        
        return real_to_copy[head]

            