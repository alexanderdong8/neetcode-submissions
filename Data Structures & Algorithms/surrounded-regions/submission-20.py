class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n and board[r][c] == "O"

        def dfs(r, c):
            """Return (cells_in_island, touches_border_flag)."""
            stack = [(r, c)]
            cells = []
            touches_border = False

            while stack:
                x, y = stack.pop()
                cells.append((x, y))

                # Check if this cell is on the border
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    touches_border = True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if isValid(nx, ny) and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))

            return cells, touches_border

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