"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Note: There are at least two nodes in this BST.
"""
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        left = "" if self.left is None else str(self.left)
        right = "" if self.right is None else str(self.right)
        return str(self.val) + left + right


def get_minimum_difference(root):
    """
    Since it is given that this is a BST meaning that for every subtree, left subtree is less than and right subtree is
    greater than.
    
    In order traversal of BST will give least to greatest, thus the smallest possible differences.
    
    :type root: TreeNode
    :rtype: int
    """
    prev = None
    cur_min = sys.maxsize

    def in_order_traversal(node):
        if node is None:
            return
        in_order_traversal(node.left)
        nonlocal prev
        if prev is not None:
            nonlocal cur_min
            cur_min = min(cur_min, abs(prev.val - node.val))
        prev = node
        in_order_traversal(node.right)

    in_order_traversal(root)
    return cur_min


if __name__ == '__main__':
    print("""
    Example:
    
    Input:
    
       1
        \
         3
        /
       2
    
    Output:
    1
    
    Explanation:
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
    """)

    ex_root = TreeNode(1)
    ex_root.right = TreeNode(3)
    ex_root.right.left = TreeNode(2)
    print(get_minimum_difference(ex_root))

