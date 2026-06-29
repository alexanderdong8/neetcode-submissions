class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set()
        seen = set()
        length = 0
        biggest = 0
        for x in nums:
            hashmap.add(x)
        for x in nums:
            if x in seen:
                continue
            if x-1 not in hashmap:
                length += 1
                seen.add(x)
                value = x
                while True:
                    if value + 1 in hashmap:
                        seen.add(value)
                        length += 1
                        value += 1
                    else:
                        break
                
                biggest = max(biggest, length)
                length = 0
            
            
        return biggest

                    

                    
