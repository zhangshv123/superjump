"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #assume minHeap could at most be larger than maxHeap by 1
        self.maxHeap, self.minHeap = [], []
        self.isEven = True

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.isEven:
            heapq.heappush(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        self.isEven = not self.isEven 

    def findMedian(self):
        """
        :rtype: float
        """
        # print self.minHeap, self.maxHeap, self.isEven
        if self.isEven:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return self.minHeap[0]