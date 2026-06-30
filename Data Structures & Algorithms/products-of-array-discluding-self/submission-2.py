class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                continue
            product *= num

        
        if count > 1:
            return [0] * len(nums)

        res = []

        for num in nums:
            if count > 0 and num == 0:
                res.append(product)
            elif count > 0:
                res.append(0)
            elif count == 0:
                res.append(product // num)
        return res