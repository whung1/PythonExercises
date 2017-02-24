"""Breath-First Search / Level-Order Traversal of a binary tree to get nodes by depth"""
from collections import deque, defaultdict


# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node: %s' % self.data


def get_nodes_by_depth(root, depth=0):
    """Given a binary tree, returns a dictionary of {depth: [node]}
    where depth is the key as a number with value of a list of relevant nodes at that depth
    Allows setting of depth in case it is a subtree where root does not have depth of 0"""
    if root is None:
        return

    # Set up queue for Breath First Search (BFS) / Level order traversal
    queue = deque()
    queue.append((root, depth))

    depth_dict = defaultdict(list)
    traverse_nodes_by_depth(queue, depth_dict)

    return depth_dict


def traverse_nodes_by_depth(queue, depth_dict):
    if len(queue) == 0:
        return depth_dict

    (node, depth) = queue.popleft()  # gets pair of (node, depth)

    #  Work on current node and add children, then recur
    depth_dict[depth].append(node)
    if node.left is not None:
        queue.append((node.left, depth+1))
    if node.right is not None:
        queue.append((node.right, depth+1))

    traverse_nodes_by_depth(queue, depth_dict)  # recur

if __name__ == '__main__':
    """Example tree
            1
          /   \
        2       3
      /   \
    4       5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(get_nodes_by_depth(root, 0))
