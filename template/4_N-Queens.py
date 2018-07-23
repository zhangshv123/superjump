#!/usr/bin/python
class Solution(object):
	def solveNQueens(self, n):
		res = []
		self.dfs(n,res,[],0)
		return res
	
	def dfs(self, n, res, path, row):
		if len(path) == n:
			res.append(path[:])
			return
			
		for i in range(n):
			if isValid(path,row,i): #合理才会放进去 
				path.append((row,i))
				self.dfs(n, res, path, row+1)
				path.pop()

			
			
			
		
