class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= curr[1]:
                curr[1] = max(curr[1], end)
            else:
                res.append(curr)
                curr = [start, end]
        res.append(curr)
        return res