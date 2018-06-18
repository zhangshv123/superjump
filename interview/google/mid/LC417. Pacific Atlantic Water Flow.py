"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return []
        M, N = len(matrix), len(matrix[0])
        pacific = [[False for _ in range(N)] for _ in range(M)]
        atlantic = [[False for _ in range(N)] for _ in range(M)]
        def dfs(i, j, height, visited):
            if i < 0 or i >= M or j < 0 or j >= N or visited[i][j] or matrix[i][j] < height:
                return
            else:
                visited[i][j] = True
                for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    dfs(i + di, j + dj, matrix[i][j], visited)
        for i in range(M):
            dfs(i, 0, 0, pacific)
            dfs(i, N - 1, 0, atlantic)
        for j in range(N):
            dfs(0, j, 0, pacific)
            dfs(M - 1, j, 0, atlantic)
        res = []
        for i in range(M):
            for j in range(N):
                if pacific[i][j] and atlantic[i][j]:
                    res.append((i, j))
        return res