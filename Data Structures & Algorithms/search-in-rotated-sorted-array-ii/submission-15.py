class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            
            mid = (left + right) // 2
            print(mid, nums[mid])
            if nums[mid] == target:
                print(nums[mid], target, "check")
                return True

            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            
            # 3 4 4 5 6 1 2 2 
            # 4 4 5 6 1 2 2 3
            if nums[left] < nums[mid]:
                if target < nums[left]:
                    left = mid + 1
                else:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        right = mid - 1

            else:
                if target > nums[right]:
                    right = mid - 1
                else:
                    if target > nums[mid]:
                        left = mid + 1

                    elif target < nums[mid]:
                        right = mid - 1

        return False
