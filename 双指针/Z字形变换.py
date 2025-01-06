"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

"""


def convert(s: str, num_rows: int) -> str:
    if not s:
        return ""
    if num_rows <= 1:
        return s
    stack = [""] * num_rows
    index = 0
    flag = -1
    for i in range(len(s)):
        if index == 0 or index == num_rows - 1:
            flag = -flag
        stack[index] += s[i]
        index += flag

    return "".join(stack)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(convert(s, numRows))
