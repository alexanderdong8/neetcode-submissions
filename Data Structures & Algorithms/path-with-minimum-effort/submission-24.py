class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def isValid(row, col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])
        res = 0
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        minHeap = [(0,0,0)]
        seen = set()
        costs = {(0,0): 0}
        while minHeap:
            cost, row, col = heapq.heappop(minHeap)
            # if costs.get((row, col), float('inf')) < cost:
            #     continue

            if (row, col) in seen: # this is important because you can't put it immediatelly into the loop because since I use a heap it doens't guarantee it will be looked at in the same order and another thing taht is sbetter may be put in first
                continue
            seen.add((row, col))

            if (row, col) == (len(heights)-1, len(heights[0])-1):
                return cost

            for dx, dy in directions:
                newRow = dx + row
                newCol = dy + col
                if (newRow, newCol) not in seen and isValid(newRow, newCol):
                    diff = abs(heights[newRow][newCol] - heights[row][col])
                    newCost = max(cost, diff)
                    heapq.heappush(minHeap, (newCost, newRow, newCol))
                    
        return -1

            


                