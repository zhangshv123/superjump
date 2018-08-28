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

由于Follow up中说每秒中会有很多点击，下面这种方法就比较巧妙了，定义了两个大小为300的一维数组times和hits，分别用来保存时间戳和点击数，
在点击函数中，将时间戳对300取余，然后看此位置中之前保存的时间戳和当前的时间戳是否一样，一样说明是同一个时间戳，那么对应的点击数自增1，
如果不一样，说明已经过了五分钟了，那么将对应的点击数重置为1。那么在返回点击数时，我们需要遍历times数组，找出所有在5分中内的位置，
然后把hits中对应位置的点击数都加起来即可
具体参考：
http://www.cnblogs.com/grandyang/p/5605552.html

followup让快一些，然后就用一个定长（这里的时刻最小单位到秒，所以开300的）结构数组，以对应访问时刻模300作为索引，
存下对应hit次数以及hit的时间来做统计，更新思路和队列差不多。其实hit时刻可以不用开数组计，可以只用一个单变量来表示最后一次访问的时刻，
然后开一个朴素的数组计次，不过既然他没问我也就没有实现。最后是考一些单元测试的东西，自己写一下测试，很快就写完了。最后问我如果time.time()不准怎么办。
我说可以给hit和count函数传参，或者用mock库来提供假的系统时间，或者是用一个实例成员变量来表示，最后他说还有办法么，
然后说其实可以传一个TimeProvider的对象到类的构造函数中，这样通过不同的TimeProvider.provide_time()函数就可以提供不同时间源，
而在HitCounter类看来外部的行为是没有区别的，嗯我当时表示哇听起来确实很科学。他没问时空复杂度，没问更小的精度，也没考多线程，
最后就让我问了三两个问题，不到30分钟就结束了面试（呃...国人小哥果然很好）


