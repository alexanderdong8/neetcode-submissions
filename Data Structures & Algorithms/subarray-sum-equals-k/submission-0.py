class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        #prefix sum - k exists in seen then we know that some prefix sum + k will equal to the current prefix which means that k exists
        #obviously if i encounter k itself then i add one too

        seen = defaultdict(int)
        res = 0
        for num in prefix:

            if num - k in seen:
                res += (seen[num-k])
            seen[num] += 1

        return res

        '''
        [1, -1, 0]
        [1, 0, 0]
        1:1, (1:1, 0:1), (1:1, 0:2) 

        [0, 1, 2, 3]
        '''

