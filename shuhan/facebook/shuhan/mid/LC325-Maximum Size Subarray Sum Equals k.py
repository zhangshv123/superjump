#!/usr/bin/python
class Solution(object):
	    def maxSubArrayLen(self, nums, k):
			d = dict()
			cur,res,= 0,0
			for i in range(len(nums)):
				cur += nums[i]
				if cur == k:
					res = i+1
				if cur - k in d:
					res = max(res,i-d[cur-k])
				if cur not in d:#只保留第一次出现的，后面都不行
					d[cur] = i
			return res

s = Solution()
print s.maxSubArrayLen([1,0,-1], -1)