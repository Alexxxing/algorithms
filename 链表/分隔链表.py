"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

示例 2：

输入：head = [2,1], x = 2
输出：[1,2]
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_list_node(nums: List[int]):
    """
    :param nums: num list for generate list node
    :return: list node
    """
    dummy = ListNode(0)
    cur = dummy
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy.next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    small_dummy, bigger_dummy = ListNode(0), ListNode(0)
    small, bigger = small_dummy, bigger_dummy
    cur = head
    while cur:
        if cur.val >= x:
            bigger.next = cur
            bigger = bigger.next
        else:
            small.next = cur
            small = small.next
        cur = cur.next
    bigger.next = None
    small.next = bigger_dummy.next
    return small_dummy.next


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 5, 2]
    head = generate_list_node(nums)
    res = partition(head, 3)
    c = res
    while c:
        print(c.val)
        c = c.next
