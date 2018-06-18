"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words
do not share common letters. You may assume that each word will contain only lower case letters. 
If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""
from collections import Set
class Solution(object):
    def nooverlap(self, left, right, chars):
        for i in range(26):
            if chars[left][i] and chars[right][i]:
                return False
        return True
    
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #first sort the word according to len max to len min
        words.sort(lambda a, b: len(b) - len(a))
        chars = [[False for _ in range(26)] for _ in range(len(words))]
        for i, word in enumerate(words):
            for c in word:
                chars[i][ord(c) - ord('a')] = True
        left, right, cutoffLength, res = 0, 0, 0, 0
        while left < len(words) and len(words[left]) >= cutoffLength:
            right = left + 1
            while right < len(words) and len(words[right]) >= cutoffLength:
                if self.nooverlap(left, right, chars):
                    cutoffLength = len(words[right])
                    res = max(res, len(words[left]) * len(words[right]))
                right += 1
            left += 1                
        return res