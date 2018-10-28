找到一个矩阵里面的最大X，好像面经有，比如
以下是1
1
以下是2
1 0 1
0 1 0
1 0 1. 
以下是3
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
大致想法就是遍历每个元素，算四个方向，取最小值是边长，然后找到最大的，follow up是如何加快，可以每次把一个斜边的算完以后存起来，以后要是发现左上和右上已经算过了，就可以直接用了
1.brute force的方法：
	就是遍历matrix里面的每个1，然后4个方向去找长度，最后取4个方向里面最短的作为结果，然后res取所有里面最长的即可
2.用dp优化：
4个方向我们称为0，1，2，3（顺时针的）
第一排的元素，0，1方向都必定为0，然后while循环算出2，3方向的长度，存到dp[0][j][2]和dp[0][j][3]里面
剩下非第一排的元素，都可以根据左上和右上的元素来确定

时间复杂度0 N^2

dp写法：
class Solution:
	def findBiggestX(self, matrix):
		row, col = len(matrix), len(matrix[0])
		dp = [[[0 for _ in range(4)] for _ in range(col)] for _ in range(row)]
		res = 0
		for j in range(col):
			if matrix[0][j] == 1:
				res = 1
				dp[0][j][0] = 0 #0，1方向都必定为0
				dp[0][j][1] = 0
				count2 = 0 #这里开始算第二方向
				startX, startY = 0, j
				while startX + 1 < len(matrix) and startY - 1 >= 0:
					count2 += 1
					startX += 1
					startY -= 1
				dp[0][j][2] = count2
				count3 = 0 #这里开始算第三方向
				startX, startY = 0, j
				while startX + 1 < len(matrix) and startY + 1 < len(matrix[0]):
					count3 += 1
					startX += 1
					startY += 1
				dp[0][j][3] = count3
		for i in range(1, row):
			for j in range(col):
				tmp = 0
				if matrix[i][j] == 1:
					if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == 1:
						dp[i][j][0] = dp[i-1][j-1][0]+1
						tmp = dp[i][j][0]
					if i-1 >=0 and j+1 < len(matrix[0]) and matrix[i-1][j+1] == 1:
						dp[i][j][1] = dp[i-1][j+1][1]+1
						tmp = min(tmp,dp[i][j][1])
					if i-1 >=0 and j+1 < len(matrix[0]) and matrix[i-1][j+1] == 1:
						dp[i][j][2] = dp[i-1][j+1][2]-1
						tmp = min(tmp,dp[i][j][2])
					if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == 1:
						dp[i][j][3] = dp[i-1][j-1][3]-1
						tmp = min(tmp,dp[i][j][3])
				res = max(res,tmp+1)
		return res

s = Solution()
print s.findBiggestX([[0]])
print s.findBiggestX([[1]])
print s.findBiggestX([[1, 0, 1],[0, 1, 0],[1, 0, 1]])
print s.findBiggestX([[1, 0, 1],[0, 0, 0],[1, 0, 1]])
print s.findBiggestX([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]])


brute-force的写法：
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