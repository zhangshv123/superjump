#!/usr/bin/python
"""
****conor case need to think careful
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
import copy
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = map(lambda row: map(lambda item: int(item), row), matrix)
        length = max(max(dp[0]), max(map(lambda a: a[0], dp)))
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
                    length = max(length, dp[i][j])
        return length * length