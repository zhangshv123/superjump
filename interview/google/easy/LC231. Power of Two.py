"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return self.isPowerOfTwo(n / 2)
        
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n & 1 == 1:
                return False
            n >>= 1
        return True        