class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int)
        def dfs(total):
            if total >= target:
                if total == target:
                    print("success")
                    return 1
                return 0
            if total in cache:
                return cache[total]

            for x in range(len(nums)):
                cache[total] += dfs(total + nums[x])

            return cache[total]

        return dfs(0)