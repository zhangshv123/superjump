#!/usr/bin/python
class Solution(object):
	def moveZeroes1(self, nums):
		"""
		方法一：
		把非0的都放在前面，然后pos和其后面的元素都置为零
		time:O(n)
		"""
		pos = 0
		size = len(nums)
		for i in range(size):
			if nums[i] != 0:
				nums[pos] = nums[i]
				pos += 1
		
		for j in range(pos,size):
			nums[j] = 0
