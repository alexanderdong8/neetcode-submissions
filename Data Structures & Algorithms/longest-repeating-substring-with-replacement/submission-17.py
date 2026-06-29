class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def largestVal(hashmap):
            res = 0
            for key, val in hashmap.items():
                res = max(res, val)
            return res
        
        left, right = 0, 0
        occurences = collections.defaultdict(int)
        res = 0
        while right < len(s):
            occurences[s[right]] += 1
            while (right - left + 1) - largestVal(occurences) > k:
                print(left, right, occurences, largestVal(occurences))
                occurences[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

