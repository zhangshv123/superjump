"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1],

A solution set is:
[
  [-1, 0, 1]
  [-1, -1, 2]
]

1. could be resused multiples times
"""
class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		path = []
		res = []
		nums.sort()
		print nums
		self.helper(nums,path,0,res)
		return res
	
	def helper(self, nums, path, idx,res):
		if len(path) == 3:
#			print path,idx
			if sum(path) == 0:
				res.append(path[:])
			return
		for i in range(idx, len(nums)):
			print i, path
			path.append(nums[i])
			self.helper(nums,path,i,res)
			path.pop()
			
s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])
# 这里面有2个-1，应该把input变成没有重复数字的更好，有重复的数字也不影响结果，只是更慢
# 时间复杂度：6的3次方