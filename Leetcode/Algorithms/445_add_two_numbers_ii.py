"""
https://leetcode.com/problems/add-two-numbers-ii

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
from collections import deque
import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ('' if self.next is None else '->' + str(self.next))


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    s1 = deque()
    s2 = deque()

    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next

    sum = 0
    cur_node = None
    while s1 or s2 or sum != 0:
        if s1:
            sum += s1.pop()
        if s2:
            sum += s2.pop()
        new_node = ListNode(sum % 10)
        new_node.next = cur_node
        cur_node = new_node
        sum = math.floor(sum/10)
    return cur_node

if __name__ == '__main__':
    start = ListNode(1)
    start.next = ListNode(2)
    start.next.next = ListNode(3)
    start.next.next.next = ListNode(4)
    start.next.next.next.next = ListNode(5)

    start2 = ListNode(1)
    start2.next = ListNode(2)
    start2.next.next = ListNode(3)
    start2.next.next.next = ListNode(4)
    start2.next.next.next.next = ListNode(5)

    print(add_two_numbers(start, start2))
