"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        fRow, fCol = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                fCol = True
        for j in range(n):
            if matrix[0][j] == 0:
                fRow = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0          
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0                   
        if fCol:
            for i in range(m): 
                matrix[i][0] = 0
        if fRow:
            for j in range(n): 
                matrix[0][j] = 0                
                    