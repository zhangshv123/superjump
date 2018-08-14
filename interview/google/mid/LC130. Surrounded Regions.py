#思路:
#	从边缘的0出发，标黑所有跟边缘0相关的点，只有这些点是不能变成X的，其余剩下的部分直接标X就好
class Solution(object):
	def solve(self, board):
		if len(board) == 0 or len(board[0]) == 0 or not board:
			return
		row = len(board)
		col = len(board[0])
		res = []
		for i in range(col):
			if board[0][i] == "O":
				self.dfs(board,0,i,res)
			if board[row-1][i] == "O":
				self.dfs(board,row-1,i,res)
		for j in range(row):
			if board[j][0] == "O":
				self.dfs(board,j,0,res)
			if board[j][col-1] == "O":
				self.dfs(board,j,col-1,res)
		for i in range(row):
			for j in range(col):
				if (i,j) not in res:
					board[i][j] = "X"
		return 
					
	
	def dfs(self, matrix, x, y, res):
		res.append((x,y))
		directions = [-1,0],[0,-1],[0,1],[1,0]
		for direction in directions:
			new_x = x + direction[0]
			new_y = y + direction[1]
			if new_x < 0 or new_y < 0 or new_x > len(matrix)-1 or new_y > len(matrix[0])-1: 
				continue
			if (new_x, new_y) in res:
				continue
			if matrix[new_x][new_y] != "O":
				continue
			self.dfs(matrix, new_x, new_y, res)

s = Solution()
#s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
print s.solve([["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]])
	
			

		
		
		


		