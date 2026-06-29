import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatBananas(num):
            bites = 0
            for bananas in piles:
                bites += math.ceil(bananas / num)
            return bites

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            biteNum = eatBananas(mid)
            if biteNum <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
