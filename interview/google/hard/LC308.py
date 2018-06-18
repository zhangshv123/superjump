class NumMatrix(object):
	sum_matrix = []
	matrix = []
	def __init__(self, matrix):
		"""
		initialize your data structure here.
		:type matrix: List[List[int]]
		"""
		for row in matrix:
			sum_temp, sum_row = 0, []
			for item in row:
				sum_temp += item
				sum_row.append(sum_temp)
			self.sum_matrix.append(sum_row)
		self.matrix = matrix
	def update(self, row, col, val):
		"""
		update the element at matrix[row,col] to val.
		:type row: int
		:type col: int
		:type val: int
		:rtype: void
		"""
		sum_row = self.sum_matrix[row]
		print val, self.matrix[row][col]
		for i in range(col, len(sum_row)):
			sum_row[i] += val - self.matrix[row][col]
		self.matrix[row][col] = val
	def sumRegion(self, row1, col1, row2, col2):
		"""
		sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
		:type row1: int
		:type col1: int
		:type row2: int
		:type col2: int
		:rtype: int
		"""
		sum_temp = 0
		for row in range(row1, row2 + 1):
			pre = self.sum_matrix[row][col1-1] if col1 > 0 else 0
			sum_temp += self.sum_matrix[row][col2] - pre
		return sum_temp
matrix = [
	[3, 0, 1, 4, 2],
	[5, 6, 3, 2, 1],
	[1, 2, 0, 1, 5],
	[4, 1, 0, 1, 7],
	[1, 0, 3, 0, 5]
]
s = NumMatrix(matrix)
#print s.sum_matrix
print s.sumRegion(2, 1, 4, 3)
s.update(3, 2, 2)
print s.sumRegion(2, 1, 4, 3)