"""

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
"""
My solution uses DP. The main idea is as follows: I construct a array longest[], for any longest[i], it stores the longest length of valid parentheses which is end at i.

And the DP idea is :

If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot be a valid one.

Else if s[i] is ')'

     If s[i-1] is '(', longest[i] = longest[i-2] + 2

     Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], longest[5] = longest[4] + 2 + longest[1] = 6.
求极值问题一般想到DP或Greedy，显然Greedy在这里不太适用，只有用DP了。

1. 状态：
DP[i]：以s[i-1]为结尾的longest valid parentheses substring的长度。

2. 通项公式：
s[i] = '('：
DP[i] = 0

s[i] = ')'：找i前一个字符的最长括号串DP[i]的前一个字符j = i-2-DP[i-1]
DP[i] = DP[i-1] + 2 + DP[j]，如果j >=0，且s[j] = '('
DP[i] = 0，如果j<0，或s[j] = ')'

......... (     x    x    x    x   )
          j                      i-2 i-1

证明：不存在j' < j，且s[j' : i]为valid parentheses substring。
假如存在这样的j'，则s[j'+1 : i-1]也valid。那么对于i-1来说：
(    x    x    x    x    x
j'  j'+1                  i-1
这种情况下，i-1是不可能有比S[j'+1 : i-1]更长的valid parentheses substring的。

3. 计算方向
显然自左向右，且DP[0] = 0
http://bangbingsyb.blogspot.com/2014/11/leetcode-longest-valid-parentheses.html
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        longest = [0 for _ in range(len(s))]
        max_length = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":   #类型一：(......)()
                    longest[i] = longest[i - 2] + 2 if i >= 2 else 2
                elif i - longest[i - 1] - 1 >= 0 and s[i - longest[i - 1] - 1] == "(":  # (（...）)
                    longest[i] = longest[i - 1] + 2
                    if i - longest[i - 1] - 2 >= 0:  # 如果前面还有东西....((....))
                        longest[i] += longest[i - longest[i - 1] - 2]
                max_length = max(max_length, longest[i])
        return max_length

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = [0 for _ in range(len(s))]
        res = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    sol[i] = 2 + (0 if i < 2 else sol[i - 2])
                else:
                    #i-1 sol 存在
                    if sol[i - 1] != 0:
                        if i - 1 - sol[i - 1] >= 0 and s[i - 1 - sol[i - 1]] == "(":
                            sol[i] = 2 + sol[i - 1] + (0 if i - sol[i - 1] - 2 < 0 else sol[i - 2 - sol[i - 1]])
            res = max(res, sol[i])
        return res     



