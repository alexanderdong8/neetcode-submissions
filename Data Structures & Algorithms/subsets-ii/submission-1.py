class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        def dfs(index, arr):
            
            if tuple(arr) not in seen:
                res.append(arr.copy())
                seen.add(tuple(arr))

            if index == len(nums):
                return


            for x in range(index, len(nums)):
                arr.append(nums[x])
                print(arr, nums[x])
                dfs(x+1, arr)
                arr.pop()

        dfs(0, [])
        print(seen)
        return res

            