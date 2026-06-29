import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #1, 2, 3, 4 bisect right will always go to after the equal one so greater always
        start = bisect.bisect_right(arr, x)
        left, right = start - 1, start # start could be over the arr
        res = deque()
        
        while len(res) < k:
            if left >= 0:
                leftDiff = abs(x - arr[left])
            else:
                leftDiff = float('inf')
            if right < len(arr):
                rightDiff = abs(x - arr[right])
            else:
                rightDiff = float('inf')

            if leftDiff <= rightDiff:
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        return list(res)

