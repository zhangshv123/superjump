#!/usr/bin/python
"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
    0  -1 INF INF
After running your function, the 2D grid should be:
    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4
"""
"""
top bfs
"""
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while len(q) > 0:
            i, j = q.pop()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj, ndis = i + di, j + dj, rooms[i][j] + 1
                if ni >=0 and ni < len(rooms) and nj >= 0 and nj < len(rooms[0]):
                    if rooms[ni][nj] > ndis:
                        rooms[ni][nj] = ndis
                        q.append((ni, nj))

"""
naive dfs
"""
class Solution(object):
    def dfs(self, rooms, i, j, target):
        # boundary
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return
        # mark not go back at first enter or not need update
        if target != 0 and rooms[i][j] <= target:
            return
        rooms[i][j] = target
        self.dfs(rooms, i - 1, j, target + 1)
        self.dfs(rooms, i + 1, j, target + 1)
        self.dfs(rooms, i, j - 1, target + 1)
        self.dfs(rooms, i, j + 1, target + 1)
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)