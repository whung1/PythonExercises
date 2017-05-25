"""
https://leetcode.com/problems/ransom-note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
from collections import Counter


def can_construct(ransom_note, magazine):
    c1 = Counter(ransom_note)
    c2 = Counter(magazine)

    c2.subtract(c1)
    for key, value in c2.items():
        if value < 0:
            return False
    return True

if __name__ == '__main__':
    print(can_construct('a', 'b'))
    print(can_construct('aa', 'ab'))
    print(can_construct('aa', 'aab'))

