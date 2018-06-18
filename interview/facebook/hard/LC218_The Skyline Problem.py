#!/usr/bin/python
"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are 
given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these 
buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left 
and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0.
 You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to 
mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part 
of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
import heapq
class Solution(object):
    """
    we need data structure:
        max->O(1), insert->O(logn), remove->O(1)
    """
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for building in buildings:
            points.append((building[0], -building[2]))
            points.append((building[1], building[2]))
        """
        **lambda-> up should before down, 
        for up, larger should be first, 
        for down, smaller should be first
        """
        points.sort(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])
        res = []
        heights = [0]
        preHeight = 0
        for point in points:
            index = self.search(heights, abs(point[1]))
            if point[1] < 0:
                heights.insert(index, -point[1])
            else:
                heights.remove(point[1])
            if preHeight != heights[-1]:
                res.append([point[0], heights[-1]])
                preHeight = heights[-1]
        return res
#binary search        
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ps = []
        for b in buildings:
            ps.append((b[0], -b[2]))
            ps.append((b[1], b[2]))
        ps.sort(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])
        h, preH, res = [0], 0, []
        def search(h, val):
            l, r = 0, len(h) - 1
            while l <= r:
                m = l + (r - l) / 2
                if h[m] <= val:
                    l = m + 1
                else:
                    r = m - 1
            return l
        for p in ps:
            if p[1] < 0:
                idx = search(h, -p[1])
                h.insert(idx, -p[1])
            else:
                h.remove(p[1])
            if preH != h[-1]:
                res.append((p[0], h[-1]))
                preH = h[-1]
        return res
#linear search        
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ps = []
        for b in buildings:
            ps.append((b[0], -b[2]))
            ps.append((b[1], b[2]))
        ps.sort(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])
        h, preH, res = [0], 0, []
        def search(h, val):
            for i, e in enumerate(h):
                if e > val:
                    return i
            return len(h)
        for p in ps:
            if p[1] < 0:
                idx = search(h, -p[1])
                h.insert(idx, -p[1])
            else:
                h.remove(p[1])
            if preH != h[-1]:
                res.append((p[0], h[-1]))
                preH = h[-1]
        return res
                        