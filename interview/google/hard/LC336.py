#!/usr/bin/python
class Solution(object):
    def isPalindrome(self, word):
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        record_index_map = dict()
        res = []
        for i, word in enumerate(words):
            record_index_map[word] = i
        for i, word in enumerate(words):
            for j in range(len(words)+1):
                first_part = word[:j]
                second_part = word[j:]
                if self.isPalindrome(second_part):
                    first_part_reverse = first_part[::-1]
                    if first_part_reverse in record_index_map and record_index_map[first_part_reverse] != i:
                        res.append([i, record_index_map[first_part_reverse]])
                if len(first_part) > 0 and self.isPalindrome(first_part):
                    second_part_reverse = second_part[::-1]
                    if second_part_reverse in record_index_map and record_index_map[second_part_reverse] != i:
                        res.append([record_index_map[second_part_reverse], i])
        return res
words = ["abcd", "dcba", "lls", "s", "sssll"]
s = Solution()
print s.palindromePairs(words)               