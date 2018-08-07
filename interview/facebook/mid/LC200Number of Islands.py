#!/usr/bin/python
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
"""
follow up 如果matrix非常大怎么办？
切成小片，一块块读，可能要考虑边界。
Matrix 很大时先切成小块，然后用union find

divide:划分成更小的块
conquer:块与块之间整合的时候，考虑抵消的情况
"""

# 时间复杂度： 4的单词长度次方

class Solution(object):
    def numIslands(self, grid):
        count = 0
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return count        
        row = len(grid)
        col = len(grid[0])
        flag = [["0" for i in range(len(grid[0]))] for j in range(len(grid))] #作为标记，为了不改变input grid

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and flag[i][j] == "0": #没有访问过，并且grid里面是土地
                    count += 1
                    self.dfs(i, j, grid, flag)
        return count
    
    
    def dfs(self, x, y, grid, flag):
        flag[x][y] = "1"
        if x >=1 and grid[x-1][y] == "1" and flag[x-1][y] == "0":
            self.dfs(x-1, y, grid, flag)
        if y >=1 and grid[x][y-1] == "1" and flag[x][y-1] == "0":
            self.dfs(x, y-1, grid, flag)
        if y+1 < len(grid[0]) and grid[x][y+1] == "1" and flag[x][y+1] == "0":
            self.dfs(x, y+1, grid, flag)
        if x+1 < len(grid) and grid[x+1][y] == "1" and flag[x+1][y] == "0":
            self.dfs(x+1, y, grid, flag)
        return


class Solution(object):
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        res = 0
        flag = [[0 for i in range(col)] for j in range(row)] #作为标记，为了不改变input grid
        for i in range(row):
            for j in range(col):
                if flag[i][j] == 0 and grid[i][j] == "1": #没有访问过，并且grid里面是土地
                    self.helper(i,j,grid,flag)
                    res += 1
        return res
    
    def helper(self,i,j,grid,flag): # grid should never change
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):   # out-liner 越界
            return
        if flag[i][j] == 1: #回头，访问过的
            return 
        if grid[i][j] == "0": #不是土地
            return
            
        # enter into a non-visited land 
        flag[i][j] = 1
        self.helper(i-1,j,grid,flag)
        self.helper(i,j-1,grid,flag)
        self.helper(i+1,j,grid,flag)
        self.helper(i,j+1,grid,flag)

#BFS
import sets
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        s, q, num = set(), deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    s.add((i, j))
        while len(s) > 0:
            ele = s.pop()
            s.add(ele)
            q.append(ele)
            num += 1
            while len(q) > 0:
                i, j = q.popleft()
                if i < 0  or i >= m or j < 0 or j >= n:
                    continue
                if (i, j) not in s:
                    continue
                s.remove((i, j))
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    q.append((i + di, j + dj))
        return num

# FB面试改进：
# 输出每个岛的面积
class Solution(object):
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return count        
        row = len(grid)
        col = len(grid[0])
        flag = [["0" for i in range(len(grid[0]))] for j in range(len(grid))]
        res = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and flag[i][j] == "0":
                    path = [1]
                    self.dfs(i, j, grid, flag, res, path)
                    res.append(len(path))
        return res
    
    
    def dfs(self, x, y, grid, flag, res, path):
        flag[x][y] = "1"
        if x >=1 and grid[x-1][y] == "1" and flag[x-1][y] == "0":
            path.append("1")
            self.dfs(x-1, y, grid, flag, res, path)
        if y >=1 and grid[x][y-1] == "1" and flag[x][y-1] == "0":
            path.append("1")
            self.dfs(x, y-1, grid, flag, res, path)
        if y+1 < len(grid[0]) and grid[x][y+1] == "1" and flag[x][y+1] == "0":
            path.append("1")
            self.dfs(x, y+1, grid, flag, res, path)
        if x+1 < len(grid) and grid[x+1][y] == "1" and flag[x+1][y] == "0":
            path.append("1")
            self.dfs(x+1, y, grid, flag, res, path)
        return
s = Solution()
print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])
#别的版本
class Solution(object):
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        curr = 0
        flag = [[0 for i in range(col)] for j in range(row)] 
        area_idx = 0
        area = []
        for i in range(row):
            for j in range(col):
                if flag[i][j] == 0 and grid[i][j] == "1": 
                    area.append(0)
                    self.helper(i,j,grid,flag,area, area_idx)
                    area_idx += 1
        return area
    
    def helper(self,i,j,grid,flag,area,area_idx): # grid should nver change
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):  
            return
        if flag[i][j] == 1:
            return 
        if grid[i][j] == "0": 
            return
        
        # enter into a non-visited land 
        flag[i][j] = 1
        area[area_idx] += 1
        self.helper(i-1,j,grid,flag,area,area_idx)
        self.helper(i,j-1,grid,flag,area,area_idx)
        self.helper(i+1,j,grid,flag,area,area_idx)
        self.helper(i,j+1,grid,flag,area,area_idx)
s = Solution()
print s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

          