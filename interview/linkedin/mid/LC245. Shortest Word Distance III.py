"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.
"""
"""
这道题增加了一个条件，就是说两个单词可能会相同，所以在第一题中的解法的基础上做一些修改，
我最先想的解法是基于第一题中的解法二，由于会有相同的单词的情况，那么p1和p2就会相同，
这样结果就会变成0，显然不对，所以我们要对word1和word2是否的相等的情况分开处理，
如果相等了，由于p1和p2会相同，所以我们需要一个变量t来记录上一个位置，这样如果t不为-1，
且和当前的p1不同，我们可以更新结果，如果word1和word2不等，那么还是按原来的方法做
"""
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1, p2, s_len = -1, -1, len(words)
        if word1 != word2:
            for i, word in enumerate(words):
                if word == word1:
                    p1 = i
                if word == word2:
                    p2 = i
                if p1 != -1 and p2 != -1:
                    s_len = min(s_len, abs(p2 - p1))
        else:
            for i, word in enumerate(words):
                pre = p1
                if word == word1:
                    p1 = i
                if pre != -1 and pre != p1:
                    s_len = min(s_len, abs(p1 - pre))
        return s_len     