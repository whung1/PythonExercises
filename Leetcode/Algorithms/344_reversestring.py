"""
https://leetcode.com/problems/reverse-string

Write a function that takes a string as input and returns the string reversed.
"""


def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]


if __name__ == "__main__":
    print("""
    Example:
        Given s = "hello", return "olleh".
    """)

    print(reverseString('hello'))
