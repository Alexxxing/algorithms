"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


"""


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    m, n = len(board), len(board[0])

    def in_area(i, j):
        return bool(0 <= i < m and 0 <= j < n)

    def recur(i, r, c):
        if not in_area(r, c) or board[r][c] != word[i]:
            return False
        if i == len(word) - 1:
            return True

        board[r][c] = ""
        res = recur(i + 1, r - 1, c) or recur(i + 1, r + 1, c) or recur(i + 1, r, c - 1) or recur(i + 1, r, c + 1)
        board[r][c] = word[i]
        return res

    for i in range(m):
        for j in range(n):
            if recur(0, i, j):
                return True
    return False


if __name__ == '__main__':
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
