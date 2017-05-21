"""
https://leetcode.com/problems/odd-even-linked-list

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ('' if self.next is None else '->' + str(self.next))


def odd_even_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return
    prev_odd = odd = head
    even_start = even = head.next
    while odd is not None and even is not None:
        # Go to next odd
        prev_odd = odd
        odd.next = even.next
        odd = even.next
        if odd is not None:
            # Go to next even
            even.next = odd.next
            even = odd.next
    # Connect the odd end with the even end
    odd = prev_odd if odd is None else odd
    odd.next = even_start
    return head

if __name__ == '__main__':
    start = ListNode(1)
    start.next = ListNode(2)
    start.next.next = ListNode(3)
    start.next.next.next = ListNode(4)

    print(start)
    print(odd_even_list(start))

    start = ListNode(1)
    start.next = ListNode(2)
    start.next.next = ListNode(3)
    start.next.next.next = ListNode(4)
    start.next.next.next.next = ListNode(5)

    print(start)
    print(odd_even_list(start))
