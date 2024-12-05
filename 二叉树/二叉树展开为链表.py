from typing import Optional

from 二叉树.base_tree import TreeNode


def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return root
    dummy = TreeNode(root.val)
    cur = dummy

    def recur(node):
        if not node:
            return
        nonlocal cur
        cur.right = TreeNode(node.val)
        cur.left = None
        cur = cur.right
        recur(node.left)
        recur(node.right)

    recur(root)

    root = dummy

    return root


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.right.right = TreeNode(6)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    flatten(tree)
    print(tree)


