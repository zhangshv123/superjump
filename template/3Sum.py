class Solution(object):
	def threeSum(self, nums):
		nums = sorted(nums)
		res = []
		for i, num in enumerate(nums):
			#去重
			if i > 0 and nums[i] == nums[i-1]:
				continue
			res += self.helper(i+1, nums, -num)
		return res
	
	
	def helper(self, start, nums, target):
		res = []
		i, j = start, len(nums) - 1
		while i < j:
			#去重
			if i > start and nums[i] == nums[i-1]:
				i += 1
				continue
			#去重
			if j < len(nums) - 1 and nums[j] == nums[j+1]:
				j -= 1
				continue
			if nums[i] + nums[j] == target:
				res.append([-target, nums[i], nums[j]])
				i += 1
				j -= 1
			elif nums[i] + nums[j] < target:
				i += 1
			else:
				j -= 1
		return res

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])	