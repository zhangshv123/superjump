"""

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
#xin二分模板 start(inclusize) end(exclusive)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        start,end = 0,num
        while start < end:
            mid = (start+end)/2
            if mid*mid == num:
                return True
            elif  mid*mid < num:
                start = mid +1
            else:
                end = mid
        return False