# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, direction, small, big):
            if not node:
                return True

            if direction == "left" and not (small < node.val < big):
                return False

            elif direction == "right" and not (small < node.val < big):
                return False

            leftVal = dfs(node.left, "left", small, node.val)
            rightVal = dfs(node.right, "right", node.val, big)

            return leftVal and rightVal
        return dfs(root, "", float('-inf'), float('inf'))