"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
"""
一个指针指向word1上次出现的位置，一个指针指向word2上次出现的位置。
因为两个单词如果比较接近的话，肯定是相邻的word1和word2的位置之差，
所以我们只要每次得到一个新位置和另一个单词的位置比较一下就行了。
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1, p2, s_len = -1, -1, len(words)
        for i, word in enumerate(words):
            if word == word1:
                p1 = i
            if word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                s_len = min(s_len, abs(p2 - p1))
        return s_len