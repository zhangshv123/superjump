思路：
这道题让我们设计一个点击计数器，能够返回五分钟内的点击数，提示了有可能同一时间内有多次点击。
由于操作都是按时间顺序的，下一次的时间戳都会大于等于本次的时间戳，那么最直接的方法就是用一个队列queue，
每次点击时都将当前时间戳加入queue中，然后在需要获取点击数时，我们从队列开头开始看，如果开头的时间戳在5分钟以外了，就删掉，
直到开头的时间戳在5分钟以内停止，然后返回queue的元素个数即为所求的点击数
from collections import deque
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.q.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while len(self.q) > 0 and self.q[0] <= timestamp - 300:
            self.q.popleft()
        return len(self.q)
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

这道题最好的方法就是queue，用array什么的worst case都是n^2,但是queue worst case是n

