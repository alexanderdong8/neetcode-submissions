class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            res = max(res, (right - left) * min(heights[left], heights[right]))

            if heights[right] >= heights[left]:
                left += 1
            else:
                right -= 1

        return res