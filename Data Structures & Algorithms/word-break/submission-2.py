class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # dp = [False] * (n+1)
        # dp[n] = True
        # wordSet = set(wordDict)
        # for x in range(n-1, -1, -1):
        #     dp[x] = dp[x+]

        n = len(s)
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == n:
                return True
            
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    if dp(i+len(word)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        return dp(0)