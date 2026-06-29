class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        count = 0
        for x in nums:
            if x == 0:
                count += 1
                continue
            total *= x

        if count > 1:
            return [0] * len(nums)

        result = []
        for x in nums:
            if x == 0:
                result.append(total)
            elif count == 1:
                result.append(0)
            else:
                result.append(total // x)

        return result


            


        