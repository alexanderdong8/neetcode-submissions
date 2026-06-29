class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(num):
            count = 0
            for x in piles:
                count += math.ceil(x/num)
            return count <= h
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (right + left) // 2
            if canFinish(mid):
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
            
        return res
            
