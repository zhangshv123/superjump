"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        def liveCells(i, j):
            count = 0
            for di, dj in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= M or nj < 0 or nj >= N:
                    continue
                if board[ni][nj] not in [1, 2]:
                    continue
                count += 1
            return count
        for i in range(M):
            for j in range(N):
                if board[i][j] == 0:
                    if liveCells(i, j) == 3:
                        board[i][j] = 3
                if board[i][j] == 1:
                    if liveCells(i, j) not in [2, 3]:
                        board[i][j] = 2
        m = {0: 0, 1: 1, 2: 0, 3: 1}
        for i in range(M):
            for j in range(N):
                board[i][j] = m[board[i][j]]