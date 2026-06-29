"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sweep = defaultdict(int)
        for interval in intervals:
            sweep[interval.start] += 1
            sweep[interval.end] -= 1

        sweep = sorted(sweep.items())
        active = 0
        res = 0
        for x in range(len(sweep)):
            index, num = sweep[x][0], sweep[x][1]

            active += num
            res = max(res, active)
        return res