"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[sys.maxint for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
        return dp[m - 1][n - 1]