class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for x in range(len(heights)-1, -1, -1):
            if not stack:
                stack.append(heights[x])
                res.append(x)
            elif stack and heights[x] > stack[-1]:
                stack.append(heights[x])
                res.append(x)
        res.reverse()
        return res