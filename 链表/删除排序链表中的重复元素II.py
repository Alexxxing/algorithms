"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

示例 1：

输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：

输入：head = [1,1,1,2,3]
输出：[2,3]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    cur = pre.next
    while cur and cur.next:
        if cur.val != cur.next.val:
            pre = pre.next
            cur = cur.next
            continue
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        _next = cur.next
        cur.next = None
        pre.next = _next
        cur = _next
    return dummy.next


if __name__ == '__main__':
    dummy = ListNode(0)
    nums = [1, 2, 3, 3, 4, 4, 5]
    cur = dummy
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    head = dummy.next
    res = delete_duplicates(head)
    c = res
    while c:
        print(c.val)
        c = c.next
