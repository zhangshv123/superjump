#!/usr/bin/python
class Solution:
	d = {'2':['a','b','c'],
		 '3':['d','e','f'],
		 '4':['g','h','i'],
		 '5':['j','k','l'],
		 '6':['m','n','o'],
		 '7':['p','q','r','s'],
		 '8':['t','u','v'],
		 '9':['w','x','y','z']
		}
	def letterCombinations(self, digits):
		res = []
		length = len(digits)
		if length == 0:
			return res
		self.dfs(0, "", res, digits)
		return res

	def dfs(self, idx, tmp, res, digits):
			if idx == len(digits):
				res.append(tmp)
				return
			for letter in self.d[digits[idx]]:
					self.dfs(idx+1, tmp+letter, res, digits)
					
s = Solution()
print s.letterCombinations("23")

