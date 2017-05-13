"""
https://leetcode.com/problems/palindrome-linked-list

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def is_palindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # get middle of linked list
    fast_node = head
    slow_node = head
    while fast_node is not None and fast_node.next is not None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

    # reverse latter half of linked list
    end_node = None
    while slow_node is not None:
        next_node = slow_node.next
        slow_node.next = end_node
        end_node = slow_node
        slow_node = next_node

    # Now iterate through list, if everything matches and end hits none, is a palindrome
    while end_node is not None:
        if head.val != end_node.val:
            return False
        head = head.next
        end_node = end_node.next

    return True



def print_linked_list(head):
    while head is not None:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    start = ListNode('a')
    start.next = ListNode('b')
    start.next.next = ListNode('c')
    start.next.next.next = ListNode('b')
    start.next.next.next.next = ListNode('a')
    print(is_palindrome(start))

    start = ListNode(0)
    start.next = ListNode(0)
    print(is_palindrome(start))

    start = ListNode(0)
    print(is_palindrome(start))

    start = ListNode(1)
    start.next = ListNode(2)
    start.next.next = ListNode(2)
    start.next.next.next = ListNode(1)
    print(is_palindrome(start))
