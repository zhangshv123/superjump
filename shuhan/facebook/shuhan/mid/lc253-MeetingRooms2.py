#!/usr/bin/python
class Solution(object):
	def minMeetingRooms(self, intervals):
		"""
		每个区间的起始点代表一个区间的开始，会有可能将重叠区域＋１，每个区间的结束点代表一个区间的结束，将会使重叠区域－１，因此我们可以利用这个性质，并结合STL的map来实现
		"""
		points = []
		for interval in intervals:
			points.append((interval.start,1))
			points.append((interval.end,-1))
			
		points.sort(lambda a,b : a[1]-b[1] if a[0]==b[0] else a[0]-b[0])
		max_room, room = 0,0
		for point in points:
			room +=point[1]
			max_room = max(max_room,room)
		return max_room
