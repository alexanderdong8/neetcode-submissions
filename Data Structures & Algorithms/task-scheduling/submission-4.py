from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-x for x in counts.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                val = heapq.heappop(maxHeap) + 1
                if val:
                    queue.append((val, time + n))
            else:
                time = queue[0][1]

            
            if queue and queue[0][1] == time:
                new_time = queue.popleft()
                heapq.heappush(maxHeap, new_time[0])

            
        return time

