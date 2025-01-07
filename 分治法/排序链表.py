"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：

输入：head = [4,2,1,3]
输出：[1,2,3,4]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    dummy = ListNode(0)
    cur = dummy
    while left and right:
        if left.val < right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    cur.next = left if left else right
    return dummy.next


if __name__ == '__main__':
    head = ListNode(4, next=ListNode(2, next=ListNode(1, next=ListNode(3))))
    sort_head = sort_list(head)
    print(sort_head)
