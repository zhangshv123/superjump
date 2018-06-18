#!/usr/bin/python
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


"""
top sol
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"(":")","{":"}","[":"]"}
        stk = []
        for bracket in s:
            if bracket in bracket_map.keys():
                stk.append(bracket)
            if bracket in bracket_map.values():
                if len(stk) == 0 or bracket_map[stk.pop()] != bracket:
                    return False
        return len(stk) == 0

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"(":")","{":"}","[":"]"}
        stk = []
        for bracket in s:
            # last ele in stk is left bracket and it's correspond right bracket is current char
            if len(stk) > 0 and stk[-1] in bracket_map and bracket_map[stk[-1]] == bracket:
                stk.pop()
            else:
                stk.append(bracket)
        return len(stk) == 0