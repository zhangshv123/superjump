# 时间复杂度 O(nm)  n= wordlist的长度，m是最长的单词的长度
from collections import deque
from string import ascii_lowercase
class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		q = deque()
		q.append(beginWord)
		visited = set() #图特殊需要的，因为可能有环
		visited.add(beginWord)
		res = 1
		if endWord not in wordList:
			return 0
		while len(q) > 0:
			size = len(q)
			res += 1
			for i in range(size):
				cur = q.popleft()
				for i in range(len(cur)):
					for c in ascii_lowercase: 
						new = cur[:i] + c + cur[i+1:]
						if new == endWord:
							return res
						elif new in wordList and new not in visited:
							q.append(new)
							visited.add(new)
		return 0