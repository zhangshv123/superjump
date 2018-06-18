#!/usr/bin/python
class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		if grid == None or len(grid) == 0 or len(grid[0]) == 0:
			return 0
		count = 0
		row, col = len(grid), len(grid[0])
		for i in range(row):
			for j in range(col):
				if grid[i][j] == '1':
					count += 1
					self.dfs(grid,i,j)
		return count
	
	def dfs(self,grid,i,j):
		row, col = len(grid), len(grid[0])
		if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] ！= '1':
			return
		grid[i][j] = '0'
		self.dfs(grid,i-1,j)
		self.dfs(grid,i,j-1)
		self.dfs(grid,i+1,j)
		self.dfs(grid,i,j+1)
