"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

the rule is complex,but in this condition. It can be tell as:
we start from the end of String.
if the char before the current char we are reading.
plus it
if not
reduce it
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s) - 1):
            if m[s[i]] < m[s[i + 1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]
        return res + m[s[-1]]