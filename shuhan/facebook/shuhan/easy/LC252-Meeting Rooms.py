#!/usr/bin/python

class Solution(object):
	def canAttendMeetings(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: bool
		"""
		intervals.sort(key = lambda x: x.start)
		for i in range(1,len(intervals)):
			if intervals[i].start < intervals[i-1].end:
				return False
		
		return True