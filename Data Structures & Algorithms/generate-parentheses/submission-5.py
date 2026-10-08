class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(arr, left, right):
            if len(arr) == n*2:
                res.append("".join(arr.copy()))
                return


            arr.append("(")
            dfs(arr, left+1, right)
            arr.pop()
            if right < left:
                arr.append(")")
                dfs(arr, left, right)
                arr.pop()

        dfs([], 0)

        return res
            