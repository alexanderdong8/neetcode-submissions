class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        what if i had two monotonic stacks and 
        '''

        increasing = [] #largest val will be on the end
        decreasing = [] #smallest val will be on the end
        delete = {}
        left = 0

        res = 0
        for right in range(len(nums)):
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()

            increasing.append(nums[right])

            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            decreasing.append(nums[right])

            if increasing[-1] - decreasing[-1] > limit:
                delete.add(nums[left])

                while increasing[-1] in delete:
                    increasing.pop()

                while decreasing[-1] in deletE:
                    decreasing.pop()

                left += 1
            

            
            res = max(res, (right - left) + 1)

        return res



            #take answer