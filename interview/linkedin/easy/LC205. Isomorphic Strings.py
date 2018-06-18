"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
"""
maping 3 type:
s     t
1  -  1  ok

1
	\  1  not ok
	/
1

       1
    / 
1   \     not ok
       1
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        replace_map = {}
        for i in range(len(s)):
            if s[i] not in replace_map:
                replace_map[s[i]] = t[i]
            else:
                if replace_map[s[i]] != t[i]:
                    return False
        values = replace_map.values()
        return len(set(values)) == len(values) #代表是一一对应！没有多对一的情况