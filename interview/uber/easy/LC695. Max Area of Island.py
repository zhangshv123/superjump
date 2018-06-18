"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
"""
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        M, N = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                area += dfs(i + di, j + dj)
            return area
        maxArea = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i, j), maxArea)    
        return maxArea