"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
# I  relation is not transitive
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        for w1, w2 in zip(words1, words2):
            if not any([w1 == w2, [w1, w2] in pairs, [w2, w1] in pairs]):
                return False
        return True



# II  relation is transitive
from collections import defaultdict
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        union_map = defaultdict(lambda : "root")
        def findRoot(word):
            root = word
            while union_map[root] != "root":
                root = union_map[root]
            return root
        def union(w1, w2):
            r1, r2 = findRoot(w1), findRoot(w2)
            if r1 != r2:
                union_map[r1] = r2
                return True
            return False
        for w1, w2 in pairs:
            union(w1, w2)
        for w1, w2 in zip(words1, words2):
            if union(w1, w2):
                return False
        return True
