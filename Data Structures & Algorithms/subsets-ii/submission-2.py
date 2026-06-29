class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        def dfs(index, arr):
            

            res.append(arr.copy())


            if index == len(nums):
                return

            while index < len(nums):
                arr.append(nums[index])
                dfs(index+1, arr)
                arr.pop()
                while index < len(nums) - 1 and nums[index] == nums[index+1]:
                    index += 1

                index += 1
            # for x in range(index, len(nums)):
            #     arr.append(nums[x])
            #     print(arr, nums[x])
            #     dfs(x+1, arr)
            #     arr.pop()

        dfs(0, [])
        print(seen)
        return res

            