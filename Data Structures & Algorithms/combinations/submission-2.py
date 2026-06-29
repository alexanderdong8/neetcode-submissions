class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(arr, i):
            if len(arr) == k:
                res.append(arr.copy())
                return


            for x in range(i, n+1):
                arr.append(x)
                dfs(arr, x+1)
                arr.pop()
            
        dfs([], 1)
        return res