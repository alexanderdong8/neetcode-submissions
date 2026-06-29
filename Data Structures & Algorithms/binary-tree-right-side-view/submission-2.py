# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([(root, 0)])
        prevNode = None
        while queue:
            node, depth = queue.popleft()
            if prevNode and depth > prevNode[1]:
                res.append(prevNode[0].val)

            prevNode = (node, depth)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        res.append(node.val)
        return res