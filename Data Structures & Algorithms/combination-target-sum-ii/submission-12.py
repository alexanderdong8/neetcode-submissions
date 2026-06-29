class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        visited = []
        def dfs(total, seen, arr):
            if total >= target:
                if total == target and set(arr) not in visited:
                    res.append(arr.copy())
                    visited.append(set(arr))
                return

            for index, val in enumerate(candidates):
                if index not in seen:
                    total += val
                    seen.add(index)
                    arr.append(val)
                    dfs(total, seen, arr)
                    total -= val
                    seen.remove(index)
                    arr.remove(val)
            
        dfs(0, set(), [])
        return res