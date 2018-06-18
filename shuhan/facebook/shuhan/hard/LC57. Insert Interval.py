# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		其实就是三种情况，一次遍历就解决了。看图
		https://simpleandstupid.com/2014/10/29/insert-interval-leetcode-%E8%A7%A3%E9%A2%98%E7%AC%94%E8%AE%B0/
		"""
		res = []
		for interval in intervals:
			if interval.end < newInterval.start:
				result.append(interval)
			elif interval.start > newInterval.end:
				res.append(newInterval)
				newInterval = interval
			elif interval.end >= newInterval.start or interval.start <= newInterval.end:
				newInterval.start = min(newInterval.start,interval.start)
				newInterval.end = max(newInterval.end,interval.end)
		res.append(newInterval)
		return res
				

