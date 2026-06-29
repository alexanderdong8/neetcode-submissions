class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for x, y, z in times:
            edges[x].append((y,z))
        minHeap = [(0, k)]
        visited = set()
        res = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
            
        return res if len(visited) == n else -1
