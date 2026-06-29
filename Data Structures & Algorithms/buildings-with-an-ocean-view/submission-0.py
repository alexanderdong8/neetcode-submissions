class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        dp = [[False, 0] for x in range(len(heights))]
        dp[len(heights)-1][0] = True

        for x in range(len(heights)-2, -1, -1):
            if not dp[x+1][0]:
                if heights[x] > dp[x+1][1]:
                    dp[x][0] = True
                else:
                    dp[x][1] = dp[x+1][1]
            else:
                if (heights[x] > heights[x+1]):
                    dp[x][0] = True
                else:
                    dp[x][1] = heights[x+1]

        for x in range(len(dp)):
            if dp[x][0]:
                res.append(x)
        return res