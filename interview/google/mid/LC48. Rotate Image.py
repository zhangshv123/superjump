思路：
先按照对角线交换值, matrix[x][y]和matrix[y][x]
然后再同一行左右交换！
class Solution(object):
	def rotate(self, matrix):
		n = len(matrix)
		for x in range(n):
			for y in range(x):
				matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
		
		for x in range(n):
			l,r = 0, n-1
			while l < r:
				matrix[x][l], matrix[x][r] = matrix[x][r], matrix[x][l]
				l += 1
				r -= 1
		for i in range(n): #注意这里尽量写成这样！
			for j in range(n):
				print str(matrix[i][j]) + " ", #这里逗号表示不要换行
			print #print是自动换行的
		return

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])

