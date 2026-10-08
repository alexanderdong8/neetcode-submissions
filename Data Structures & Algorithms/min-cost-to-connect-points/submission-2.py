class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x in range(len(points)):
            for y in range(len(points)):
                if x == y:
                    continue
                graph[tuple(points[x])].append(tuple(points[y]))

        start = (points[0][0], points[0][1])
        seen = set([start])
        minHeap = [(start, 0)]
        res = 0
        while len(seen) < len(points):
            
            while minHeap and minHeap[0][0] in seen:
                heapq.heappop(minHeap)

            
            (x, y), length = heapq.heapop(minHeap)
            res += length

            for (newX, newY) in graph[(x, y)]:
                if (newX, newY) not in seen:
                    seen.add((newX, newY))
                    distance = abs(newX - x) + abs(newY - y)
                    heapq.heappush(((newX, newY), distance))

        return res



