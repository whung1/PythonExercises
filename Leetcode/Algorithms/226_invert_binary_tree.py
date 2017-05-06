"""
https://leetcode.com/problems/invert-binary-tree

Invert a binary tree.

Trivia:
This problem was inspired by this original tweet by Max Howell:
    "Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off."
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


def invert_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    invert_tree_recur(root)
    return root


def invert_tree_recur(node):
    if node is None:
        return
    temp = node.left
    node.left = node.right
    node.right = temp
    invert_tree(node.left)
    invert_tree(node.right)

if __name__ == '__main__':
    print("""
    Invert a binary tree.
    
         1
       /   \\
      2     3
     / \   / \\
    4   5 6   7
    to
         1
       /   \\
      3     2
     / \   / \\
    7   6 5   4
    """)

    print(invert_tree(None))
    ex_root = TreeNode(1)
    ex_root.left = TreeNode(2)
    ex_root.right = TreeNode(3)
    ex_root.left.left = TreeNode(4)
    ex_root.left.right = TreeNode(5)
    ex_root.right.left = TreeNode(6)
    ex_root.right.right = TreeNode(7)
    print(ex_root)
    print(invert_tree(ex_root))
