思路：
traverse right and increment rowBegin, then traverse down and decrement colEnd, then I traverse left and decrement rowEnd, and finally I traverse up and increment colBegin.

The only tricky part is that when I traverse left or up I have to check whether the row or col still exists to prevent duplicates. If anyone can do the same thing without that check, please let me know!


class Solution(object):
	def spiralOrder(self, matrix):
		res = []
		if not matrix:
			return res
		rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix)-1, 0, len(matrix[0])-1
		while rowBegin <= rowEnd and colBegin <= colEnd:
			for i in range(colBegin, colEnd+1):
				res.append(matrix[rowBegin][i])
			rowBegin += 1
			
			for j in range(rowBegin, rowEnd+1):
				res.append(matrix[j][colEnd])
			colEnd -= 1
			
			if rowBegin <= rowEnd:
				for k in range(colEnd, colBegin-1, -1):
					res.append(matrix[rowEnd][k])
				rowEnd -= 1
			
			if colBegin <= colEnd:
				for n in range(rowEnd, rowBegin-1, -1):
					res.append(matrix[n][colBegin])
				colBegin += 1
		
		return res
		
s = Solution()
print s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
			
			
		