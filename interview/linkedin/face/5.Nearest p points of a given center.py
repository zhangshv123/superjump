#可以用最小堆也可以用最大堆。
#1. 最小堆。把所有点放进最小堆（根据点到中心的距离比大小），然后取k个点出来。时间复杂度O(nlogn)
#2. 最大堆。遍历每个点，对于当前点： 
#    1) 如果堆内元素少于k，放入当前点
#    2) 如果堆内元素等于k，如果当前点距离 < heap.peek()，堆删除堆顶元素，再放入当前点
#                                      如果当前点距离 >= heap.peek()，忽略当前点。
#最大堆时间复杂度 是 O(nlogk)。
class Point(object):
    def __init__(self, x,y):
         self.x = x
         self.y = y
      
import heapq
class Solution(object):
    def closestKPoint(c, points, k):
        cmp = lambda p1, p2: (p1.x - c.x) * (p1.x - c.x) + (p1.y - c.y) * (p1.y - c.y) - (p2.x - c.x) * (p2.x - c.x) - (p2.y - c.y) * (p2.y - c.y)
#        heapq(cmp)
#        loop points -> heapq
#        choose first k
        points.sort(cmp)
        return points[:k]
s = Solution()
print s.closestKPoint([Point(1,1),Point(2,2)], 1)