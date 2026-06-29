class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def dfs(arr, index):
            if len(arr) == k:
                res.append(arr.copy())
                return 

            if index > n:
                return 

            dfs(arr, index+1)
            arr.append(index)
            dfs(arr, index+1)
            arr.pop()

        dfs([], 1)
        return res