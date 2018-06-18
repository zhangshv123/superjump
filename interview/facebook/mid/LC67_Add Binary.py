#!/usr/bin/python
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
"""
top solution, just naive is enough
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, carry = [], 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            na = i >= 0 and a[i] == "1"
            nb = j >= 0 and b[j] == "1"
            i -= 1
            j -= 1
            temp = na + nb + carry
            res.append(str(int(temp % 2)))
            carry = int(temp / 2)
        if carry != 0:
            res.append(str(carry))
        return "".join(reversed(res))


class Solution(object):
    def str_to_list(self, a, length):
        list_a = map(lambda a: int(a), reversed(a))
        while len(list_a) < length:
            list_a.append(0)
        return list_a
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length = max(len(a), len(b))
        list_a, list_b = self.str_to_list(a, length), self.str_to_list(b, length)
        list_c = []
        carry = 0
        for i in range(length):
            """
            sum = a ^ b
            carry = a & b, only 3 number so consider carry to be 1 by:
            a & b or (a ^ b) & c
            """
            list_c.append(list_a[i]^list_b[i]^carry)
            carry = (list_a[i]&list_b[i]) | ((list_a[i]^list_b[i]) & carry) 
        if carry != 0:
            list_c.append(carry)
        return "".join(map(lambda a: str(a), reversed(list_c)))
