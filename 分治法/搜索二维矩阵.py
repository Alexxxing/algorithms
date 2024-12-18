from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:

    if not matrix:
        return False
    up = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while up <= down:
        m1 = (up + down) // 2
        if matrix[m1][0] <= target <= matrix[m1][-1]:
            while left <= right:
                m2 = (left + right) // 2
                if matrix[m1][m2] == target:
                    return True
                elif matrix[m1][m2] > target:
                    right = m2 - 1
                else:
                    left = m2 + 1
            return False
        elif target < matrix[m1][0]:
            down = m1 - 1
        else:
            up = m1 + 1
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(search_matrix(matrix, target))
