from typing import Optional

from 二叉树.base_tree import TreeNode


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return

    return is_symmetric(root.left) == is_symmetric(root.right)


if __name__ == '__main__':
    tree = TreeNode(0)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    assert (is_symmetric(tree), False)
