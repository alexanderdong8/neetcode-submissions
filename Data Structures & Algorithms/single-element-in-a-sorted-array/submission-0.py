class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)

        res = []
        for num in seen:
            res.append(num)

        return res[0]