def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    m, n = len(board), len(board[0])

    def dfs(r, c, k):
        if not 0 <= r < m or not 0 <= c < n or board[r][c] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        board[r][c] = ""
        res = dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1)
        board[r][c] = word[k]
        return res

    for r in range(m):
        for c in range(n):
            if board[r][c] == word[0]:
                if dfs(r, c, 0):
                    return True
    return False


if __name__ == '__main__':
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
