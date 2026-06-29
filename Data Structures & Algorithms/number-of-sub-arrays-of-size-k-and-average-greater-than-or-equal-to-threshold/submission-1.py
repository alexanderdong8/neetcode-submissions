class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        left = 0
        res = 0
        for right in range(len(arr)):
            sum += arr[right]

            while right - left + 1 > k:
                sum -= arr[left]
                left += 1

            if right >= k-1 and sum // (right-left+1) >= threshold:
                res += 1

        return res