class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        INF = 2147483647
        q = deque()
        seen = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            row, col, steps = q.popleft()
            if grid[row][col] == INF:
                grid[row][col] = steps
            
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy

                if isValid(newRow, newCol) and (newRow, newCol) not in seen and grid[newRow][newCol] == INF:
                    q.append((newRow, newCol, steps+1))
