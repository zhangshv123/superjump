#!/usr/bin/python
"""
Implement int sqrt(int x).

Compute and return the square root of x.

-x too small, mid too large-|mid^2|-return point-|(mid+1)^2|-x too large,mid too small-
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while left < right:
            mid = left + (right - left) / 2
            if mid <= x / mid and (mid + 1) > x / (mid + 1):
                return mid
            elif mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
                