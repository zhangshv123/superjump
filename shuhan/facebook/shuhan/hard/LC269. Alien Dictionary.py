from collections import deque
from collections import defaultdict
class Solution(object):
	def getCmp(self, word1, word2, cmps):
		"""
		:return FALSE when error 
		:type word1: str
		:type word2: str
		:type cmps: set
		:rtype: boolean
		"""
		for i, c1 in enumerate(word1): #这个函数不会检测“xy 和yx”情况，因为最后一行做了
			if i >= len(word2): #"xyc 和 xy 这种提供不了任何信息"
				return False
			if c1 != word2[i]:
				cmps.add((c1, word2[i]))
				break
		return True
		
	
	def alienOrder(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""
		cmps = set()
		allChars = set()
		for i, word1 in enumerate(words):
			for c in word1:
				allChars.add(c) #把所有的char都放进去
			for word2 in words[i + 1:]:
				if not self.getCmp(word1, word2, cmps):
					return ""
		return "".join(self.tpsort(cmps, allChars))
		
	def tpsort(self, cmps, allChars):
		"""
		:type words: set[(char, char)]
		:rtype: list[char]
		"""
		dpenedMap = defaultdict(set)
		dpenNums = defaultdict(int)
		for cmp in cmps:
			dpenedMap[cmp[0]].add(cmp[1])
			if cmp[0] != cmp[1]:
				dpenNums[cmp[1]] += 1
		q = []
		for char in allChars:
			if dpenNums[char] == 0:
				q.append(char)
		index = 0
		while index < len(q):#BFS模板，保留q，所以用idx代替pop
			cur = q[index]
			index += 1
			for dpen in dpenedMap[cur]:
				dpenNums[dpen] -= 1
				if dpenNums[dpen] == 0:
					q.append(dpen)
		return q if len(allChars) == len(q) else [] #防止死锁
			
		
		

