class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)
        if goal % 2 == 1:
            return False
        goal = goal // 2
        memo = {}
        def dp(i, total):
            if i not in memo:
                memo[i] = {}

            if total == goal:
                return True
            if total > goal:
                return False
            if i >= len(nums):
                return False
            if memo[i].get(total, -1) != -1:
                return memo[i][total]

            memo[i][total] = dp(i+1, total) or dp(i+1, total + nums[i])

            return memo[i][total]
        return dp(0,0)





