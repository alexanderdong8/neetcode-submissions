class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k
        nums_new = nums.copy()
        for x in range(len(nums_new)):
            new_pos = (x + k) % len(nums)
            nums_new[x] = nums[new_pos]
        print(nums_new)
        for x in range(len(nums)):
            nums[x] = nums_new[x]