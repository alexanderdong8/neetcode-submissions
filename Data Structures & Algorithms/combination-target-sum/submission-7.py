class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subsum = []
        def dfs(i, total):
            if i >= len(nums) or total >= target:
                if total == target:
                    res.append(tuple(subsum.copy()))
                return


            subsum.append(nums[i])
            dfs(i, total + nums[i])

            subsum.pop()
            subsum.append(nums[i])
            dfs(i+1, total + nums[i])

            subsum.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return [list(t) for t in set(res)]
