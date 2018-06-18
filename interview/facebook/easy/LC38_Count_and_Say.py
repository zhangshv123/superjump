"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
class Solution(object):
    def translate(self, s):
        num = 1
        res = []
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i - 1] != s[i]:
                res.append(str(num))
                res.append(s[i - 1])
                num = 1
            else:
                num += 1
        return "".join(res)
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for _ in range(n - 1):
            res = self.translate(res)
        return res