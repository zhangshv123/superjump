思路：利用01bruteforce模板
对于每个字母0表示不取，1表示取，所有可能性存在res里面
然后再遍历这个res进行处理

class Solution(object):
	def generateAbbreviations(self, word):
		res = []
		total = []
		self.dfs(len(word),0,res, [],[0,1])
		for item in res:
			path = ""
			count = 0
			for i in range(len(item)):
				if item[i] == 0:
					count += 1
				else:
					if count > 0:
						path += str(count)
					path += word[i]
					count = 0
			if count > 0:
				path += str(count)
			total.append(path)
		return total
					
	def dfs(self, n, idx, res, path, possible):
		if idx == n:
			res.append(path[:])
			return
		
		for pos in possible:
			path.append(pos)
			self.dfs(n, idx+1, res, path, possible)
			path.pop()

s = Solution()
print s.generateAbbreviations("w")