#!/usr/bin/python
"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
"""
https://leetcode.com/problems/h-index/#/solution
分为存在sol和不存在sol
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(lambda a,b: b - a)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)
"""
todo: method 2
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i in range(len(citations)):
            if citations[len(citations) - 1 - i] < i + 1:
                return i
        return len(citations)
        
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right = 0, len(citations)
        while left < right:
            mid = left + (right - left) / 2
            if citations[len(citations) - 1 - mid] < mid + 1:
                right = mid
            else:
                left = mid + 1
        return left