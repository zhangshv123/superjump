"""
Implement pow(x, n).
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = - n
        stk = []
        while n != 1:
            stk.append(1 if n % 2 == 0 else x)
            n /= 2
        res = x
        while len(stk) > 0:
            res = res * res * stk.pop()
        return res

        

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, - n)
        if n == 1:
            return x
        sub = self.myPow(x, n / 2)
        return sub * sub if n % 2 == 0 else sub * sub * x