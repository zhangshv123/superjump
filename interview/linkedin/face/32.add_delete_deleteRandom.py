import random
class Solution(object):
    def __init__(self):
        self.recordMap = {}
        self.array = []
    def add(self, T):
        """
        :type itv: List[Interval]
        :type nitv: Interval
        :rtype: List[Interval]
        """
        m, a = self.recordMap, self.array
        a.append(T)
        m[T] = a
    def delete(self, T):
        m, a = self.recordMap, self.array
        idx = m[T]
        m.remove(idx)
        a[-1], a[idx] = a[idx], a[-1]
        a.pop()
        m.put(idx, T)
        
    def getRandom():
        idx = random.randrange(0, self.array)
        
           