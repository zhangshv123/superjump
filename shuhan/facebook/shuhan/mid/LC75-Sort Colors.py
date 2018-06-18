#!/usr/bin/python
class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		zero, second = 0,len(nums)-1
		for i in range(0,second+1):
			while nums[i] == 2 and i<second:
				nums[i], nums[second] = nums[second], nums[i]
				second -= 1
			while nums[i] == 0 and i > zero:
				nums[i], nums[zero] = nums[zero], nums[i]
				zero += 1
		return nums
s = Solution()
print s.sortColors([1, 0, 1, 2,1,1,1,1])		
