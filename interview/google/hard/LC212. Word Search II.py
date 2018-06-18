#假设trie已经存在，dfs最好的模板
#时间复杂度从O(row*col*len(dictWords)4^max(len(dictWords[x]))到
#O(row*col*4^max(len(dictWords[x]))
def getValidWords(matrix, dictWords):
	row = len(matrix)
	col = len(matrix[0])
	

class TriNode(object):
	    def __init__(self):
		self.left = None
		self.right = None
		self.data = None
		self.isEnd = True
	 	
	
def getValidWords(matrix, dictWords):
	row = len(matrix)
	col = len(matrix[0])
	res = []
	visited = []
	
	for i in range(row):
		for j in range(col):
			if matrix[i][j] in trie.childs:
				dfs(matrix,i,j,trie.childs[matrix[i][j]], visited, res, [matrix[i][j]])
	return res
	
directions = [-1,0],[0,-1],[0,1],[1,0]

def dfs(matrix, x, y, trie, visited,res,path):
	for direction in directions:
		new_x = x + direction[0]
		new_y = y + direction[1]

		if new_x < 0 or new_y < 0 or new_x > len(matrix)-1 or new_y > len(matrix[0])-1: 
			continue
		if (new_x, new_y) in visited:
			continue
		if matrix[new_x, new_y] not in trie.childs:
			continue

		path.append(matrix[new_x, new_y])
		visited.append((x, y))

		dfs(matrix, new_x, new_y, trie.childs[matrix[new_x][new_y]], visited, res, path)

		visited.pop()
		path.pop()

朴素做法
时间复杂度
O(row*col*len(dictWords)4^max(len(dictWords[x]))
def getValidWords(matrix, dictWords):
	row = len(matrix)
	col = len(matrix[0])
	res = []
	visited = []
	
	
	for i in range(row):
		for j in range(col):
			for k in range(len(dictWords)):
				if matrix[i][j] == dictWords[k][0]:
					exist = dfs(matrix,i,j,dictWords[k],0, visited)
					if exist:
						res.append(dictWords[k])
	return res
	

def dfs(matrix, x, y, word, index, visited):
	if x < 0 or y < 0 or x > len(matrix)-1 or y > len(matrix[0])-1: 
		return False
		
	if index == len(word):
		return True
		
	if matrix[x][y] != word[index]:
		return False
	
	if (x,y) in visited:
		return False
	
	else:
		visited.append((x,y))
		directions = [-1,0],[0,-1],[0,1],[1,0]
		res = False
		for direction in directions:
			res = res or dfs(matrix, x+direction[0], y+direction[1], word, index+1,visited)
		visited.pop()
		return res
				
	
board =[
	['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']]
	
words = ["ABCCED", "SEE", "ABCB","ABC"]
print getValidWords(board, words)
	
	
						
	
			
				
	
	
