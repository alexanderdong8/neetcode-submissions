# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        res = [0]

        def dfs(node):
            if p.val <= node.val <= q.val:
                if p.val == node.val:
                    res[0] = p
                elif q.val == node.val:
                    res[0] = q
                else:
                    res[0] = node
                return
            if node.val > q.val:
                dfs(node.left)
            elif node.val < p.val:
                dfs(node.right)
        dfs(root)
        return res[0]