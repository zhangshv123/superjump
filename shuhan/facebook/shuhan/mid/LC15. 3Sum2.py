#!/usr/bin/python
class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		#get sorted list: remove duplicate in (i,j,k), choose first if duplicate
		snums = sorted(nums)
		res = []
		for i in range(len(snums) - 2):
			#duplicate element skip
			if i > 0 and snums[i - 1] == snums[i]:
				continue
			j = i + 1
			k = len(snums) - 1
			while j < k:
				ssum = snums[i] + snums[j] + snums[k]
				#duplicate element skip，其实和第13行的逻辑一样，都是取第一个出现的，不是第一个的就跳过，k也逻辑一致
				if j > i + 1 and snums[j - 1] == snums[j]:
					j += 1
				elif k < len(snums) - 1 and snums[k + 1] == snums[k]:
					k -= 1
				elif ssum == 0:
					res.append([snums[i], snums[j], snums[k]])
					j += 1
					k -= 1
				elif ssum < 0:
					j += 1
				else:
					k -= 1
		return res


s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
		
