思路：
我们可以每个“INF”点做BFS，但是那样会超时，所以我们就需要用更巧妙的方法！
我们先找到所有0的位置，然后把这些点放进queue，然后从这些0开始向外找！
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return
        row = len(rooms)
        col = len(rooms[0])
        q = deque()
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while len(q) > 0:
            i,j = q.popleft()
            for dire in directions:
                new_x = i+dire[0] 
                new_y = j+dire[1]
                new_d = rooms[i][j]+1
                if new_x >= 0 and new_x < len(rooms) and new_y >= 0 and new_y < len(rooms[0]):
                    if rooms[new_x][new_y] > new_d:
                        rooms[new_x][new_y] = new_d
                        q.append((new_x,new_y))
        return

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