#!/usr/bin/python
"""
***not familiar with trie node in python...

Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string containing 
    only letters a-z or .. A . means it can represent any one letter.

    For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
"""
from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        def dfs(cur, idx):
            if idx == len(word):
                return cur.isWord
            if word[idx] == ".":
                for child in cur.children.values():
                    if dfs(child, idx + 1):
                        return True
            elif word[idx] in cur.children:
                return dfs(cur.children[word[idx]], idx + 1)
            return False
        return dfs(cur, 0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)