class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def isValid(row, col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])
        
        pacSet, atlSet = set(), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, seen):
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if (new_row, new_col) not in seen and isValid(new_row, new_col) and heights[new_row][new_col] >= heights[row][col]:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col, seen)

        for c in range(len(heights[0])):
            pacSet.add((0, c))
            dfs(0, c, pacSet)
            atlSet.add((len(heights)-1, c))
            dfs(len(heights) - 1, c, atlSet)
        for r in range(len(heights)):
            pacSet.add((r, 0))
            dfs(r, 0, pacSet)
            atlSet.add((r, len(heights[0]) - 1))
            dfs(r, len(heights[0]) - 1, atlSet)
        print(pacSet, atlSet)
        intersection_set = pacSet.intersection(atlSet)
        res = []
        for row, col in intersection_set:
            res.append([row, col])

        return res