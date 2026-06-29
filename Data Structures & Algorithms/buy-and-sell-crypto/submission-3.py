class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        left = 0
        right = 1
        maxVal = max(0, prices[right] - prices[left])
        while right < len(prices):
            maxVal = max(maxVal, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
            right += 1
        

        return maxVal
            
            