#path 里面存的都是index
class Solution(object):
	def permuteUnique(self, l):
		l = sorted(l)
		res = []
		self.dfs(l, res, [])
		return res
	
	def dfs(self, l, res, path):
		if len(path) == len(l):
			tmp = []
			for idx in path:
				tmp.append(l[idx])
			res.append(tmp[:])
			return
	
		last = -1
		for i in range(len(l)):
			if i in path:
				continue
			if last != -1 and l[i] == l[last]:
				continue
			path.append(i)
			dfs(l, res, path)
			last = path[-1]
			path.pop()
