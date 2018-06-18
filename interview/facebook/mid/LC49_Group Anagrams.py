#!/usr/bin/python
"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]
"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            sort_map[sorted_s].append(s)
        return sort_map.values()
