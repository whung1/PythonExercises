"""
https://leetcode.com/problems/binary-tree-tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Note:
    1. The sum of node values in any subtree won't exceed the range of 32-bit integer.
    2. All the tilt values won't exceed the range of 32-bit integer.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_tilt(root):
    """
    Postorder DFS for sum, and then return the tilt sum.
    :type root: TreeNode
    :rtype: int
    """
    tilt_sum = 0

    def get_tilt(node):
        if node is None:
            return 0
        nonlocal tilt_sum
        left, right = get_tilt(node.left), get_tilt(node.right)
        tilt_sum += abs(left - right)
        return node.val + left + right

    get_tilt(root)
    return tilt_sum

if __name__ == '__main__':
    print("""
    Example:
    Input: 
             1
           /   \\
          2     3
    Output: 1
    
    Explanation: 
    Tilt of node 2 : 0
    Tilt of node 3 : 0
    Tilt of node 1 : |2-3| = 1
    Tilt of binary tree : 0 + 0 + 1 = 1
    """)

    ex_root = TreeNode(1)
    ex_root.left = TreeNode(2)
    ex_root.right = TreeNode(3)
    print(find_tilt(ex_root))
