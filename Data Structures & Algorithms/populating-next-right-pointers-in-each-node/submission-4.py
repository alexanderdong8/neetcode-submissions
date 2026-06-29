"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque([root])
        # node = None
        while queue:
            length = len(queue)
            for x in range(length):
                node = queue.popleft()
                if x == length - 1:
                    node.next = None
                else:
                    nextNode = queue[0]
                    node.next = nextNode

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
        return root