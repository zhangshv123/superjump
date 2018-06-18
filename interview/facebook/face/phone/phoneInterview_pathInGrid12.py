"""
听口音应该是国人大哥，只有一道题，m*n matrix，每个坐标都有一个character，找到所有左上角到右下角的路径（只能向右向下走）
并打印，比如a->b->c。 第一遍 String dfs秒了。followup优化用stringbuilder，秒了。followup再次优化用char[]，
稍稍卡了几下（算index算的有点儿慢），大哥给了小提。剩下时间问问题。
>>>>>>> origin/master

"""
from collections import defaultdict
class Solution(object):
	def getPath(self, board):
		dp = defaultdict(list)
		dp[(0, 0)] = [[board[0][0]]]
		def walk(i, j):
			if (i, j) in dp:
				return dp[(i, j)]
			if i < 0 or j < 0:
				return []
			for l in walk(i - 1, j) + walk(i, j - 1):
#				这步把 [[1, 2]],[[1, 3]] 变成 [[1, 2], [1, 3]]
				dp[(i, j)].append(l + [board[i][j]])
			return dp[(i, j)]
		return walk(len(board) - 1, len(board[0]) - 1 )
s = Solution()
print s.getPath([[1,2],[3,4]])

#涵涵version
from collections import defaultdict
class Solution(object):
	def getPath(self, board):
		dp = defaultdict(list)
		dp[(0,0)] = [[board[0][0]]]
		m,n = len(board),len(board[0])
		return self.walk(m-1,n-1,board,dp)
		
	def walk(self,i,j,board,dp):
		if (i,j) in dp:
			return dp[(i,j)]
		if i < 0 or j < 0:
			return []
		for l in self.walk(i-1,j,board,dp)+self.walk(i, j-1, board, dp):
			dp[(i,j)].append(l+[board[i][j]])
			
		return dp[(i,j)]

s = Solution()
print s.getPath([[1,2],[3,4]])

			