def climb_stairs(n: int) -> int:
    def recur(num):
        if num == 0:
            return 1
        if num < 0:
            return 0

        two = recur(num - 2)
        one = recur(num - 1)

        return two + one

    return recur(n)


if __name__ == '__main__':
    print(climb_stairs(38))
