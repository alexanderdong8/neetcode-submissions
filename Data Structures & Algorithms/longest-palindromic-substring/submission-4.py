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
        print(dp)
        return s[resIndex: resIndex + resLen]


