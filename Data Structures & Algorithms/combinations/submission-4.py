class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def dfs(arr, index):
            if len(arr) == k:
                res.append(arr.copy())
                return 

            if index > n:
                return 
            for x in range(index, n+1):
                arr.append(x)
                dfs(arr, x+1)
                arr.pop()
            
            # dfs(arr, index+1)
            # arr.append(index)
            # dfs(arr, index+1)
            # arr.pop()

        dfs([], 1)
        return res