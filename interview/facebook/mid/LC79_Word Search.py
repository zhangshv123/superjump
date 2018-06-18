#!/usr/bin/python
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def dfs(self, index, i, j, board, word):
        #boarder check
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        #word check
        if word[index] != board[i][j]:
            return False
        #base
        if index == len(word) - 1:
            return True
        #recursion
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            board[i][j] = "#"
            if self.dfs(index + 1, i + di, j + dj, board, word):
                return True
            board[i][j] = word[index]
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(0, i, j, board, word):
                    return True
        return False
            
class Solution(object):
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path, stk = [], []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    stk.append((i, j, 0))
        while len(stk) > 0:#这个while放在if里面和外面都一样！
            i, j, index = stk.pop()
            #boarder check
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                continue
            #word check
            if word[index] != board[i][j]:
                continue
            #check character
            if (i, j) in path[:index]:
                continue
            if len(path) <= index:
                path.append((i, j))
            else:
                path[index] = (i, j)
            #base
            if index == len(word) - 1:
                return True
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                stk.append((i + di, j + dj, index + 1))
        return False
            