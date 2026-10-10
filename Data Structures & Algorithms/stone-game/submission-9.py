class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        cache = {}
        def dfs(player, left, right):
            if left > right:
                return 0
            if (player, left, right) in cache:
                return cache[(player, left, right)]
            res = None
            if player: # true indicates Alice, False indicates Bob
                res = float('-inf')
                res = max(res, dfs(not player, left+1, right) + piles[left])
                res = max(res, dfs(not player, left, right-1) + piles[right])
            else:
                res = float('inf')
                res = min(res, dfs(not player, left+1, right) - piles[left])
                res = min(res, dfs(not player, left, right-1) - piles[right])

            cache[(player, left, right)] = res

            return res

        val = dfs(True, 0, len(piles)-1)

        return True if val > 0 else False

            
            