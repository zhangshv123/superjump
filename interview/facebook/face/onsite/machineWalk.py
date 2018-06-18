"""
两周多前FB onsite.最后一轮coding.被问了一道没见过的题（可能是我做的题少所以没见过）,跟大家分享一下。
题目是给你一个机器人和一个房间，你并不知道机器人在房间什么位置，你也不知道房间的形状大小，你有一个遥控器，
可以让机器人走前后左右四个方向。这里给你一个move method : boolean move(int direction), direction: 0,1,2,3 
表示四个方向。能移动就返回true,不能移动表示false。问你：这个房间多大。
"""
#!/usr/bin/python
class Robot(object):
	def __init__(self, board):
		self.board = board
		self.i = 0
		self.j = 0
		self.dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
	def set(self, i, j):
		self.i, self.j = i, j
	def move(self, i):
		di, dj = self.dir[i]
		ni, nj = self.i + di, self.j + dj
		if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0]):
			return False
		if board[ni][nj] == "0":
			return False		
		print (self.i, self.j), "-->", (ni, nj)	
		self.i = ni
		self.j = nj
		return True

class Solution(object):
	def maxArea(self, i, j, robot):
		robot.set(i, j)
		s = set()
		move_back = {0: 1, 1: 0, 2: 3,3: 2}
		def helper(i, j):
			if (i, j) in s:
				return
			s.add((i, j))
			for i, (di, dj) in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]):
				if robot.move(i):
					helper(i + di, j + dj)
					robot.move(move_back[i])
		helper(i, j)
		for i, j in s:
			print (i, j), robot.board[i][j]
		print s
		return len(s)

		
s = Solution()
board = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
r = Robot(board)
print s.maxArea(0, 0, r)


"""
一个机器人 不规则房间  房间有障碍物, 能够上下左右, 求机器人能走到的全部区域面积
0 是障碍物
"""
from collections import deque
class Solution(object):
	def maxArea(self, i, j, board):
		q = deque()
		s = set()
		if board[i][j] == "1":
			q.append((i, j))
			s.add((i, j))
		while len(q) > 0:
			i, j = q.popleft()
			for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
				ni, nj = di + i, dj + j
				if ni < 0 or ni >= len(board) or j < 0 or j > len(board[0]):
					continue
				if board[ni][nj] != "1":
					continue
				if (ni, nj) in s:
					continue
				q.append((ni, nj))
				s.add((ni, nj))
		return len(s)
s = Solution()
board = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print s.maxArea(0, 0, board)