"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵
平衡
 二叉搜索树。

示例 1：

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:

    def recur(l, r):
        if l > r:
            return
        mid = (l + r) // 2
        node = TreeNode(nums[mid])
        node.left = recur(l, mid - 1)
        node.right = recur(mid + 1, r)
        return node

    return recur(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    tree = sorted_array_to_bst(nums)
    print(sorted_array_to_bst(nums))
