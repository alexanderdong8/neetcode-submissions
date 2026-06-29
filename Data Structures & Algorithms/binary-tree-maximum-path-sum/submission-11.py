# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            leftval = dfs(node.left)
            rightval = dfs(node.right)
            leftval = max(leftval, 0)
            rightval = max(rightval, 0)
            res[0] = max(res[0], node.val + leftval + rightval)
            return node.val + max(leftval, rightval)
        dfs(root)
        return res[0]