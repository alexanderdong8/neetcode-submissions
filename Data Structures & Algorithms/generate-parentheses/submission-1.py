class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openL, openR):
            if openL == openR == n:
                res.append("".join(stack))
                return
            if openL < n:
                stack.append("(")
                backtrack(openL+1, openR)
                stack.pop()
            if openR < openL:
                stack.append(")")
                backtrack(openL, openR+1)
                stack.pop()
            
        backtrack(0,0)
        return res
        