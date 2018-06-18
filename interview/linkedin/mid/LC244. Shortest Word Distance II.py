"""
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.
"""
from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.index_map = defaultdict(list)
        for i, word in enumerate(words):
            self.index_map[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.index_map[word1]
        list2 = self.index_map[word2]
        i, j = 0, 0
        ret = sys.maxsize
        while i < len(list1) and j < len(list2):
            idx1,idx2 = list1[i],list2[j]
            if idx1 < idx2:
                ret = min(ret,idx2 - idx1)
                i += 1
            else:
                ret = min(ret,idx1 - idx2)
                j += 1
        return ret

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)