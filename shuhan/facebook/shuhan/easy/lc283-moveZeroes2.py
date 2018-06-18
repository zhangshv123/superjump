#!/usr/bin/python
class Solution(object):
	def moveZeroes2(self, nums):
		"""
		方法二：更推荐
		2个指针，pos相当于right，position的右边一定都为0，和i来交换
		time:O(n)
		"""
		pos = 0
		size = len(nums)
		for i in range(size):
			if nums[i] != 0:
				nums[pos],nums[i] = nums[i],nums[pos]
				pos += 1