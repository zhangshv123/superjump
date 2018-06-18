from collections import defaultdict
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def getSlope(self, p1, p2):
        if p1.x == p2.x:
            return sys.maxint
        return float(p1.y - p2.y) / float(p1.x - p2.x)
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        max_res = 0
        for p1 in points:
            res = 0
            slope_map = defaultdict(int)
            samepoint = 1
            for p2 in points:
                if p1 == p2:
                    continue
                if p1.x == p2.x and p1.y == p2.y:
                    samepoint += 1
                else:    
                    slope_map[self.getSlope(p1, p2)] += 1
                    res = max(res, slope_map[self.getSlope(p1, p2)])
            max_res = max(max_res, res + samepoint)
        return max_res
        