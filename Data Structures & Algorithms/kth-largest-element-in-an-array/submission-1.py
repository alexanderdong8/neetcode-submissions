class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        size = len(nums) - k + 1

        while len(nums) > size:
            heapq.heappop(nums)

        return nums[0] * -1