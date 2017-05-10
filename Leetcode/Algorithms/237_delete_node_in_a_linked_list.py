"""
https://leetcode.com/problems/delete-node-in-a-linked-list

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ('' if self.next is None else '->' + str(self.next))


def delete_node(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    # Note: can't simply do node = node->next since its pass by value, where the pointer itself is the value
    if node.next is None:
        return
    else:
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    start = ListNode(0)
    start.next = ListNode(1)
    print(start)
    delete_node(start)
    print(start)
