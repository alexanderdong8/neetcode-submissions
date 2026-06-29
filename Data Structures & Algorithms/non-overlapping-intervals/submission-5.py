class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = []
        count = 0
        for x in intervals:
            if res and x[0] < res[-1][1]:
                if x[1] < res[-1][1]:
                    res[-1] = x
                count += 1
                continue
            res.append(x)
        print(res)
        return count