import random
import inspect


def echo_multiplication_table(num):
    # 打印九九乘法表
    for i in range(1, num+1):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print('')


if __name__ == '__main__':
    echo_multiplication_table(9)
