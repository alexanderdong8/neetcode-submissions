class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        res = float('-inf')
        for x in nums:
            curr += x
            res = max(res, curr)

            if curr < 0:
                curr = 0
        
        return res