def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    counter = [0] * 2
    ans = []
    tmp = []

    def dfs(num):
        if num == 0:
            ans.append("".join(tmp))
            return
        for i in "()":
            if i == "(":
                counter[0] += 1
            else:
                counter[1] += 1
            if counter[0] > n:
                counter[0] -= 1
                continue
            if counter[1] > n:
                counter[1] -= 1
                continue
            if counter[1] > counter[0]:
                counter[1] -= 1
                continue
            tmp.append(i)
            dfs(num - 1)
            if i == "(":
                counter[0] -= 1
            else:
                counter[1] -= 1
            tmp.pop()

    dfs(n * 2)
    return ans


if __name__ == '__main__':
    print(generate_parenthesis(3))
