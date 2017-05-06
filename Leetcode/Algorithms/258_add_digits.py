"""
https://leetcode.com/problems/add-digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


def add_digits(num):
    """
    :type num: int
    :rtype: int
    """
    """
    There are three cases we can get from testing.

    if remaining digit is 0, then its zero.
    if the sum of all digits % 9 == 0, then we know the last digit sum must be 9, thus n % 9 -> sumdigits(n) = 9
    else it is the remainder.
    
    We can find this by reducing the problem first to two digits (since all subsequent increase in digits 
    will eventually be two digits, and thus one) and using the patterns
    """
    if num == 0:
        return 0
    else:
        return num % 9 if num % 9 != 0 else 9

if __name__ == '__main__':
    print("""
    For example:

    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
    """)

    print(add_digits(38))
