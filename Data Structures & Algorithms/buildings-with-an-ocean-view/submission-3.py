class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for index, height in enumerate(heights):

            while stack and height >= heights[stack[-1]]:
                stack.pop()

            stack.append(index)

        return stack


            