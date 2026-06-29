class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for index, val in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < val:
                ans[stack[-1]] = index - stack[-1]
                stack.pop()

            stack.append(index)

        return ans