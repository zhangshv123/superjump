"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
"""
from collections import defaultdict
class Solution:
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        n = len(dict)
        abbv = ["#"] * n
        prefix = [1] * n
        def makeShort(word, i):
            if i >= len(word) - 2:
                return word
            return word[:i] + str(len(word) - 1 - i) + word[-1:]
        for i in range(n):
            abbv[i] = makeShort(dict[i], 1)
        for i in range(n):
            while True:
                s = set()
                for j in range(i + 1, n):
                    if abbv[i] == abbv[j]:
                        s.add(j)
                if len(s) == 0:
                    break
                s.add(i)
                for k in s:
                    prefix[k] += 1
                    abbv[k] = makeShort(dict[k], prefix[k])
        return abbv
            
            
