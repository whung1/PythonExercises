"""
https://leetcode.com/problems/keyboard-row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Note:
    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""
import re

def find_words_sets(words):
        """
        Using Sets to match words at the cost of higher space complexity but improved readability.
        
        Remember that we use sets instead of unordered hashtables/dicts here because the value doesnt matter
        and order does not matter thus no lists
        :type words: List[str]
        :rtype: List[str]
        """

        row_1 = set('qwertyuiop')
        row_2 = set('asdfghjkl')
        row_3 = set('zxcvbnm')
        same_row_words = []  # Return list

        for word in words:
            current = set(word.lower())
            if current.issubset(row_1) or current.issubset(row_2) or current.issubset(row_3):
                same_row_words.append(word)
        return same_row_words


def find_words_regex(words):
    """
    Using regular expressions to match words for less space complexity than sets
    :type words: List[str]
    :rtype: List[str]
    """

    # Using + here to not put in empty strings, ^=start, $=end, re.I = ignorecase
    keyboard = re.compile('^([qwertyuiop]+|[asdfghjkl]+|[zxcvbnm]+)$', re.I)
    same_row_words = []  # Return list

    for word in words:
        if keyboard.match(word):
            same_row_words.append(word)
    return same_row_words

if __name__ == "__main__":
    print("""
    Example 1:
        Input: ["Hello", "Alaska", "Dad", "Peace"]
        Output: ["Alaska", "Dad"]
    """)

    print(find_words_sets(["Hello", "Alaska", "Dad", "Peace"]))
    print(find_words_regex(["Hello", "Alaska", "Dad", "Peace"]))
