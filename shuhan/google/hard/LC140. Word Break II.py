#!/usr/bin/python
#backtracking的版本，理解的不好，要重写此题
class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		wordSet = set(wordDict)
		size = len(s) -1
		allResults = [None]*(size+1)
		self.helper(s,size,wordSet,allResults)
		return allResults[size]
	
	def helper(self,s,end,wordSet,allResults):
		if allResults[end] != None:
			return
		result = []
		
		if s[:end+1] in wordSet:
			result.append(s[:end+1])
		
		for p in range(1,end+1):
			if s[p:end+1] in wordSet:
				self.helper(s,p-1,wordSet,allResults)
				for preString in allResults[p-1]:
					result.append(preString + " " + s[p:end+1] )
		
		allResults[end] = result
		
#breakable的版本
	