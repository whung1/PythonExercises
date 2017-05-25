"""
https://leetcode.com/problems/remove-linked-list-elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ('' if self.next is None else '->' + str(self.next))


def remove_elements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    prev = None
    cur = head
    while cur is not None:
        if cur.val == val:
            if head.val == val:
                head = head.next
            if prev:
                prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return head


if __name__ == '__main__':
    start = ListNode(6)
    start.next = ListNode(1)
    start.next.next = ListNode(6)
    start.next.next.next = ListNode(2)
    start.next.next.next.next = ListNode(6)

    print(remove_elements(start, 6))
