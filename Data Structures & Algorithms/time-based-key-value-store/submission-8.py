from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.times[key]
        if not values:
            return ""
        left = 0
        right = len(values) - 1
        res = [values[0], 0]
        while left <= right:
            mid = (left + right) // 2

            if (values[mid][1] == timestamp):
                if (mid > res[1]):
                    res = [values[mid], mid]

            if values[mid][1] > timestamp:
                right = mid - 1
                if (min(timestamp - values[mid][1], timestamp - res[0][1]) == (timestamp - values[mid][1])) and mid > res[1] and (timestamp - values[mid][1]) > 0:
                    res = [values[mid], mid]
            
            else:
                left = mid + 1
                if (min(timestamp - values[mid][1], timestamp - res[0][1]) == (timestamp - values[mid][1])) and mid > res[1] and (timestamp - values[mid][1]) > 0:
                    res = [values[mid], mid]
        
        if (res[0][1] <= timestamp):
            return res[0][0]
        else:
            return ""



