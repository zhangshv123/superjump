#!/usr/bin/python
"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

"""
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        index, count, n = 0, 0, len(sentence)
        lengths = map(lambda s: len(s), sentence)
        for row in range(rows):
            col = -1
            while col + lengths[index] < cols:
                #always add white space after word
                col += lengths[index] + 1
                index += 1
                if index == n:
                    count += 1
                    index = 0
        return count
s = Solution()
print s.wordsTyping(["try","to","be","better"], 10000, 9001)