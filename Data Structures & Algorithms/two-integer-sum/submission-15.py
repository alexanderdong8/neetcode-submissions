class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSums = {}

        for index, num in enumerate(nums):
            diff = target - num
            if num in prevSums:
                return [prevSums[num], index]
            prevSums[diff] = index
            