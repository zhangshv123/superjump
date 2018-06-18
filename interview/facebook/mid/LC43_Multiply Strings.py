#!/usr/bin/python
"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        """
        remember to check whether "0" exist
        """
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2)
        len3 = len1 + len2
        num3 = [0 for _ in range(len3)]
        for i, char1 in enumerate(reversed(num1)):
            for j, char2 in enumerate(reversed(num2)):
                num3[i + j] += int(char1) * int(char2)
        for i in range(len3 - 1):
            num3[i + 1] += num3[i] / 10
            num3[i] = num3[i] % 10
        num3.reverse()
        res_list = num3[0 if num3[0] > 0 else 1:]
        res_str_list = map(lambda a: str(a), res_list)
        return "".join(res_str_list)
       
s = Solution()
print s.multiply("10", "12")
    
    