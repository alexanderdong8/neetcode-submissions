class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[right] == nums[mid]:
                return True
            
            # 3 4 4 5 6 1 2 2 
            target = 1
            if nums[left] < nums[mid]:
                if target < nums[left]:
                    left = mid + 1
                else:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        mid = right - 1

            else:
                if target > nums[right]:
                    mid = right - 1
                else:
                    if target > nums[mid]:
                        mid = left + 1

                    elif target < nums[mid]:
                        mid = right - 1

        return False
