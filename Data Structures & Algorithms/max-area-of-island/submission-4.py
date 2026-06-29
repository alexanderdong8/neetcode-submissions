class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in seen and grid[row][col] == 1

        def dfs(row, col):
            area = 1
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if isValid(new_row, new_col):
                    seen.add((new_row, new_col))
                    area += dfs(new_row, new_col)

            return area




        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    return_val = dfs(row, col)
                    res = max(res, return_val)
        
        return res