from string import ascii_lowercase
from collections import defaultdict
class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		if endWord not in wordList:
			return []
		q, res = [], []
		idx = 0
		stop = False
		depth = 0
		q.append((beginWord, -1))
		while idx < len(q): # bfs by tree layer
			j = idx
			k = len(q)
			depth += 1
			idx = len(q)
			if depth >= len(wordList):
				return []
			for m in range(j, k):
				word, pre = q[m]
				for i in range(len(word)):
					for c in ascii_lowercase:
						new_word = word[:i] + c + word[i+1:]
						if new_word in wordList:
							q.append((new_word, m))
							if new_word == endWord:
								stop = True
								res.append(len(q)-1)
			if stop:
				break
				
		total = []
		for i in res:
			path = []
			cur = i
			while cur != -1:
				path.append(q[cur][0])
				cur = q[cur][1]
			total.append(path[::-1])					
		return total
			