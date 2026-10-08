class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x in range(len(points)):
            for y in range(len(points)):
                if x == y:
                    continue
                graph[tuple(points[x])].append(tuple(points[y]))

        start = (points[0][0], points[0][1])
        seen = set()
        minHeap = [(start, 0)]
        res = 0
        while len(seen) < len(points):
            (x, y), length = heapq.heappop(minHeap)

            if (x, y) in seen:
                continue
            
            seen.add((x, y))
            res += length

            for (newX, newY) in graph[(x, y)]:
                if (newX, newY) not in seen:
                    # seen.add((newX, newY)) #cannot add here yet
                    distance = abs(newX - x) + abs(newY - y)
                    heapq.heappush(minHeap, ((newX, newY), distance))

        return res



