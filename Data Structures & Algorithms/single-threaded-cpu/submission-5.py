import heapq
import collections
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_list = [(start, time, index) for index, (start, time) in enumerate(tasks)]
        task_list.sort()
        curr_time = 0
        res = []
        minHeap = []
        x = 0
        while x < len(task_list):
            if not minHeap:
                res.append(task_list[x][2])
                curr_time = task_list[x][0]+task_list[x][1]
                x += 1
                while x < len(task_list) and task_list[x][0] <= curr_time:
                    start, time, index = task_list[x][0], task_list[x][1], task_list[x][2]
                    heapq.heappush(minHeap, (time, index, start))
                    x += 1

            while minHeap:
                time, index, start = heapq.heappop(minHeap)
                print(time, index, start)
                res.append(index)
                curr_time += time
                while x < len(task_list) and task_list[x][0] <= curr_time:
                    start, time, index = task_list[x][0], task_list[x][1], task_list[x][2]
                    heapq.heappush(minHeap, (time, index, start))
                    x += 1

        return res

            

        