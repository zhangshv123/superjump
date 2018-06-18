"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
"""
从Insert Interval那题的解法，我们知道了如何判断两个interval是否重合，如果不重合，如何判断先后顺序。那么这题就很简单了，首先按照start的大小来给所有interval排序，start小的在前。然后扫描逐个插入结果。如果发现当前interval a和结果中最后一个插入的interval b不重合，则插入a到b的后面；反之如果重合，则将a合并到b中。
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals.sort(key = lambda a:a.start)
        for interval in intervals:
            if len(res) == 0 or res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end,interval.end)
        return res