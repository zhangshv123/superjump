"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
这道题让我们求一个二维区域和的检索，是之前那道题Range Sum Query - Immutable 区域和检索的延伸。
有了之前那道题的基础，我们知道这道题其实也是换汤不换药，还是要建立一个累计区域和的数组，
然后根据边界值的加减法来快速求出给定区域之和。这里我们维护一个二维数组dp，
其中dp[i][j]表示累计区间(0, 0)到(i, j)这个矩形区间所有的数字之和，
那么此时如果我们想要快速求出(r1, c1)到(r2, c2)的矩形区间时，
只需dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1]即可，
下面的代码中我们由于用了辅助列和辅助行，所以下标会有些变化
"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) > 0 and len(matrix[0]) > 0:  
            m, n = len(matrix), len(matrix[0])
            sums = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    sums[i][j] += matrix[i][j]
                    sums[i][j] += sums[i][j - 1] if j > 0 else 0
                    sums[i][j] += sums[i - 1][j] if i > 0 else 0
                    sums[i][j] -= sums[i - 1][j - 1] if i > 0 and j > 0 else 0
            self.sums = sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sums, res = self.sums, 0
        
        res += sums[row2][col2]
        res += sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        res -= sums[row2][col1 - 1] if col1 > 0 else 0
        res -= sums[row1 - 1][col2] if row1 > 0 else 0
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)