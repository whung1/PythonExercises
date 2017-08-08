"""
Trie implementation
"""
from collections import deque


class TrieNode:
    def __init__(self, val=None, end_data=None):
        self.val = val  # Data of this node
        self.end = end_data  # Metadata storage if required, signaling end
        self.children = dict()

    def add_child(self, child):
        self.children[child.val] = child

    def get_children(self):
        return [node for node in self.children.values()]


class Trie:
    def __init__(self):
        self.root = TrieNode('', 0)
        self.cur = self.root  # Current position in the Trie

    def insert_word(self, word, prune=False):
        """
        Inserts a word into the Trie.
        :param prune: if True, ends the insert if a prefix of a word
                        is already a completed word
        """
        cur = self.root
        for letter in word:
            if letter in cur.children.keys():
                cur = cur.children[letter]
            else:
                if prune is True and cur.end:
                    return  # Stop early if prefix is in the tree
                cur.add_child(TrieNode(letter))
                cur = cur.children[letter]
        # Insert complete word at the end to indicate end and
        # give access to word at end of traversal
        cur.end = word

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

    def traverse_to(self, prefix):
        """
        Traverses from current position of the Trie to ones of prefix
        :param prefix: The rest of letters to to traverse up to in the Trie
        :return: Current TrieNode the Trie is on
        """
        cur = self.cur
        for letter in prefix:
            if letter not in cur.children.keys():
                # Assumption that prefix is in tree is False
                raise ValueError
            cur = cur.children[letter]
        self.cur = cur  # Update current node of Trie
        return self.cur

    def get_words(self):
        """
        Traverses a Trie from start to get all words possible in the Trie
        from its current position (self.cur) via BFS

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
                if cur.end is not None:
                    words.append((cur, cur_step))
                for child in cur.children.values():
                    queue.append((child, cur_step + 1))
        return words

    # Wrapper functions to hide local variables
    def get_next_nodes(self):
        """
        Return the children nodes of current node in tree
        :return:
        """
        return self.cur.get_children()

    def get_next_values(self):
        """
        Gets the current node's children values
        :return:
        """
        return [letter for letter in self.cur.children.keys()]

    def reset(self):
        """
        Resets the current position of the Trie back to the root
        :return:
        """
        self.cur = self.root

    def is_leaf(self):
        """
        :return: True if current node is leaf node, False otherwise
        """
        return True if not self.cur.children and self.cur.end else False
