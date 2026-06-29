class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        var = set()
        for x in nums:
            var.add(x)
        
        return not (len(nums) == len(var))
         