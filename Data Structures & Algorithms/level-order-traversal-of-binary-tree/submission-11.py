# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        ans = []
        while queue:
            node, depth = queue.popleft()
            if len(ans) < depth + 1 and node:
                ans.append([])
            if node:
                ans[depth].append(node.val)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))


        return ans