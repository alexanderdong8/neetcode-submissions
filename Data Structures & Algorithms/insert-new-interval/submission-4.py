class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for x in range(len(intervals)):
            if newInterval[1] < intervals[x][0]:
                res.append(newInterval)
                res += intervals[x:]
                return res
            elif newInterval[0] > intervals[x][1]:
                res.append(intervals[x])
            else:
                newInterval = [min(newInterval[0], intervals[x][0]), max(newInterval[1], intervals[x][1])]
            
        res.append(newInterval)
        return res
            