from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = Counter(nums)

        numsCount = [(count, val) for val, count in numsCount.items()]
        numsCount.sort(key=lambda x: -x[0])
        res = []
        for x in range(k):
            res.append(numsCount[x][1])
        return res