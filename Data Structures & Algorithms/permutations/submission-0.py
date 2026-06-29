class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(arr, seen):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for x in range(len(nums)):
                if nums[x] not in seen:
                    seen.add(nums[x])
                    arr.append(nums[x])
                    dfs(arr, seen)
                    seen.remove(nums[x])
                    arr.pop()

        dfs([], set())
        return res