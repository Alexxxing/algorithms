"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长
子串
 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def length_of_longest_substring(s: str) -> int:
    dic = {}
    l = -1
    ans = 0
    for i in range(len(s)):
        if s[i] in dic:
            l = max(dic[s[i]], l)
        dic[s[i]] = i
        ans = max(ans, i - l)
    return ans


if __name__ == '__main__':
    s = "au"
    print(length_of_longest_substring(s))
