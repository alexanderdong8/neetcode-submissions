class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(num):
            count = 0
            for val in piles:
                count += math.ceil(val / num)
            return count
        
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
        