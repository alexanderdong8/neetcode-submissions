# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if sameSubtree(node, subRoot):
                nonlocal res
                res = True


        def sameSubtree(node, subNode):
            if not node and not subNode:
                return True
            if not node or not subNode or node.val != subNode.val:
                return False
            
            left = sameSubtree(node.left, subNode.left)
            right = sameSubtree(node.right, subNode.right)

            return left and right

        dfs(root)
        return res