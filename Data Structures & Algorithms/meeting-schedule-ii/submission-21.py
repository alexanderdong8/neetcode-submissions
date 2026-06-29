"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        res, count = 0, 0
        startP, endP = 0, 0

        while startP < len(intervals):
            if start[startP] < end[endP]:
                count += 1
                startP += 1
            else:
                count -= 1
                endP += 1
            
            res = max(res, count)
        return res