from collections import deque

from 二叉树.base_tree import TreeNode


def pre_order(tree: TreeNode):
    if not tree:
        return tree
    print(tree.val, end=" ")
    pre_order(tree.left)
    pre_order(tree.right)


def in_order(tree: TreeNode):
    if not tree:
        return tree
    in_order(tree.left)
    print(tree.val, end=" ")
    in_order(tree.right)


def post_order(tree: TreeNode):
    if not tree:
        return tree
    post_order(tree.left)
    post_order(tree.right)
    print(tree.val, end=" ")


def level_order(tree: TreeNode):
    if not tree:
        return tree
    stack = deque([tree])
    while stack:
        cur = stack.popleft()
        print(cur.val, end=" ")
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)


if __name__ == '__main__':
    """
             1
            /  \
          2      3
         / \    / \
        4   5  6   7
           / \
          8   9   
    """
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    tree.left.right.left = TreeNode(8)
    tree.left.right.right = TreeNode(9)
    # 先序遍历
    pre_order(tree)
    print("")
    # 中序遍历
    in_order(tree)
    print("")
    # 后续遍历
    post_order(tree)
    print("")
    # 层序遍历
    level_order(tree)
    print("")
