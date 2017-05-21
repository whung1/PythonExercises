"""
https://leetcode.com/problems/reverse-linked-list

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ('' if self.next is None else '->' + str(self.next))


def reverse_list_iterative(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt


def reverse_list_recursive(node, prev=None):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if node is None:
        return
    nxt = node.next
    node.next = prev
    reverse_list_recursive(nxt, node)


if __name__ == '__main__':
    start = ListNode(1)
    start.next = ListNode(2)
    start.next.next = ListNode(3)
    start.next.next.next = ListNode(4)
    start.next.next.next.next = ListNode(5)
    end = start.next.next.next.next

    print(start)
    reverse_list_iterative(start)
    print(end)
    reverse_list_recursive(end)
    print(start)
