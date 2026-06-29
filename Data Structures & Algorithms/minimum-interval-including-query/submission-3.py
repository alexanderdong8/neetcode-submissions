import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        oldqueries = queries.copy()
        queries.sort()
        minHeap = []
        res = {}
        i = 0
        for query in queries:
            
            while i < len(intervals) and intervals[i][0] <= query:
                print(intervals[i][0] <= query <= intervals[i][1])
                heapq.heappush(minHeap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            print(minHeap)
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if minHeap:
                res[query] = minHeap[0][0]
            else:
                res[query] = -1
        arr = []
        print(res)
        for query in oldqueries:
            arr.append(res[query])
        return arr