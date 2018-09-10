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
 linkedin follow up
 if the input is a scrape of wikipedia documents, instead of a nice clean list of words
pass the scrape file and throw out all HTML tags and process the content to have all valid words
 advanced: what if the input is a stream and there are more words than can fit in memory (how do you solve this in a distributed way)?

存的下，就一个个读进来处理：
abc abc abc ... * 1B
abc: {bac bca}
de: {ed}

存不下，就要map reduce，本质上用分布式内存，用多台机子的内存来存

