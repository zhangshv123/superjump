#!/usr/bin/python
class Solution(object):
	def subsets(self, nums):
		res = []
		self.dfs(sorted(nums), 0, [], res)
		return res
	
	def dfs(self, nums, index, path, res):
		res.append(path)
		for i in xrange(index, len(nums)):
			self.dfs(nums, i+1, path+[nums[i]], res)
			#这里path+[nums[i]]是新建了一个new object，不是原来的path了
