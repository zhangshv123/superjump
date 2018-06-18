#!/usr/bin/python
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

"""
todo: top sol
"""
"""
设定状态为：f[i]表示s从0开始，长度为i的子串的解码方式数量，于是我们最终要求的答案便是f[n]。

那么如何求解f[i]呢？这个很简单，枚举最后一个字母对应1位还是2位，将f转化为规模更小的子问题。

设f[i] = 0
枚举最后一个字母对应1位（要求s[i - 1] != '0')，那么有f[i] += f[i-1]；
枚举最后一个字母对应2位（要求i > 1且s[i - 2]和s[i - 1]组成的字符串在"10"~"26"的范围内），那么有f[i] += f[i - 2]；
也就是说，我们可以通过f[i - 1]和f[i - 2]计算出f[i]来，这就是我们的状态和转移方程。

在具体实现中，我们可以按照i从1到n的顺序，依次计算出所有的f[i]。
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        #base dp[i]代表前i个元素的原问题的答案
        dp[0] = 1
        dp[1] = 1 
        #dp function
        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if s[i - 2] != "0" and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
            if int(s[i - 2: i]) == 0:#连续2个0的话，直接丢弃答案
                return 0
        return dp[len(s)]