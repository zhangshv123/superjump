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
最简单的模式，把2边都翻译成一种语言，然后看是否一样就可以了,和LC290一模一样
from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, words):
        out_d = defaultdict(list)
        for word in words:
            count = 0
            pattern = ""
            d = dict()
            for i in range(len(word)):
                if word[i] not in d:
                    d[word[i]] = count
                    count += 1
                pattern += str(d[word[i]])
            out_d[pattern].append(word)
        return out_d.values()     
s = Solution()
print s.isIsomorphic(["foo", "bar", "baz", "qux", "oof", "aaa", "aah", "abb" , "aba"]) 
print s.isIsomorphic(["foo", "abb"]) 

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

linkedin follow up:
如果给一个list of words
1.check是是不是所有的words都是isomorphic的：
第一个很简单，repeating 2-word solution for each consecutive pair of words 
2.是不是any two words是isomorphic的？
3.给list of words，make isomorphic groups
比方说：
words = {"foo", "bar", "baz", "qux", "oof", "aaa", "aah", "abb" , "aba"}
expected output:
[[aaa], [aba], [abb, foo], [bar, qux, baz], [oof, aah]]
就是用最简单的方案！最好！

