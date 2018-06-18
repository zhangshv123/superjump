#!/usr/bin/python

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
这道和之前那道 Insert Interval 插入区间 很类似，这次题目要求我们合并区间，之前那题明确了输入区间集是有序的，而这题没有，
所有我们首先要做的就是给区间集排序，由于我们要排序的是个结构体，所以我们要定义自己的comparator，才能用sort来排序，
我们以start的值从小到大来排序，排完序我们就可以开始合并了，首先把第一个区间存入结果中，然后从第二个开始遍历区间集，
如果结果中最后一个区间和遍历的当前区间无重叠，直接将当前区间存入结果中，如果有重叠，将结果中最后一个区间的end值更新为结果中
最后一个区间的end和当前end值之中的较大值，然后继续遍历区间集，以此类推可以得到最终结果
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals.sort(key = lambda a: a.start)
        for cur in intervals:
            if len(res) == 0:
                res.append(cur)
            else:
                if res[-1].end >= cur.start:
                    res[-1].end = max(res[-1].end, cur.end)
                else:
                    res.append(cur)
        return res