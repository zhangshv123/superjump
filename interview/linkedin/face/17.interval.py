class Solution(object):
    def __init__(self):
        self.itv = []
        self.total = 0
    def insert(self, itv, nitv):
        """
        :type itv: List[Interval]
        :type nitv: Interval
        :rtype: List[Interval]
        """
        
        res = []
        i = 0
        #add before merge
        while i < len(itv) and itv[i].end < nitv.start:
            res.append(itv[i])
            i += 1
        mitv = Interval(nitv.start, nitv.end)
        #merge
        while i < len(itv) and itv[i].start <= nitv.end:
            mitv.start = min(mitv.start, itv[i].start)
            mitv.end = max(mitv.end, itv[i].end)
            i += 1
            self.total -= (itv[i].end - itv[i].start)#把老的都剪掉
        res.append(mitv)
        self.total += mitv.end - mitv.start#把新的小胖子加进去
        
        #add after merge
        while i < len(itv):
            res.append(itv[i])
            i += 1
        return res
    def getTotalCoverage():
        return self.total
           