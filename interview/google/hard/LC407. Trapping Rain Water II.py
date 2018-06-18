"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""
import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if heightMap is None or len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        h = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(n):
            heapq.heappush(h, (heightMap[0][i], 0, i))
            visited[0][i] = True
            heapq.heappush(h, (heightMap[m - 1][i], m - 1, i))
            visited[m - 1][i] = True
        for i in range(1, m - 1):
            heapq.heappush(h, (heightMap[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(h, (heightMap[i][n - 1], i, n - 1))
            visited[i][n - 1] = True
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        trap_water = 0
        while len(h) > 0:
            height, i, j = heapq.heappop(h)
            for di, dj in direc:
                ni, nj = i + di, j + dj
                #boarder check
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                #visit check
                if visited[ni][nj]:
                    continue
                visited[ni][nj] = True
                if height > heightMap[ni][nj]:
                    trap_water += height - heightMap[ni][nj]
                heapq.heappush(h, (max(height, heightMap[ni][nj]), ni, nj))
        return trap_water
        