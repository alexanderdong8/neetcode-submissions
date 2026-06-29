import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        maxVal = float('-inf')
        for num in nums:
            counts[num] += 1
            maxVal = max(maxVal, counts[num])
        
        buckets = [[] for x in range(maxVal+1)]

        for num, count in counts.items():
            buckets[count].append(num)
        res = []
        for x in range(len(buckets)-1, -1, -1):
            for num in buckets[x]:
                if len(res) == k:
                    break
                res.append(num)
        return res
            
            