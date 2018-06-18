#!/usr/bin/python
"""
 似乎是新题， 给一个排序好的数组，数一数有多少个子集（subset）使得子集里面的最大元素加上最小元素小于K
A: [2, 3, 5, 7]  K: 8 . 
=> # of subsets S: Max(S) + Min(S) < K
=> [2] , [2, 3], [2, 5], [2, 3, 5], [3] => #: 5
"""
class Solution(object):
	def numOfSubset(self, nums, target):
		i, j, res = 0, len(nums) - 1, []
		while i < j:
			if nums[i] + nums[j] < target:
				for k in range(i + 1, j + 1):
					for aws in self.combinationSubset(nums[i + 1: k]):
						res.append([nums[i]] + aws + [nums[k]])
				i += 1
			else:
				j -= 1
		for num in nums:
			if num < target:
				res.append([num])
		return res
	def combinationSubset(self, nums):
		res = [[]]
		for num in nums:
			new_res = []
			for aws in res:
				new_res.append(aws + [num])
			res += new_res
		return res
#重复
class Solution(object):
	def numOfSubset(self, nums, target):
		i, j, res = 0, len(nums) - 1, []
		while i < j:
			#去重
			if i != 0 and nums[i] == nums[i - 1]:
				i += 1
			#去重	
			elif j != len(nums) - 1 and nums[j] == nums[j + 1]:
				j -= 1
			elif nums[i] + nums[j] < target:
				#去重
				for k in range(i + 1 if nums[i] != nums[j] else j, j + 1):
					for aws in self.combinationSubset(nums[i + 1: k]):
						res.append([nums[i]] + aws + [nums[k]])
				i += 1
			else:
				j -= 1
		for i in range(len(nums)):
			if nums[i] < target:
				#去重
				if i != 0 and nums[i] == nums[i - 1]:
					continue
				res.append([nums[i]])
		return res
	def combinationSubset(self, nums):
		res = [[]]
		#去重		
		pre_size = 0
		nums.sort()
		for i in range(len(nums)):
			size = len(res)
			for j in range(size):
				if i == 0 or nums[i] != nums[i -1] or j>=pre_size:
					res.append(res[j] + [nums[i]])
			pre_size = size
		return res
s = Solution()		
print s.numOfSubset([3,3,3,3],8)	