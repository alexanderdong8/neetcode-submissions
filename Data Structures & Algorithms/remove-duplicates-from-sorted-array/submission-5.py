class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        change, main = 0, 0

        while main < len(nums):
            nums[change] = nums[main]
            while main + 1 < len(nums) and nums[main+1] == nums[main]:
                main += 1
            change += 1
            main += 1
        return change