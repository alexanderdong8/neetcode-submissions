class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = defaultdict(int)

        def dfs(index, hold):

            if index == len(prices):
                return 0
            if (index, hold) in cache:
                return cache[(index, hold)]
            cache[(index, hold)] = max(cache[(index, hold)], dfs(index+1, hold))
            if hold:
                cache[(index, hold)] = max(cache[(index, hold)], dfs(index+1, not hold) + prices[index])
            else:
                cache[(index, hold)] = max(cache[(index, hold)], dfs(index+1, not hold) - prices[index])

            return cache[(index, hold)]

        return dfs(0, False)
        '''
        skip day
        if hold I can skip or sell
        if not hold I can skip or buy
        '''