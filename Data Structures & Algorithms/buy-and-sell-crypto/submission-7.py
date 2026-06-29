class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        maxVal = 0
        while right < len(prices):
            
            if prices[left] < prices[right]:
                maxVal = max(maxVal, prices[right] - prices[left])
            
            else:
                left = right
            right += 1
        

        return maxVal
            
            