def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    def dfs(i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
            return False
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = ""
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = word[k]
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False


if __name__ == '__main__':
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
