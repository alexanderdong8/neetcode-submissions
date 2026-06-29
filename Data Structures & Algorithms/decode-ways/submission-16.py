from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        cache = defaultdict(int)

        def dfs(newS):
            if not newS:
                return 1
            
            if newS and newS[0] == "0":
                return 0

            if newS in cache:
                return cache[newS]

            for x in range(1, len(newS)+1):
                if 1 <= int(newS[:x]) <= 26:
                    print(int(newS[:x]))
                    cache[newS] += dfs(newS[x:])
                else:
                    break
            
            return cache[newS]
            

        return dfs(s)
