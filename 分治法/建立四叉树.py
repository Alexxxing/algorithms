from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid: List[List[int]]) -> 'Node':
    n = len(grid)
    total = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total[i][j] = total[i][j - 1] + total[i - 1][j] - total[i - 1][j - 1] + grid[i - 1][j - 1]

    def sum_total(r1, r0, c1, c0):
        return total[r1][c1] - total[r1][c0] - total[r0][c1] + total[r0][c0]

    def recur(r1, r0, c1, c0):
        s = sum_total(r1, r0, c1, c0)
        if s == 0:
            return Node(False, True)
        if s == (r1 - r0) * (c1 - c0):
            return Node(True, True)
        return Node(
            True,
            False,
            recur((r0 + r1) // 2, r0, (c0 + c1) // 2, c0),
            recur((r0 + r1) // 2, r0, c1, (c0 + c1) // 2),
            recur(r1, (r0 + r1) // 2, (c0 + c1) // 2, c0),
            recur(r1, (r0 + r1) // 2, c1, (c0 + c1) // 2)
        )

    return recur(n, 0, n, 0)


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]
    tree = construct(grid)
    print(tree)
