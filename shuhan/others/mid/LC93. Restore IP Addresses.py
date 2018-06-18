#最简单的recursion
class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		res= []
		self.helper(res,[],0,4,12,s)
		return res
	
	def helper(self,res,path,start,minSize,maxSize,s):
		if len(s) - start >= minSize and len(s) - start <= maxSize:
			if minSize == 0 and maxSize == 0:
				res.append(".".join(path))

			for i in range(start,len(s)):
				if i != start and s[start] == "0":
					break
				if int(s[start:i+1]) > 255:
					break
				path.append(s[start:i+1])
				self.helper(res,path,i+1,minSize - 1, maxSize - 3,s)
				path.pop()
		
"""
使用stack来做dfs，固定高度
"""
class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		res,stack = [],[]
		path = []
		stack.append(("",0,4,12,0))
		while len(stack) > 0:
			word,start,minSize,maxSize,height = stack.pop()
			if len(s) - start >= minSize and len(s) - start <= maxSize:
				if len(path) <= height:
					path.append(word)
				else:
					path[height] = word
				#base
				if minSize == 0 and maxSize == 0:
					res.append(".".join(path[1:]))
				
				for i in range(start,len(s)):
					if i != start and s[start] == "0":
						break
					if int(s[start:i+1]) > 255:
						break
					stack.append((s[start:i+1],i+1,minSize - 1, maxSize - 3,height+1))
		return res	
#bfs来做
from collections import deque
class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		res,queue = [], deque() 
		
		queue.append(("",0,4,12))
		
		while len(queue) > 0:
			path,start,minSize,maxSize = queue.popleft()
			if len(s) - start >= minSize and len(s) - start <= maxSize:
				#base
				if minSize == 0:
					res.append(path)
				for i in range(start,len(s)):
					 #"025"
					if i != start and s[start] == "0":
						break
					#"552"
					if int(s[start: i + 1]) > 255:
						break
					newPath = s[start: i + 1] if len(path) == 0 else path+"."+s[start:i+1]
					queue.append((newPath, i + 1, minSize - 1, maxSize - 3))
		return res
		
