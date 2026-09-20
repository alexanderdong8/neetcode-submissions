import collections
class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = collections.defaultdict(lambda: False)

        def dfs(index, leftop):
            
            if index >= len(s):
                print("ran")
                return True if leftop == 0 else False
            
            if (index, leftop) in cache:
                return cache[(index, leftop)]

            if s[index] == "(":
                leftop += 1
                cache[(index, leftop-1)] |= dfs(index+1, leftop)
                leftop -= 1 #might not need this actually

            elif s[index] == ")":
                if leftop > 0:
                    leftop -= 1
                    cache[(index, leftop+1)] |= dfs(index+1, leftop)
                    leftop += 1 #do i need this?
                else:
                    cache[(index, leftop)] |= False
            else:
                leftop += 1
                cache[(index, leftop-1)] |= dfs(index+1, leftop)
                leftop -= 1

                if leftop > 0:
                    leftop -= 1
                    cache[(index, leftop+1)] |= dfs(index+1, leftop)
                    leftop += 1
                else:
                    cache[(index, leftop)] |= False

                cache[(index, leftop)] |= dfs(index+1, leftop)

            return cache[(index, leftop)]

        return dfs(0, 0)
