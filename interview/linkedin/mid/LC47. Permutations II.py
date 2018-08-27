#path 里面存的都是index
class Solution(object):
	def permuteUnique(self, nums):
		nums = sorted(nums)
		res = []
		self.dfs(nums, res, [])
		return res
		
	def dfs(self, nums, res, path):
		if len(path) == len(nums):
			new_temp = []
			for idx in path:
				new_temp.append(nums[idx])
			res.append(new_temp[:])
			return
		
		for i in range(len(nums)):
			if i in path:
				continue
			if i >= 1 and nums[i] == nums[i-1] and i-1 not in path:
				continue
			path.append(i)
			self.dfs(nums, res, path)
			path.pop()

s = Solution()
print s.permuteUnique([1,1,2])
