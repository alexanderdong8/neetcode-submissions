import collections
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False

        target = target // 2

        cache = collections.defaultdict(lambda: False)

        def dfs(index, total):
            if total >= target or index >= len(nums):
                if total == target:
                    return True
                return False
            if (index, total) in cache:
                return cache[(index, total)]

            cache[(index, total)] |= dfs(index+1, total)
            cache[(index, total)] |= dfs(index+1, total + nums[index])

            return cache[(index, total)]

        return dfs(0,0)
