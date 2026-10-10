class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x in range(len(points)):
            for y in range(len(points)):
                if x == y:
                    continue
                graph[tuple(points[x])].append(tuple(points[y]))

        start = tuple(points[0])
        minHeap = [(0, start)]
        seen = set()
        res = 0
        while len(seen) < len(points):
            length, node = heapq.heappop(minHeap)

            if node in seen:
                continue

            seen.add(node)
            res += length

            for newNode in graph[node]:
                if newNode not in seen:
                    dist = abs(newNode[1] - node[1]) + abs(newNode[0] - node[0])
                    heapq.heappush(minHeap, (dist, newNode))

        return res

