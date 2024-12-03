def is_happy(n: int) -> bool:
    while n > 1:
        tmp = 0
        for _ in str(n):
            tmp += int(_) * int(_)
        n = tmp


if __name__ == '__main__':
    is_happy(2)
