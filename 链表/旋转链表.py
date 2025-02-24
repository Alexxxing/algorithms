"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：

输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：

输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return
    dummy = ListNode(0)
    dummy.next = head
    l = 0
    pre = dummy
    while pre.next:
        pre = pre.next
        l += 1
    k = k % l
    if not k:
        return head
    cur = dummy
    h = dummy
    for i in range(l - k):
        cur = cur.next
    _next = cur.next
    pre_next = h.next
    cur.next = None
    pre.next = pre_next
    h.next = _next
    return dummy.next


if __name__ == '__main__':
    dummy = ListNode(0)
    nums = [1, 2, 3, 4, 5, 6]
    cur = dummy
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    head = dummy.next
    res = rotate_right(head, 2)
    c = res
    while c:
        print(c.val)
        c = c.next
