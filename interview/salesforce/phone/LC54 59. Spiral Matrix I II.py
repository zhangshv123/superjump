"""
I
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in 
spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
Take the first row plus the spiral order of the rotated remaining matrix. Inefficient for large matrices, 
but here I got it accepted in 40 ms, one of the fastest Python submissions.
"""
# SOL1
def spiralOrder(self, matrix):
    ret = []
    while matrix:
        ret += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix:
            ret += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    return ret	

# SOL2 ***
def spiralOrder(self, matrix):
    res = []
    if not matrix:
        return []
    i,j,di,dj = 0,0,0,1
    m, n = len(matrix),len(matrix[0])
    for v in xrange(m * n):
        res.append(matrix[i][j])
        matrix[i][j] = ''
        if matrix[(i+di)%m][(j+dj)%n] == '':
            di, dj = dj, -di
        i += di
        j += dj
    return res 

"""
II
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

"""
Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. 
Make a right turn when the cell ahead is already non-zero.
"""
def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A        
