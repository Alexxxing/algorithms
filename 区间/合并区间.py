"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    i = 0
    ans = []
    intervals.sort()
    while i < n:
        interval = intervals[i]
        if ans and interval[0] <= ans[-1][-1]:
            ans[-1][-1] = max(interval[1], ans[-1][-1])
        else:
            ans.append(interval)
        i += 1
    return ans


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
