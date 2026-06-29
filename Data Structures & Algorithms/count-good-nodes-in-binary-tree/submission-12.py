# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(prevMax, node):
            nonlocal ans
            if not node:
                return 
            
            if node.val >= prevMax:
                print(node.val, prevMax)
                ans += 1
                prevMax = node.val

            
            dfs(prevMax, node.left)
            dfs(prevMax, node.right)

        dfs(float('-inf'), root)
        return ans
