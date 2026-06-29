class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for x in nums:
            hashset.add(x)

        biggest = 0
        seen = set()
        for x in nums:
            if x in seen:
                continue

            size = 0
            if x - 1 not in hashset:
                size += 1
                curr = x
                while True:
                    print(curr, size)
                    if curr + 1 in hashset:
                        seen.add(curr)
                        size += 1
                        curr += 1
                    else:
                        break
                        

            biggest = max(biggest, size)
            size = 0
        return biggest
        