class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(curr, i, total):
            if total >= target:
                if total == target:
                    ans.append(curr.copy())
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(curr, j, total+nums[j])
                curr.pop()
        
        dfs([], 0, 0)
        return ans
