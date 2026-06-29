class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for x in range(0, len(nums)):
            map1[nums[x]] = x
        
        for x in range(0, len(nums)):
            difference = target - nums[x]
            if difference in map1 and map1[difference] != x:
                return [x, map1[difference]]
        

            