#!/usr/bin/python
"""
Implement int sqrt(int x).

Compute and return the square root of x.

-x too small, mid too large-|mid^2|-return point-|(mid+1)^2|-x too large,mid too small-
"""
class Solution(object):
    def mySqrt(self, x):
        if x == 1:
            return 1
        start, end = 0, x/2
        while start + 1 < end:
            mid = (start + end)/2
            if mid * mid <= x:
                start = mid
            elif mid* mid > x:
                end = mid
        
        if start*start <= x and end * end > x:
            return start
        elif end*end <=x and (end+1)*(end+1) > x:
            return end
                