"""
2. 给一个质数数组，没有重复元素，比如[2, 3, 5]，要求返回所有元素之间可能的乘积，比如结果是[2, 3, 5, 6, 10, 15, 30]，
每个数最多用一次，结果不一定需要是有序的。. 
最小的素数是2
"""
from collections import defaultdict
class Solution(object):
	def combinationMutiply(self, nums):
		res = [1]
		for num in nums:
			new_res = []
			for aws in res:
				new_res.append(aws * num)
			res += new_res
		return res[1:]
s = Solution()
print s.combinationMutiply([2,3,5])


class Solution(object):
	def combinationMutiply(self, nums):
		nums.sort()
		path, res = [], []
		self.dfs(nums, 0, 1, res)
		return res[1:]

	def dfs(self, nums, index, ans, res):
		res.append(ans)
		for i in xrange(index, len(nums)):
			self.dfs(nums, i + 1, ans * nums[i], res)

s = Solution()
print s.combinationMutiply([2,3,5])