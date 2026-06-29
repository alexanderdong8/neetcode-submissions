class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        count = 0
        maximum = 0
        for x in nums:
            if x - 1 not in hashset:
                num = x
                while (num in hashset):
                    count += 1
                    num += 1
                maximum = max(maximum, count)
                count = 0
        
        return maximum

