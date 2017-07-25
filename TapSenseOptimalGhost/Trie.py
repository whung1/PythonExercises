"""
Trie implementation
"""
from collections import deque


class TrieNode:
    def __init__(self, val=None, end_data=None):
        self.val = val
        self.end = end_data  # Metadata storage if required, signaling end
        self.children = dict()

    def add_child(self, child):
        self.children[child.name] = child


class Trie:
    def __init__(self):
        self.root = TrieNode('')
        self.cur = self.root

    def insert_words(self, words):
        for word in words:
            self.insert_word(word)

    def insert_word(self, word):
        cur = self.root
        for letter in word:
            if letter in cur.children.keys():
                cur = cur.children[letter]
            else:
                cur.add_child(TrieNode(letter))
                cur = cur.children[letter]
        # Insert complete word at the end to indicate end and
        # give access to word at end of traversal
        cur.data = word

    def search(self, word):
        """
        Checks if word is in the Trie, searching from the root of the Trie
        :param word: Word to try to find in Trie
        :return: True if in Trie, False otherwise
        """
        cur = self.root
        for letter in word:
            if letter not in cur.children.keys():
                return False
        if '_end' in cur:
            return True
        return False

    def traverse_to(self, suffix):
        """
        Traverses from current position of the Trie to ones of prefix
        :param suffix: The rest of letters to to traverse up to in the Trie
        :return: Current TrieNode the Trie is on
        """
        cur = self.cur
        for letter in suffix:
            if letter not in cur.children.keys():
                raise ValueError  # Assumption that suffix is in tree is False
            cur = cur.children[letter]
        self.cur = cur  # Update current node of Trie
        return self.cur

    def get_words(self):
        """
        Traverses a Trie from start to get all words possible in the Trie
        from its current position via BFS

        :param start: origin TrieNode
        :return: List of tuples of (word, distance) where
        word is a completed word in the Trie
                    sorted from least to greatest in distance
                    from current Trie position
        """
        queue = deque()
        words = []

        queue.append((self.cur, 0))
        while queue:
            cur, cur_step = queue.pop()
            if cur:
                if cur.data is not None:
                    words.append((cur.data, cur_step))
                for child in cur.children:
                    queue.append((child, cur_step + 1))
        return words