class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        def dfs(steps):
            if steps >= n:
                if steps == n:
                    res[0] += 1
                return
            
            dfs(steps+1)
            dfs(steps+2)
        
        dfs(0)

        return res[0]

