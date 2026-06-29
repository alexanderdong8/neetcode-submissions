class Solution:
    def longestPalindrome(self, s: str) -> str:
        # resLen = 0
        # resIndex = 0
        # n = len(s)
        # dp = [[False] * n for i in range(n)]
        # for x in range(n):
        #     for y in range(x, -1, -1):
        #         if s[x] == s[y] and (x-y <= 2 or dp[x-1][y+1]):
        #             dp[x][y] = True
        #             if x - y + 1 > resLen:
        #                 resLen = x-y+1
        #                 resIndex = y
        # print(dp)
        # # return s[resIndex: resIndex + resLen]
        resLen = 1
        resIndex = 0
        for x in range(len(s)):
            left = x
            right = x
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right-left + 1 > resLen:
                        resLen = right-left+1
                        resIndex = left
                else:
                    break

                left -= 1
                right += 1

            left = x
            right = x+1

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right-left + 1 > resLen:
                        resLen = right-left+1
                        resIndex = left
                else:
                    break

                left -= 1
                right += 1

        return s[resIndex: resIndex+resLen]
            


