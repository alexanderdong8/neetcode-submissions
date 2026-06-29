class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right-left) // 2)
            halfSize = mid
            if (mid-1 < 0 or nums[mid-1] != nums[mid]) and (mid+1 >= len(nums) or nums[mid+1] != nums[mid]):
                return nums[mid]

            if halfSize % 2 == 0:
                if mid - 1 >= 0 and nums[mid-1] == nums[mid]:
                    right = mid-1
                
                elif mid + 1 < len(nums) and nums[mid+1] == nums[mid]:
                    left = mid+1
            else:
                if mid - 1 >= 0 and nums[mid-1] != nums[mid]:
                    right = mid-1
                elif mid + 1 < len(nums) and nums[mid+1] != nums[mid]:
                    left = mid+1

        


            