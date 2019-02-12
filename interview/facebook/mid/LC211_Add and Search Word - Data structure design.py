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
        

    def dfs(self, word, idx, node):
        if idx == len(word):
            return node.isWord
        if word[idx] in node.children: #这里一定需要return!不然就是空跑
            return self.dfs(word, idx+1, node.children[word[idx]])
        elif word[idx] == ".":
            for key in node.children.values():
                if self.dfs(word, idx+1, key):
                    return True
        return False
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)