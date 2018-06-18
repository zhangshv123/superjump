class Solution(object):
	def threeSum(self, nums):
		nums.sort()
		res = []
		size = len(nums)
		for i in range(0,size-2):
			if i > 0 and nums[i] == nums[i-1]: #只取第一个
				continue
			target = nums[i]*(-1)
			start,end = i+1,size-1
			while start < end:
				if nums[start]+nums[end] == target:
					res.append([nums[i],nums[start],nums[end]])
					start += 1
					end -= 1
					while start<end and nums[start] == nums[start-1]:#去重，只取第一个
						start +=1
					while start<end and nums[end] == nums[end+1]:#去重，只取第一个
						end -= 1
				elif nums[start]+nums[end] < target:
					start += 1
					
				else:
					end -= 1
		return res

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -1,  -4])
[-1,-1,0,1,2]