from typing import Optional

from 二叉树.base_tree import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    tree_a = TreeNode(0)
    tree_a.left = TreeNode(1)
    tree_a.right = TreeNode(2)
    tree_b = TreeNode(0)
    tree_b.left = TreeNode(2)
    tree_b.right = TreeNode(1)
    print(is_same_tree(tree_a, tree_b))
