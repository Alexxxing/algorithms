from collections import defaultdict


def trailing_zeroes(n):
    """
    :type n: int
    :rtype: int
    """
    ans = 0
    t = 5
    while t <= n:
        ans += n // t
        t = t * 5
    return ans


if __name__ == '__main__':
    print(trailing_zeroes(30))
