def rotate_matrix(matrix, angle):
    # 矩阵顺时针旋转
    n = len(matrix)
    result = [[0] * (n) for i in range(n)]
    angle_convert_result = (angle // 90) % 4
    angle_convert_remainder = angle % 90
    if angle_convert_remainder != 0:
        raise ValueError('输入的角度有问题！')

    if angle_convert_result == 1:
        for i in range(n):
            for j in range(len(matrix[0])):
                result[j][n-i-1] = matrix[i][j]
    if angle_convert_result == 2:
        for i in range(n):
            for j in range(len(matrix[0])):
                result[n-i-1][n-j-1] = matrix[i][j]
    if angle_convert_result == 3:
        for i in range(n):
            for j in range(len(matrix[0])):
                result[n-j-1][i] = matrix[i][j]
    if angle_convert_result == 0:
        result = matrix

    return result


def rotate_matrix_in_place(matrix):
    """
    在不创建等量内存地址空间情况下做翻转（双指针）
    :param matrix: 输入魔方
    """
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    for x in matrix:
        print(x, sep=' ')


def draw_matrix(matrix):
    """
    打印魔方
    :param matrix: 输入魔方
    """
    for block in matrix:
        print(block)


if __name__ == '__main__':
    original_matrix = [[i * 5 + j for j in range(5)] for i in range(5)]
    draw_matrix(original_matrix)
    result_matrix = rotate_matrix(original_matrix, 90)
    draw_matrix(result_matrix)

