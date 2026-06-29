class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x, y):
            return (x**2 + y**2)**0.5
        
        closest = []
        heapq.heapify(closest)
        for x, y in points:
            distance = euclidean_distance(x, y)
            heapq.heappush(closest, (distance, x, y))

        ans = []
        for _ in range(k):
            var = heapq.heappop(closest)
            x = var[1]
            y = var[2]
            ans.append([x,y])

        return ans

        