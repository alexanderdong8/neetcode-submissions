class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = Counter(nums)
        res = []
        for num, occurrences in countMap.items():
            if occurrences > (len(nums) / 3):
                res.append(num)
        
        return res