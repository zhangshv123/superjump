class Solution(object):
	def combinationSum(self, candidates, target):
		res = []
		candidates = sorted(candidates)
		self.dfs(candidates, 0, res, [], target)
		return res
	
	def dfs(self, candidates, idx, res, path, target):
		if target == 0:
			res.append(path[:])
			return
			
		for i in range(idx,len(candidates)):
			if candidates[i] <= target:
				path.append(candidates[i])
				self.dfs(candidates, i, res, path, target - candidates[i])
				path.pop()

s = Solution()
print s.combinationSum([2,3,5], 8)
print s.combinationSum([2,3,6,7], 7)