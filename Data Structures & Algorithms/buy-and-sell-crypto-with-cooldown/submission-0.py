class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dfs(index, own):

            if index >= len(prices):
                return 0

            if (index, own) in cache:
                return cache[(index, own)]
                
            res = 0
            if own:
                res = max(res, dfs(index+2, not own) + prices[index])

            res = max(res, dfs(index+1, own))
            if not own:
                res = max(res, dfs(index+1, not own) - prices[index])

            cache[(index, own)] = res

            return res

        return dfs(0, False)

        
