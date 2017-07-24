"""
Trie implementation
"""
from collections import deque


class TrieNode:
    def __init__(self, val=None, end_data=None):
        self.val = val
        self.end = end_data  # Metadata storage if required at the end of a Trie
        self.children = dict()

    def add_child(self, child):
        self.children[child.name] = child


class Trie:
    def __init__(self):
        self.root = TrieNode('')

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
        cur.data = word  # Insert complete word at the end to indicate end and give access to word at end of traversal

    def search(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children.keys():
                return False
        if '_end' in cur:
            return True
        return False

    @staticmethod
    def traverse_to(start, prefix):
        if start is None or not isinstance(start, TrieNode):
            raise ValueError  # Assumption that start is a valid Trie is false
        cur = start
        for letter in prefix:
            if letter not in cur.children.keys():
                raise ValueError  # Assumption that prefix is in tree is False
            cur = cur.children[letter]
        return cur

    @staticmethod
    def get_words(start):
        """
        Traverses a Trie from start to get all words possible in the Trie
        via BFS and returns them sorted by length
        :param start: origin TrieNode
        :return:
        """
        if start is None or not isinstance(start, TrieNode):
            raise ValueError  # Assumption that start is a valid Trie is false

        queue = deque()
        words = []

        queue.append((start, 0))
        while queue:
            cur, cur_step = queue.pop()
            if cur:
                if cur.data is not None:
                    words.append((cur.data, cur_step))
                for child in cur.children:
                    queue.append((child, cur_step + 1))
        return words

