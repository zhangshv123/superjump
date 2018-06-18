#!/usr/bin/python
"""
Given a string s and a dictionary of words dict, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
#139 middle 题目

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        # max_len = max(lambda l:len(l), wordDict)
        for i in range(len(s) + 1):
            for j in range(i): # for j in range(i+1) 都是一样的
                dp[i] |= dp[j] and s[j: i] in wordDict
        return dp[len(s)]
        
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
#backtracking
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        n = len(s) -1
        # dp[i]: s[:i]的子问题
        dp = [None for _ in range(n+1)]
        self.helper(s, n, wordSet, dp)
        return dp[n]
    
    def helper(self, s, end, wordSet, dp):
        if dp[end] != None:
            return
        result = []
        if s[:end+1] in wordSet:
            result.append(s[:end+1])
        for p in range(1,end+1):
            if s[p:end+1] in wordSet:
                self.helper(s,p-1,wordSet,dp)
                for preString in dp[p-1]:
                    result.append(preString + " " + s[p:end+1] )
        dp[end] = result

import sets
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0 or len(wordDict) == 0:
            return []
        dp = [[] for _ in range(len(s) + 1)]
        dp[0].append("")
        wordDict = set(wordDict)
        lens = map(lambda a: len(a), wordDict)
        minLen, maxLen = min(lens), max(lens)
        for i in range(len(s) + 1 - minLen):
            for j in range(i + minLen, min(i + maxLen + 1, len(s) + 1)):
                word = s[i: j]
                if word in wordDict:
                    dp[j] += map(lambda ans:ans + " " + word if len(ans) > 0 else word, dp[i])
        # print dp
        return dp[len(s)]        


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(wordDict) == 0:
            return []
        n = len(s)
        wordDict = set(wordDict)
        breakable = [False for _ in range(n + 1)]
        breakable[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                breakable[i] |= breakable[j] and s[j:i] in wordDict
        dp = [[] for _ in range(n + 1)]
        dp[0].append("")
        maxLen = max(map(lambda a: len(a), wordDict))
        for i in range(1, n + 1):
            if not breakable[i]:
                continue
            for j in range(max(0, i - maxLen), i):
                word = s[j:i]
                if word in wordDict:
                    for ans in dp[j]:
                        dp[i].append(ans + " " + word)
        return map(lambda c: c[1:], dp[n])        