"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    n = len(s)
    l, r = 0, 0
    ans = ""
    if n < len(t):
        return ans
    differ = Counter(t)

    while r < n:
        add_word = s[r]
        if add_word in differ:
            differ[add_word] -= 1
        while l <= r and all(i <= 0 for i in differ.values()):
            if not ans or len(ans) > r - l + 1:
                ans = s[l:r + 1]
            remove_word = s[l]
            if remove_word in differ:
                differ[remove_word] += 1
            l += 1
        r += 1
    return ans


if __name__ == '__main__':
    s = "a"
    t = "a"
    print(min_window(s, t))
