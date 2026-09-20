class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    seenRow[row].add((row, col))
                    seenCol[col].add((row, col))

        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if len(seenRow[row]) >= 2 or len(seenCol[col]) >= 2:
                        res += 1

        return res
                