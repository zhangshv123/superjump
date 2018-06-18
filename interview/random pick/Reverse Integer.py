#!/usr/bin/python
import sys
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        neg = n < 0
        if neg:
            n = -n
        res = 0
        while n > 0:
            digit = n % 10
            n = n / 10
            if res > sys.maxint / 10:
                return 0
            res = res * 10 + digit
        return -res if neg else res