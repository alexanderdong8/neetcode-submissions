class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchHelp(nums, target, left, right):

            if (left == right):
                return -1
            mid = (left + right) // 2
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                return searchHelp(nums, target, left, mid)
            else:
                return searchHelp(nums, target, mid + 1, right)

        return searchHelp(nums, target, 0, len(nums))
            

        