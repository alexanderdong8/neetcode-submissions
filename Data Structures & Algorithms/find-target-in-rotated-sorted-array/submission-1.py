class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            
            #left side needs to check if the right has the values
            if nums[mid] == target:
                return mid
        
            if nums[mid] >= nums[left]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
                
            else:

                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            #right side needs to chek if the left side ahs the values
            


        
        return -1