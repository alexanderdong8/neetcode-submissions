class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        res = []
        for x in range(len(nums)-1, -1, -1):
            if nums[x] not in seen:
                seen.add(nums[x])
            else:
                nums.remove(nums[x])

        return len(nums)