class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for x in range(len(obstacleGrid)+1)]
        for row in range(len(dp)):
            dp[row][len(dp[0])-1] = 1

        for col in range(len(dp[0])):
            dp[len(dp)-1][col] = 1


        for row in range(len(obstacleGrid)-1, -1, -1):
            for col in range(len(obstacleGrid[0])-1, -1, -1):
                dp[row][col] = 0 if obstacleGrid[row][col] else dp[row+1][col] + dp[row][col+1]
        [2, 1, 1, 1]
        [1, 0, 0, 1]
        [1, 0, 0, 1]
        [1, 1, 1, 1]
        
        print(dp)
        return dp[0][0]