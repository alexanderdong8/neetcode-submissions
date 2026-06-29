class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIndex = 0
        n = len(s)
        dp = [[False] * n for i in range(n)]
        for x in range(n):
            for y in range(x, -1, -1):
                if s[x] == s[y] and (x-y <= 2 or dp[x-1][y+1]):
                    dp[x][y] = True
                    if x - y + 1 > resLen:
                        resLen = x-y+1
                        resIndex = y
        return s[resIndex: resIndex + resLen]


        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        resIndex = i
        
        return s[resIndex: resIndex + resLen]