# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            print("ran")
            left = [0,0]
            right = [0,0]
            if not node.left and not node.right:
                print("ran if statement")
                self.res = max(self.res, node.val)
                return [node.val, node.val]
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)


            split_val = node.val + left[1] + right[1]
            straight_path = max(node.val + max(left[1], right[1]), node.val)

            self.res = max(self.res, split_val, straight_path, node.val)
            return [split_val, straight_path]

        dfs(root)
        return self.res