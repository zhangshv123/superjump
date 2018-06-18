"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
# BFS
from collections import deque
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def isWall(i, j):
            if i < 0 or i >= len(maze):
                return True
            if j < 0 or j >= len(maze[0]):
                return True
            if maze[i][j] == 1:
                return True
            return False
        dirc = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        q = deque()
        q.append(start)
        while len(q) > 0:
            i, j= q.popleft()
            maze[i][j] = 2
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in dirc:
                ii, jj = i, j
                while not isWall(ii + di, jj + dj):
                    ii += di
                    jj += dj
                if maze[ii][jj] != 2:
                    q.append((ii, jj))
        return False
                
# DFS
class Solution(object):
    def hasPath(self, maze, start, destination):
        return self.helper(maze, destination, start[0], start[1])
        
    
    def helper(self, maze, dest, i, j):
        if [i, j] == dest:
            return True
        if maze[i][j] == 2:
            return False
        maze[i][j] = 2
        up, down, left, right = i, i, j, j
        while up > 0 and maze[up-1][j] != 1:
            up -= 1
        while down < len(maze)-1 and maze[down+1][j] != 1:
            down += 1
        while left > 0 and maze[i][left-1] != 1:
            left -= 1
        while right < len(maze[0])-1 and maze[i][right+1] != 1:
            right += 1
        return self.helper(maze, dest, up, j) or self.helper(maze, dest, down, j) or self.helper(maze, dest, i, left) or self.helper(maze, dest, i, right)

"""
find the shortest distance for the ball to stop at the destination. 
https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode
"""

import heapq
class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        M, N = len(maze), len(maze[0])
        def isWall(i, j):
            if i < 0 or i >= M or j < 0 or j >= N:
                return True
            if maze[i][j] == 1:
                return True
            return False
        q = [(0, start)]
        visited = {}
        while len(q) > 0:
            dis, (i, j) = heapq.heappop(q)
            if (i, j) in visited and dis >= visited[i, j]:
                continue # if cur is visited and with a shorter length, skip it.
            visited[i, j] = dis
            if i == destination[0] and j == destination[1]:
                return dis
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii, jj, d = i, j, 0
                while not isWall(ii + di, jj + dj):
                    ii += di
                    jj += dj
                    d += 1
                heapq.heappush(q, (dis + d, (ii, jj)))
        return -1      

        
"""
III
find out how the ball could drop into the hole by moving the shortest distance.
hole different than stop, it could be less restriction on the destination.
"""
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        def isWall(i, j):
            if i < 0 or i >= len(maze):
                return True
            if j < 0 or j >= len(maze[0]):
                return True
            if maze[i][j] == 1:
                return True
            return False
        dirc = [(0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u'), (1, 0, 'd')]
        visited={}
        q=[]
        dest=tuple(hole)
        heapq.heappush(q, (0, '', tuple(ball)))
        while q:
            length, path, cur = heapq.heappop(q)
            if cur in visited and visited[cur]<=length:
                continue # if cur is visited and with a shorter length, skip it.
            visited[cur] = length
            if cur == dest:
                return path
            for di, dj, dr in dirc:
                ii, jj = cur
                ll = length
                while not isWall(ii + di, jj + dj):
                    ii += di
                    jj += dj
                    ll += 1
                    # hole different than stop, it does not need to be at stop place
                    if (ii, jj) == dest:
                        break
                heapq.heappush(q, (ll, path + dr, (ii, jj)))
        return "impossible"