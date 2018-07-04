矩阵[[1,2,3],[4,5,6],[7,8,9]]
输出 [[1],[2,4],[3,5,7],[6,8],[9]]和[[7],[4,8],[1,5,9],[2,6],[3]] 类似LC498不过更简单
from collections import deque
class Solution(object):
	def findDiagonalOrder(self, matrix):
		res = []
		row, col = len(matrix), len(matrix[0])
		q = deque()
		q.append((0,0))
		while len(q) > 0:
			layer = []
			size = len(q)
			for i in range(size):
				cur = q.popleft()
				layer.append(cur)
				next1 = (cur[0]+1, cur[1])
				next2 = (cur[0], cur[1]+1)
				if next1[0] >= 0 and next1[0] <= row - 1 and next1[1] >= 0 and next1[1] <= col - 1 and next1 not in q:
					q.append(next1)
				if next2[0] >= 0 and next2[0] <= row - 1 and next2[1] >= 0 and next2[1] <= col - 1 and next2 not in q:
					q.append(next2)
			tmp = []
			for idx in reversed(layer):
				tmp.append(matrix[idx[0]][idx[1]])
			res.append(tmp)
		
		return res
		
s = Solution()
print s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
print s.findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
				
					
					 