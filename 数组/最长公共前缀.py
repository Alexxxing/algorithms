"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    common_prefix = ""
    str1 = strs[0]
    n = len(str1)
    for i in range(n + 1):
        cur_pre = str1[:i]
        for s in strs[1:]:
            if not s.startswith(cur_pre):
                return common_prefix
        common_prefix = cur_pre
    return common_prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs))
