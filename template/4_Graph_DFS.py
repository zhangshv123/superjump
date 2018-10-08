"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
"""
"""
如果还按照DFS回溯的方法，逐个检查每个word是否在board里，显然效率是比较低的。我们可以利用Trie数据结构，
也就是前缀树。然后dfs时，如果当前形成的单词不在Trie里，就没必要继续dfs下去了。如果当前字符串在trie里，
就说明board可以形成这个word。
"""
#假设trie已经存在，dfs最好的模板
#时间复杂度从O(row*col*len(dictWords)4^max(len(dictWords[x]))到
#O(row*col*4^max(len(dictWords[x]))
import sets
class TrieNode(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = {}
		self.isWord = False
		
class Solution(object): 
	def buildTrie(self, words):
		"""
		:type board: List[str]
		:rtype:TrieNode
		"""
		root = TrieNode()
		for word in words:
			node = root
			for c in word:
				if c not in node.children:
					node.children[c] = TrieNode()
				node = node.children[c]
			node.isWord = True
		return root
	def findWords(self, matrix, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		root = self.buildTrie(words)
		row = len(matrix)
		col = len(matrix[0])
		res = []
		visited = set()
		
		for i in range(row):
			for j in range(col):
				if matrix[i][j] in root.children:
					visited.add((i,j))
					self.dfs(matrix,i, j, root.children[matrix[i][j]], visited, res, matrix[i][j])
					visited.pop()
		return list(set(res))

	
	def dfs(self,matrix, x, y, trie, visited, res, path): #find the next point from (x,y) to match this trie node
		if trie.isWord:
			res.append(path[:]) #即使找到了还可以继续找下去，所以没有return
		directions = [-1,0],[0,-1],[0,1],[1,0]
		for direction in directions:
			new_x = x + direction[0]
			new_y = y + direction[1]

			if new_x < 0 or new_y < 0 or new_x > len(matrix)-1 or new_y > len(matrix[0])-1: 
				continue
			if (new_x, new_y) in visited:
				continue
			if matrix[new_x][new_y] not in trie.children:
				continue

			path = path + (matrix[new_x][new_y])
			visited.add((new_x, new_y))

			self.dfs(matrix, new_x, new_y, trie.children[matrix[new_x][new_y]], visited, res, path)

			visited.remove((new_x, new_y)) #注意这里不能用pop!hashtable和set只有add, remove. stack, queue只有push和pop!
			path = path[:-1]
					
	
board =[
	['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']]
	
words = ["ABCCED", "SEE", "ABCB","ABC"]
s = Solution()
print s.findWords(board, words)
	
	
						
	
			
				
	
	
