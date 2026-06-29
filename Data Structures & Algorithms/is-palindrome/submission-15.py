class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def isletter(s):
            return ord("a") <= ord(s) <= ord("z") or ord("0") <= ord(s) <= ord("9")
        
        right = len(s) - 1
        left = 0
        while left < right:
            while left < right and (not isletter(s[left:left+1])):
                left += 1
            while left < right and (not isletter(s[right:right+1])):
                right -= 1
            
            if s[left:left+1] != s[right:right+1]:
                return False
            
            left += 1;
            right -= 1;
        
        return True