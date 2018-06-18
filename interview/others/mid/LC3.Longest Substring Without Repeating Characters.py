"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        d = defaultdict(int)
        dup = 0
        max_length = 0
        while end < len(s):
            if d[s[end]] == 1:
                dup += 1
            d[s[end]] += 1
            while start < end and dup > 0:
                if d[s[start]] == 2:
                    dup -= 1
                d[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
            end += 1
        return max_length
        
from collections import Set
class Solution(object): 
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = set()
        i, j, n, res = 0, 0, len(s), 0
        while j < n:
            #remove dup
            if s[j] in st:
                #delete s[i] util s[i] == s[j]
                while s[i] != s[j]:
                    st.remove(s[i])
                    i+= 1
                #delete s[i]                    
                st.remove(s[i])
                i+= 1
            #add new
            st.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res        