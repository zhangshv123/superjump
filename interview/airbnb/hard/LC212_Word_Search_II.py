"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
"""
"""
如果还按照DFS回溯的方法，逐个检查每个word是否在board里，显然效率是比较低的。我们可以利用Trie数据结构，
也就是前缀树。然后dfs时，如果当前形成的单词不在Trie里，就没必要继续dfs下去了。如果当前字符串在trie里，
就说明board可以形成这个word。
"""

import sets
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False
        
class Solution(object): 
    def buildTrie(self, words):
        """
        :type board: List[str]
        :rtype:TrieNode
        """
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isWord = True
        return root
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.buildTrie(words)
        res = set()
        lboard = [ list(row) for row in board]
        visited = [[False for _ in range(len(row))] for row in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.searchWords(i, j, "", lboard, root, res, visited)
        return list(res)
    def searchWords(self, i, j, word, board, node, res, visited):
        #base
        if node.isWord:
            res.add(word)
        #recursion
        if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and not visited[i][j] and board[i][j] in node.children:
            visited[i][j] = True
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self.searchWords(i + dir[0], j + dir[1], word + board[i][j], board, node.children[board[i][j]], res, visited)
            visited[i][j] = False