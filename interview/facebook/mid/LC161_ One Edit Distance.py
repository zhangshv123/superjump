#!/usr/bin/python
"""
Given two strings S and T, determine if they are both one edit distance apart.
"""
class Solution(object):
    def isOneCharacterReplaced(self, s, t):
        count = 0
        for i, c in enumerate(s):
            print c, t[i]
            if c != t[i]:
                count += 1
        print count
        return count == 1
    
    def isOneCharacterAdded(self, s, t):
        count, i, j = 0, 0, 0
        while j < len(t):
            if i >= len(s) or s[i] != t[j]:
                count += 1
                j += 1
            else:
                i += 1
                j += 1
        return count == 1
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_s = s if len(s) <= len(t) else t
        str_l = s if len(s) > len(t) else t
        if len(str_s) == len(str_l):
            return self.isOneCharacterReplaced(str_s, str_l)
        elif len(str_s) + 1 == len(str_l):
            return self.isOneCharacterAdded(str_s, str_l)
        return False

class Solution(object):
    
    
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #same length
        if len(s) == len(t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
            return count == 1
        #length 1 diff
        if abs(len(s) - len(t)) == 1:
            s, l = (s, t) if len(s) < len(t) else (t, s)
            count, i, j = 0, 0, 0
            while j < len(l):
                #i走完，j还有 或是 s[i] != l[j]
                if i >= len(s) or s[i] != l[j]:
                    count += 1
                    j += 1
                elif s[i] == l[j]:
                    i += 1
                    j += 1
            return count == 1
        return False        
            