class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        create a dp array that keeps track of the size of the sqaures. In or
        '''
        dp = [[0] * (len(matrix[0]) + 1) for x in range(len(matrix)+1)]
        res = 0
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if matrix[row-1][col-1] == "1":
                    print(row, col)
                    # if dp[row-1][col] == dp[row][col-1] == dp[row-1][col-1]:
                    dp[row][col] = int(min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])) + 1
                    res = max(dp[row][col], res)

        print(dp)
        return res * res