思路：如果可以开额外的空间将会很简单, 就是计算一下周围活的有几个, 然后设置一下次状态. 如果inplace的话也可以设置一个另外的标记, 就是如果原来是死的, 下一次活了, 就将其设置为2; 如果当前是活的下次死了, 那就设置为3. 最后在将2, 3的标记分别设为1, 0就可以了.
class Solution(object):
	def gameOfLife(self, board):
		directions = [(1,1),(-1,-1),(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,-1)]
		row, col = len(board), len(board[0])
		for i in range(row):
			for j in range(col):
				count = 0
				for d in directions:
					x,y = i + d[0], j+d[1]
					if x>= 0 and x<row and y>=0 and y<col and (board[x][y] == 1 or board[x][y] == 2):
						count += 1
				if (count < 2 or count > 3) and board[i][j] == 1:
					board[i][j] = 2
				elif count == 3 and board[i][j] == 0:
					board[i][j] = 3
					
		for i in range(row):
			for j in range(col):
				if board[i][j] == 2:
					board[i][j] = 0
				elif board[i][j] == 3:
					board[i][j] = 1
		return board

s = Solution()
print s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

dropbox follow up:
extra space+in place+ read 3 line，写完让口头跑case，然后问read 3line具体还能怎么优化，答可以改原game of life计算函数，改成只计算有效的那一行的定制版本……然后扯了一些分布式上的优化
楼主：
读3行算出来的只有中间一行的结果有效啊，另外两行的结果无效。
		
		
					
					 
		