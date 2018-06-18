#!/usr/bin/python
"""
The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string.

    Show Company Tags
    Show Tags
    Show Similar Problems

"""
class Solution(object):
    def read(self, index, s):
        start_index = index
        while index < len(s) and s[start_index] == s[index]:
            index += 1
        return index
    def countAndSay_oneTime(self, s):
        index = 0
        count_and_say = ""
        while index < len(s):
            new_index = self.read(index, s)
            count_and_say += str(new_index - index) + s[index]
            index = new_index
        return count_and_say
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count_and_say = "1"
        while n > 1:
            count_and_say = self.countAndSay_oneTime(count_and_say)
            n -= 1
        return count_and_say
s = Solution()
print s.countAndSay(3)