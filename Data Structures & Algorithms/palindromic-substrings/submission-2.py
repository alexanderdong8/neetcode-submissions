class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for x in range(n)]
        for x in range(n):
            for y in range(x, -1, -1):
                if s[x] == s[y] and (x-y <= 2 or dp[x-1][y+1]):
                    dp[x][y] = True
        
        res = 0
        for x in range(n):
            for y in range(n):
                if dp[x][y] == True:
                    res += 1
        return res