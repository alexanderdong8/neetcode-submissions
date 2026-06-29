class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in range(0, len(nums)):
            newNum = abs(nums[x]) - 1
                
            if nums[newNum] < 0:
                return abs(nums[x])
            else:
                nums[newNum] *= -1
        return -1
                