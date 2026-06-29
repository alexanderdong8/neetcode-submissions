class Solution:
    def isValid(self, s: str) -> bool:
        chars = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in chars:
                stack.append(char)
            else:
                if not stack or chars[stack.pop()] != char:
                    return False
        
        return False if stack else True