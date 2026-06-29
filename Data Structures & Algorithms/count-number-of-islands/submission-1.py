class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in seen and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if isValid(new_row, new_col):
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)




        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    res += 1
                    seen.add((row, col))
                    dfs(row, col)
        
        return res