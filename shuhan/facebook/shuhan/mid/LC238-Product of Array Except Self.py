#!/usr/bin/python
#The idea is simply. The product basically is calculated using the numbers before the current number and the numbers after the current number. Thus, we can scan the array twice. First, we calcuate the running product of the part before the current number. Second, we calculate the running product of the part after the current number through scanning from the end of the array.
#其实直接先得到所有数字的，然后res[i] = toal/nums[i]  就可以了，特别考虑nums[i]==0的情况
class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		length = len(nums)
		res = [0]*length
		if length == 0:
			return res
		prefix = 1 
		for i in range(length):
			res[i] = prefix
			prefix *= nums[i]
		sufix = 1
		for i in reversed(range(length)):
			res[i] *= sufix
			sufix *= nums[i]
		
		return resf