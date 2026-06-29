# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            leftH = dfs(node.left)
            rightH = dfs(node.right)

            if not leftH[0] or not rightH[0] or abs(rightH[1] - leftH[1]) > 1:
                return [False, 0]

            return [True, max(leftH[1], rightH[1]) + 1]
        return dfs(root)[0]

