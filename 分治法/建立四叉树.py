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
    m, n = len(grid), (len(grid[0]) if grid else 0)
    total = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            total[i][j] = total[i][j - 1] + total[i - 1][j] - total[i - 1][j - 1] + grid[i -1][j -1]

    def get_sum(r0, c0, r1, c1):
        res = total[r1][c1] - total[r1][c0] - total[r0][c1] + total[r0][c0]
        return res

    def recur(r0, c0, r1, c1):
        sums = get_sum(r0, c0, r1, c1)
        if sums == 0:
            return Node(False, True)
        if sums == (r1 - r0 if (r1 - r0) else 1) * (c1 - c0 if (c1 - c0) else 1):
            return Node(True, True)

        node = Node(
            True,
            False,
            recur(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
            recur(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
            recur((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
            recur((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
        )
        return node

    return recur(0, 0, len(grid), len(grid[0]))


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]
    print(construct(grid))
