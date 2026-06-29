class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n and board[r][c] == "O"

        def dfs(row, col):
            res = [[row, col]]
            touches_edge = (row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1)

            
            for dx, dy in directions:
                nx = dx + row
                ny = dy + col
                if (nx, ny) not in seen and isValid(nx, ny):
                    seen.add((nx, ny))
                    sub_list, sub_edge = dfs(nx, ny)
                    res.extend(sub_list)
                    touches_edge = touches_edge or sub_edge
            return res, touches_edge



        # Store all cells that should be flipped
        to_flip = []

        for r in range(m):
            for c in range(n):
                if isValid(r, c) and (r, c) not in seen:
                    seen.add((r, c))
                    cells, touches_border = dfs(r, c)
                    if not touches_border:
                        to_flip.extend(cells)

        # Flip surrounded regions
        for r, c in to_flip:
            board[r][c] = "X"