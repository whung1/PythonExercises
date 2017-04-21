"""
https://leetcode.com/problems/reverse-words-in-a-string-iii

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    new_str = []
    sep = " "
    for string in s.split(sep):
        new_str.append(string[::-1])  # Note that append is much faster than overloaded += (which is same as extend)
    return sep.join(new_str)

if __name__ == "__main__":
    descript = """
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    """
    print(descript)

    print(reverseWords('Let\'s take LeetCode contest'))
