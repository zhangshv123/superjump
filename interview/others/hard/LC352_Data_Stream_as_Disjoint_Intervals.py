# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
    
    def insertPos(self, val):
        i = 0
        while i < len(self.intervals) and val > self.intervals[i].end:
            i += 1
        return i

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        i = self.insertPos(val)
        mergeLeft = False if i == 0 else val <= self.intervals[i - 1].end + 1
        mergeRight = False if i == len(self.intervals) else val >= self.intervals[i].start - 1
        if mergeLeft and mergeRight:
            self.intervals[i - 1].end = self.intervals[i].end
            del self.intervals[i]
        elif mergeLeft and not mergeRight:
            self.intervals[i - 1].end = max(self.intervals[i - 1].end, val)
        elif not mergeLeft and mergeRight:
            self.intervals[i].start = min(self.intervals[i].start, val)
        else:
            self.intervals.insert(i, Interval(val, val))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals