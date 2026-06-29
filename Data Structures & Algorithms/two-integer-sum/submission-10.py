class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for x in range(0, len(nums)):
            print(x)
            hashmap[nums[x]] = x

        for x in range(0, len(nums)):
            difference = target - nums[x]

            if difference in hashmap and x != hashmap[difference]:
                return [x, hashmap[difference]]

        return 0 
            