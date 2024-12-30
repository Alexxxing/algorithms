from typing import List


def is_valid_su_do_ku(board: List[List[str]]) -> bool:
    row = [[0 for _ in range(9)] for _ in range(9)]
    column = [[0 for _ in range(9)] for _ in range(9)]
    subbox = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            c = board[i][j]
            if c != ".":
                n = int(c) - 1
                row[i][n] += 1
                column[j][n] += 1
                subbox[int(i / 3)][int(j / 3)][n] += 1
                if row[i][n] > 1 or row[j][n] > 1 or subbox[int(i / 3)][int(j / 3)][n] > 1:
                    return False
    return True


if __name__ == '__main__':
    board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    is_valid_su_do_ku(board)
