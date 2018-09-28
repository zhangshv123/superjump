class Solution(object):
	def combinationSum2(self, candidates, target):
		res = []
		candidates.sort() #必须先排序了！
		self.dfs(candidates,0, [], res, target)
		return res
	
	def dfs(self, candidates, idx, path, res, target):
		if target == 0:
			new_temp = []
			for idx in path: #path 存的是idx而不是数
				new_temp.append(candidates[idx])
			res.append(new_temp[:])
			return
		
		if target < 0:
			return
		
		for i in range(idx, len(candidates)):
			if i >= 1 and candidates[i] == candidates[i-1] and i-1 not in path: #和39不同就是这个！参照permutation模板
						continue
			path.append(i)
			self.dfs(candidates, i+1, path, res, target-candidates[i])
			path.pop()

s = Solution()
print s.combinationSum([2,5,2,1,2], 5)