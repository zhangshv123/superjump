找到一个矩阵里面的最大X，好像面经有，比如
以下是1
1
以下是2
1 0 1
0 1 0
1 0 1. 一亩-三分-地，独家发布
以下是3
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
大致想法就是遍历每个元素，算四个方向，取最小值是边长，然后找到最大的，follow up是如何加快，可以每次把一个斜边的算完以后存起来，以后要是发现左上和右上已经算过了，就可以直接用了
class Solution:
	def findBiggestX(self, matrix):
		row, col = len(matrix), len(matrix[0])
		res = 0
		for i in range(row):
			for j in range(col):
				if matrix[i][j] == 1:
					length = self.dfs(matrix, i, j)
					res = max(res, length+1)
		return res
	
	def dfs(self, matrix, x, y):
		upLeft, Upright, downLeft, downRight = 0, 0, 0, 0
		startX, startY = x, y
		while startX - 1 >=0 and startY - 1 >= 0:
			upLeft += 1
			startX -= 1
			startY -= 1
		startX, startY = x, y
		while startX - 1 >=0 and startY + 1 < len(matrix[0]):
			Upright += 1
			startX -= 1
			startY += 1
		startX, startY = x, y
		while startX + 1 < len(matrix) and startY - 1 >= 0:
			downLeft += 1
			startX += 1
			startY -= 1
		startX, startY = x, y
		while startX + 1 < len(matrix) and startY + 1 < len(matrix[0]):
			downRight += 1
			startX += 1
			startY += 1
		if upLeft!= 0 and Upright != 0 and downLeft!= 0 and downRight != 0:
			return min(upLeft, Upright, downLeft, downRight)
		return 0

s = Solution()
print s.findBiggestX([[0]])
#print s.findBiggestX([[1, 0, 1],[0, 1, 0],[1, 0, 1]])
#print s.findBiggestX([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]])