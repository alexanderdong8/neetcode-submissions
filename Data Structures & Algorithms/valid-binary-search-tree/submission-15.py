# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, small, big):
            if not node:
                return True

            if not (small < node.val < big):
                return False

            leftVal = dfs(node.left, small, node.val)
            rightVal = dfs(node.right, node.val, big)

            return leftVal and rightVal
        return dfs(root, float('-inf'), float('inf'))