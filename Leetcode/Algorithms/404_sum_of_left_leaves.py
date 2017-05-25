"""
https://leetcode.com/problems/sum-of-left-leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
            left = "" if self.left is None else str(self.left)
            right = "" if self.right is None else str(self.right)
            return str(self.val) + left + right


def sum_of_left_leaves(root, is_left = False):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val if is_left else 0

    return sum_of_left_leaves(root.left, True) + sum_of_left_leaves(root.right)

if __name__ == '__main__':
    ex_root = TreeNode(3)
    ex_root.left = TreeNode(9)
    ex_root.right = TreeNode(20)
    ex_root.right.left = TreeNode(15)
    ex_root.right.right = TreeNode(7)

    print(sum_of_left_leaves(ex_root))
