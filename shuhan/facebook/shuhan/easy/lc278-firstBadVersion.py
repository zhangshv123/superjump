#!/usr/bin/python
class Solution(object):
	def firstBadVersion(self, n):
		"""
		2分法，没啥好说的
		"""
		start,end = 1, n
		while start+1 < end:
			mid = start + (end-start)/2
			if isBadVersion(mid):
				end = mid
			else:
				start = mid
		if isBadVersion(start):
			return start
		return end
