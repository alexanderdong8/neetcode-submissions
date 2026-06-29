import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect.bisect_right(intervals, newInterval[0], key = lambda x: x[0])
        intervals.insert(index, newInterval)

        curr = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= curr[1]:
                curr[1] = max(end, curr[1])
            else:
                res.append(curr)
                curr = [start, end]

        res.append(curr)
        return res