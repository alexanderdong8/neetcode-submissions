class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for x in intervals:

            if res and x[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], x[1])]
            else:
                res.append(x)
        return res
