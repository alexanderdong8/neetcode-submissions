class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxL = height[left]
        maxR = height[right]
        currIndex = left
        res = 0

        while left < right:
            maxL = max(maxL, height[left])
            maxR = max(maxR, height[right])
            area = max(min(maxL, maxR) - height[currIndex], 0)
            res += area
            if maxL <= maxR:
                left += 1
                currIndex = left
            else:
                right -= 1
                currIndex = right

        return res