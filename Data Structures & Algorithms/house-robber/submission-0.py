class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        dp = []
        for n in nums:
            dp.append(max(n + first, second))
            first = second
            second = dp[-1]
        return dp[-1]