class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            flag = False
            for index, word in enumerate(wordDict):
                if s[i:i+len(word)] == word:
                    if dp(i+len(word)):
                        flag = True
                        memo[i] = True


            if i not in memo:
                memo[i] = False

            return memo[i]

        return dp(0)
        
