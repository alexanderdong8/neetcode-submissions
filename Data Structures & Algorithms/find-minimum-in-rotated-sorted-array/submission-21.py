class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[left]
        while left <= right:
            mid = (left + right) // 2

            if nums[left] < nums[right]:
                res = min(res, nums[left])
                return res
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid - 1

        return res
