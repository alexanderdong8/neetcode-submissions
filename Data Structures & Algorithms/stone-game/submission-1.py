from collections import defaultdict
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = defaultdict(int)
        #true is Alice false is bob
        def dfs(turn, player, arr):
            if not arr:
                return 0
            
            if (turn, player) in cache:
                return cache[(turn, player)]

            cache[(turn, player)] = max(cache[(turn, player)], dfs(turn+1, not player, arr[1:]) + arr[0])
            cache[(turn, player)] = max(cache[(turn, player)], dfs(turn+1, not player, arr[:-1]) + arr[-1])
            return cache[(turn, player)]
        dfs(0, True, piles)
        return True if cache[(0, True)] > cache[(1, False)] else False