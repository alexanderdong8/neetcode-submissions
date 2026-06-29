import collections
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        cache = collections.defaultdict(int)
        def dfs(total):
            # nonlocal res
            if total >= target:
                if total == target:
                    return 1
                else:
                    return 0
            if total in cache:
                return cache[total]
            for x in range(len(nums)):
                cache[total] += dfs(total + nums[x])
            
            return cache[total]
            # dfs(index+1, total, arr)
            # arr.append(nums[index])
            # dfs(index, total + nums[index], arr)
            # arr.pop()

        return dfs(0)
