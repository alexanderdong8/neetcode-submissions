class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        hashset = set()
        left = 0
        largest = 0
        for i, x in enumerate(s):
            while x in hashset:
                hashset.remove(s[left])
                left += 1
            
            largest = max(largest, i-left + 1)
            hashset.add(x)
        
        return largest
