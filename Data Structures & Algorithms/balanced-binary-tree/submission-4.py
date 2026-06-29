# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            if not node:
                return 
            leftH = height(node.left)
            rightH = height(node.right)
            if abs(rightH - leftH) > 1:
                nonlocal res
                res = False
            dfs(node.left)
            dfs(node.right)

        def height(node):
            if not node: return 0

            return max(height(node.left), height(node.right)) + 1

        dfs(root)
        return res