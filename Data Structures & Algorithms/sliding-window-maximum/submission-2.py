
from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = nums[:k]
        sl = SortedList(arr)
        res = []
        left = 0
        res.append(sl[-1])
        for x in range(k, len(nums)):
            sl.add(nums[x])
            sl.remove(nums[left])
            res.append(sl[-1])
            left += 1
        return res