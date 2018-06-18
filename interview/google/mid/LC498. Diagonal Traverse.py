"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
"""
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        res = []
        M, N = len(matrix), len(matrix[0])
        di, dj = -1, 1
        i, j = 0, 0
        while len(res) < M * N:
            res.append(matrix[i][j])
            i += di
            j += dj
            if i < 0 or i >= M or j < 0 or j >= N:
                di, dj = -di, -dj
            if j >= N:
                j = N - 1
                i += 2
            elif i >= M:   
                i = M - 1
                j += 2
            elif i < 0:
                i = 0
            elif j < 0:
                j = 0
        return res