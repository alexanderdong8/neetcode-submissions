class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        
        def dfs(index, arr, total):
            if index >= len(candidates) or total >= target:
                if total == target:
                    res.add(tuple(arr))
                return
            arr.append(candidates[index])
            dfs(index+1, arr, total + candidates[index])
            arr.pop()
            dfs(index+1, arr, total)

        dfs(0, [], 0)
        return [list(combo) for combo in res]