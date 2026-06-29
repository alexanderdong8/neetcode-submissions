class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_negated = [-x for x in stones]
        heapq.heapify(stones_negated)

        while (len(stones_negated) > 1):
            y = heapq.heappop(stones_negated) * -1
            x = heapq.heappop(stones_negated) * -1

            if y > x:
                heapq.heappush(stones_negated, (y-x) * -1)
            
        
        if not stones_negated:
            return 0 
        else:
            return stones_negated[0] * -1