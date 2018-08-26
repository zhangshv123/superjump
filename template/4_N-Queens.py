#!/usr/bin/python
class Solution(object):
	def solveNQueens(self, n):
		res = []
		self.dfs(0, n, [], res)
		return res
	
	def dfs(self, row, n, path, res):
		if len(path) == n:
			res.append(path[:])
			return
			
		for j in range(n):
			if isValid(path, row, j): #合理才会放进去 
				path.append((row,j))
				self.dfs(row+1, n, path, res)
				path.pop()
	
	def isValid(self, row, col, path): #行不用检查，只需要检查之前行的同列
		for point in path:
			if point[1] == col:
				return False
			if abs(row - point[0]) == abs(col - point[1]): #检查斜线
				return False
		return True
			
			
			
		
