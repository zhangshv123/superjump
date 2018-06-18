# space:O(nm * 3^k) 因为除了第一个，其他都是3个方向的
class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		row = len(board)
		col = len(board[0])
		for i in range(row):
			for j in range(col):
				if board[i][j] == word[0]:
					if self.helper(i,j,0,word,board):
						return True
		return False
		
	def helper(self,x,y,start,word,board):
		row = len(board)
		col = len(board[0])
		if start >= len(word):
			return True
		if x>=row or x<0 or y>=col or y<0:
			return False
		if board[x][y] == word[start]:
			start+=1
			board[x][y] = "#"
			res = self.helper(x-1,y,start,word,board) or self.helper(x,y-1,start,word,board) or self.helper(x+1,y,start,word,board) or self.helper(x,y+1,start,word,board)
			board[x][y] = word[start-1]
			return res
		return False
		
s = Solution()
board = [["ab"]]
print s.exist(board,"ba")