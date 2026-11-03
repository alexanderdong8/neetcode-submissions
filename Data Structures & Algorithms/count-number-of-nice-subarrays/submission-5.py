class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, res = 0, 0
        mid = 0
        odd = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1

            if odd == k:
                while nums[mid] % 2 == 0:
                    mid += 1

                res += (mid - left + 1)
            else:
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1

                mid = left
        if odd == k:
            res += 1
        return res
