"""
https://leetcode.com/problems/maximum-depth-of-binary-tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return max_depth_helper(root, 0)


def max_depth_helper(node, depth):
    """
    :type node: TreeNode
    :type depth: int
    :rtype: int
    """
    if not node:
        return depth

    left_depth = max_depth_helper(node.left, depth+1)
    right_depth = max_depth_helper(node.right, depth+1)
    return left_depth if left_depth > right_depth else right_depth

if __name__ == "__main__":
    print("""
    Example #1:
        Null Tree
        Output: 0

    Example #2:
        Input: Root with no children
        Output: 1

    Example #3:
        Input:
                1
              /
            2
        Output: 2

    Example #4:
        Input:
                1
              /   \\
            2       3
          /   \\
        4       5
        Output: 3
    """)

    print(max_depth(None))  # Example #1
    ex_root = TreeNode(1)
    print(max_depth(ex_root))  # Example #2
    ex_root.left = TreeNode(2)
    print(max_depth(ex_root))  # Example #3
    ex_root.right = TreeNode(3)
    ex_root.left.left = TreeNode(4)
    ex_root.left.right = TreeNode(5)
    print(max_depth(ex_root))  # Example #4
