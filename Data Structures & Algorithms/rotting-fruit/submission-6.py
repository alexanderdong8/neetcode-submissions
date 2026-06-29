class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0 and grid[row][col] != 2 
        fresh = 0
        q = collections.deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        if not q and fresh == 0:
            return 0
        if not q and fresh > 0:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            row, col, minutes = q.popleft()
            if grid[row][col] == 1:
                grid[row][col] = 2
                fresh -= 1
            if fresh == 0:
                return minutes
            
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if isValid(new_row, new_col):
                    q.append((new_row, new_col, minutes + 1))

        return -1

            