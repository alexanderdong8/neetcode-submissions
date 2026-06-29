class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for x in range(1, len(nums)):
            num = nums[x]
            if parity == num % 2:
                return False
            else:
                parity = num % 2

        return True