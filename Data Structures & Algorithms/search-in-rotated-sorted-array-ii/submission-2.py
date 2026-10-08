class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[mid] < nums[left]:
                    left = mid + 1
                else:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        mid = right - 1

            else:
                if nums[mid] > nums[right]:
                    mid = right - 1
                else:
                    if target > nums[mid]:
                        mid = left + 1

                    elif target < nums[mid]:
                        mid = right - 1

        return False
