# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p = collections.deque([p])
        q = collections.deque([q])

        while p and q:
            for _ in range(len(p)):
                pNode = p.popleft()
                qNode = q.popleft()
                
                if not pNode and not qNode:
                    continue
                if not pNode or not qNode or pNode.val != qNode.val:
                    return False
                
                q.append(pNode.left)
                q.append(pNode.right)
                p.append(qNode.left)
                p.append(qNode.right)

        return True

        


            
