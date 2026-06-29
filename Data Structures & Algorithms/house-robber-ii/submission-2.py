class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(arr):
            dp = []
            first, second = 0, 0
            for x in arr:
                dp.append(max(first + x, second))
                first = second
                second = dp[-1]
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]

        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))