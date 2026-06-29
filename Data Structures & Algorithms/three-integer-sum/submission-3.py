class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for index, x in enumerate(nums):
            if index == 0 or x != nums[index-1]:
                left = index + 1
                right = len(nums) - 1
                target = -1 * x
                while left < right:
                    if nums[left] + nums[right] < target:
                        left+= 1
                    elif nums[left] + nums[right] > target:
                        right-=1
                    else:
                        res.append([nums[index], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate elements for `right`
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res


        