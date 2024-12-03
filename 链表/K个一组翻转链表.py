from typing import Optional

from 链表.链表结构 import ListNode


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:

    def reverse_node(node):
        last = None
        cur = node
        while cur:
            _next = cur.next
            cur.next = last
            last = cur
            cur = _next

        return last

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    end = dummy

    while end:
        for i in range(k):
            if not end:
                break
            end = end.next
        if not end:
            break
        start = pre.next
        _next = end.next
        end.next = None
        pre.next = reverse_node(start)
        start.next = _next
        pre = start
        end = pre

    return dummy.next


if __name__ == '__main__':
    dummy = ListNode(0)
    cur = dummy
    for i in range(1, 6):
        cur.next = ListNode(i)
        cur = cur.next

    dummy.next = reverse_k_group(dummy.next, 2)
    print(dummy.next)
