from typing import Optional

from 二叉树.base_tree import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return target_sum == root.val
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    assert has_path_sum(tree, 5) is False
