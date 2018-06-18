"""
There is a new alien language which uses the latin alphabet. However, the order among letters 
are unknown to you. You receive a list of non-empty words from the dictionary, where words are
 sorted lexicographically by the rules of this new language. Derive the order of letters in 
 this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".
"""
from collections import deque
from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        cmps = set() #可能会有重复
        allChars = set() #所有出现的字母
        for i, word1 in enumerate(words):
            for c in word1:
                allChars.add(c)
            for word2 in words[i + 1:]:
                for i, c1 in enumerate(word1):
                    if i >= len(word2):
                        return ""
                    if c1 != word2[i]:
                        cmps.add((c1, word2[i]))
                        break
        outDegreeMap = defaultdict(list)
        inDegreeNums = defaultdict(int)
        for cmp in cmps:
            outDegreeMap[cmp[0]].append(cmp[1])
            inDegreeNums[cmp[1]] += 1
        q = []
        for char in allChars:
            if inDegreeNums[char] == 0:
                q.append(char)
        index = 0
        while index < len(q):
            cur = q[index]
            index += 1
            for dpen in outDegreeMap[cur]:
                inDegreeNums[dpen] -= 1
                if inDegreeNums[dpen] == 0:
                    q.append(dpen)
        return "".join(q) if len(allChars) == len(q) else ""
        
        