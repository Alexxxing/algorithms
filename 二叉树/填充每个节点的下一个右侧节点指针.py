class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    if not root:
        return root
    head = root

    while head:
        dummy = Node(0)
        cursor = dummy
        cur = head

        while cur:
            if cur.left:
                cursor.next = cur.left
                cursor = cursor.next
            if cur.right:
                cursor.next = cur.right
                cursor = cursor.next
            cur = cur.next
        head = dummy.next

    return root


if __name__ == '__main__':
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.right = Node(7)

    connect(node)
    print(node)
