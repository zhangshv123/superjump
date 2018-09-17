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
思路：
可以选用一个最大堆一个最小堆，保持两个堆的大小平衡，让大顶堆保存小的一半的数，小顶堆保存较大的一半数．
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #assume minHeap could at most be larger than maxHeap by 1
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.minHeap, num) #一定要先放minheap，这样2边的大小size diff不会超过1
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
    def findMedian(self):
        """
        :rtype: float
        """
        # print self.minHeap, self.maxHeap, self.isEven
        size = len(self.minHeap) + len(self.maxHeap)
        if size % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return self.minHeap[0]