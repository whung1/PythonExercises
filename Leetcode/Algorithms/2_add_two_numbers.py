"""
https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

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
    list_sum = 0
    ll_start = prev = ListNode(0)
    while l1 or l2 or list_sum != 0:
        if l1:
            list_sum += l1.val
            l1 = l1.next
        if l2:
            list_sum += l2.val
            l2 = l2.next
        node = ListNode(list_sum % 10)
        prev.next = node
        prev = node
        list_sum = int(list_sum / 10)
    return ll_start.next

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

    print(start)
    print(start2)
    print(add_two_numbers(start2, start))