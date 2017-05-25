"""
https://leetcode.com/problems/first-unique-character-in-a-string

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter


def first_uniq_char(s):
    """
    :type s: str
    :rtype: int
    """
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
    return -1

if __name__ == '__main__':
    print(first_uniq_char('leetcode'))
    print(first_uniq_char('loveleetcode'))


