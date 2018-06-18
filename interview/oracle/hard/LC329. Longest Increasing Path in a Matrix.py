"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
# PQ + DP

import heapq
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0:
            return 0
        h = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                heapq.heappush(h, (-matrix[i][j], (i, j)))
        mat = [[1 for _ in range(n)] for _ in range(m)]
        res = 1
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(h) > 0:
            val, (i, j) = heapq.heappop(h)
            for di, dj in direc:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if matrix[i][j] < matrix[ni][nj]:
                    mat[i][j] = max(mat[i][j], mat[ni][nj] + 1)
            res = max(res, mat[i][j])
        return res

# Memorization + dfs
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[i, j]
            res = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i + di < 0 or i + di >= M or j + dj < 0 or j + dj >= N:
                    continue
                if matrix[i][j] <= matrix[i + di][j + dj]:
                    continue
                res = max(res, dfs(i + di, j + dj) + 1)
            dp[i, j] = res
            return dp[i, j]
        return max(dfs(x, y) for x in range(M) for y in range(N))


def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))
