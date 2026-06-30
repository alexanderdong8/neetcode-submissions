class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        counts = Counter(candidates)
        countsArr = [[key, value] for key, value in counts.items()]
        def dfs(arr, total, index):
            if total > target or index >= len(countsArr):
                return
            if total == target:
                res.append(arr.copy())
                return
            dfs(arr, total, index+1)

            if countsArr[index][1] > 0:
                arr.append(countsArr[index][0])
                countsArr[index][1] -= 1
                dfs(arr, total + countsArr[index][0], index)
                arr.pop()
                countsArr[index][1] += 1

        dfs([], 0, 0)
        return res
        #     if index >= len(candidates) or total >= target:
        #         if total == target:
        #             res.add(tuple(arr))
        #         return
        #     arr.append(candidates[index])
        #     dfs(index+1, arr, total + candidates[index])
        #     arr.pop()
        #     dfs(index+1, arr, total)

        # dfs(0, [], 0)
        # return [list(combo) for combo in res]