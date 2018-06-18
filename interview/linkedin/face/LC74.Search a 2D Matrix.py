class Solution(object):
    def get(self, k, matrix):
        n = len(matrix[0])
        i, j = k / n, k % n
        return matrix[i][j]
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i, j = 0, len(matrix) * len(matrix[0]) - 1
        while i <= j:
            m = i + (j - i) / 2
            val = self.get(m, matrix)
            if val == target:
                return True
            elif val < target:
                i = m + 1
            else:
                j = m - 1
        return False