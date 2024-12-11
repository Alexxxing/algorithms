from typing import List


def plus_one(digits: List[int]) -> List[int]:
    digits.insert(0, 0)
    n = len(digits) - 1
    while n >= 0:
        if digits[n] + 1 > 9:
            digits[n] = 0
            n -= 1
        else:
            digits[n] += 1
            break
    if not digits[0]:
        digits.pop(0)
    return digits


if __name__ == '__main__':
    print(plus_one([9]))
