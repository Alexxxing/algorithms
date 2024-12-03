from typing import Optional

from 二叉树.base_tree import TreeNode


def is_symmetric(root: Optional[TreeNode]) -> bool:

    def recur(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return recur(left.left, right.right) and recur(left.right, right.left)

    return recur(root.left, root.right)


if __name__ == '__main__':
    tree = TreeNode(0)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    assert (is_symmetric(tree) is False)
