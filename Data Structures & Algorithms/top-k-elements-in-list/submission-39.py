class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = [[] for x in range(0, len(nums) + 1)]
        ans = []
        for x in nums:
            hashmap[x] += 1
        print(res, hashmap)
        
        for key, item in hashmap.items():
            res[item].append(key)
        print(res)
        for x in range(len(res)-1, 0, -1):
            for y in res[x]:
                if len(ans) >= k:
                    return ans

                ans.append(y)
        
        return ans


