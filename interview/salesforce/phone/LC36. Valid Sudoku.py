"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution(object):
    def validate(self, arr):
        s = set()
        for a in arr:
            if a != ".":
                if a in s:
                    return False
                s.add(a)
        return True
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for i in range(len(board)):
            if not self.validate(board[i]):
                return False
        # check col
        for j in range(len(board[0])):
            arr = []
            for i in range(len(board)):
                arr.append(board[i][j])
            if not self.validate(arr):
                return False
        # check smal box
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not self.validate(board[i][j: j + 3] + board[i + 1][j: j + 3] + board[i + 2][j: j + 3]):
                    return False
        return True
                