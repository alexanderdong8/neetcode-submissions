class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        cache = {}
        def dfs(left, right):
            if left > right:
                return 0
            
            if (left, right) in cache:
                return cache[(left, right)]

            player = True if (right-left) % 2 == (len(piles)-1) % 2 else False
            res = None
            if player: # true indicates Alice, False indicates Bob
                res = float('-inf')
                res = max(res, dfs(left+1, right) + piles[left])
                res = max(res, dfs(left, right-1) + piles[right])
            else:
                res = float('inf')
                res = min(res, dfs(left+1, right) - piles[left])
                res = min(res, dfs(left, right-1) - piles[right])

            cache[(left, right)] = res

            return res

        val = dfs(0, len(piles)-1)

        return True if val > 0 else False

            
            