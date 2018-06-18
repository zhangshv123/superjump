#!/usr/bin/python
"""
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))
        """
        sort the point by timeline
        if timeline is same, end point first. we reduce first
        otherwise room might be more than we need
        """
        points.sort(lambda a, b: a[1] - b[1] if a[0] == b[0] else a[0] - b[0])
        max_room, room = 0, 0
        for point in points:
            room += point[1]
            max_room = max(max_room, room)
        return max_room