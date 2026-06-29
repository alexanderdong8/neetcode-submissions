class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def findMax(hashmap):
            maximum = 0
            for x in hashmap.values():
                maximum = max(maximum, x)
            
            return maximum

        left = 0
        hashmap = {}
        maximum = 0
        for index, char in enumerate(s):
            hashmap[char] = hashmap.get(char, 0) + 1
            mostChar = findMax(hashmap)
            length = index - left + 1
            

            while (length - mostChar > k) :
                hashmap[s[left]] -= 1
                mostChar = findMax(hashmap)
                left += 1
                length = index - left + 1
            maximum = max(maximum, length)
        
        return maximum
            