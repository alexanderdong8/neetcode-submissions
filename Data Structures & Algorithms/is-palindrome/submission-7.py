class Solution:
    def isPalindrome(self, s: str) -> bool:
        def lon(s):
            return (ord("a") <= ord(s) <= ord("z") or ord("0") <= ord(s) <= ord("9"))

            
        s = s.lower().replace(" ", "")
        left = 0
        right = len(s) - 1
        
        print(s)
        while left < right:
            if lon(s[left:left+1]) == False:
                print(s[left:left+1])
                left += 1
                continue
            if lon(s[right:right+1]) == False:
                print(s[right:right+1])
                right -= 1
                continue

            if s[left:left+1] != s[right:right+1]:
                return False

            left += 1
            right -= 1

        return True

        