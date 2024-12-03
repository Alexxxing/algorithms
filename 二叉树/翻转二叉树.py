from typing import Optional

from 二叉树.base_tree import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    else:
        root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


if __name__ == '__main__':
    tree = TreeNode(0)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    invert_tree(tree)
    print(tree.left)
    print(tree.right)
