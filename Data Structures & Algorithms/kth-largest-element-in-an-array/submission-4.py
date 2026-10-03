class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        a min heap will store the largest elements and it won't remove the largest elemtns, so if i keep 5 elements in teh heap apt all times it will always hold the 5 largest elements if we go through the whole array with the bottom being the 5th largest
        n log k because it takes log k to add or remove from the heap and we do that n times. 
        '''

        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        
        return minHeap[0]