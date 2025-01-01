from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    def recur(grid, r, c):
        if not in_area(grid, r, c):
            return

        if grid[r][c] != "O":
            return

        grid[r][c] = "#"

        recur(grid, r - 1, c)
        recur(grid, r + 1, c)
        recur(grid, r, c + 1)
        recur(grid, r, c - 1)

    def in_area(grid, r, c):
        m, n = len(grid), len(grid[0])
        return 0 <= r < m and 0 <= c < n

    for r in range(len(board)):
        for c in range(len(board[0])):
            if (r == 0 or c == 0 or r == len(board) - 1 or c == len(board[0]) - 1) and board[r][c] == "O":
                recur(board, r, c)

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "O":
                board[r][c] = "X"
            if board[r][c] == "#":
                board[r][c] = "O"


if __name__ == '__main__':
    board = [["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"],
             ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    solve(board)
    for i in board:
        print(i)
