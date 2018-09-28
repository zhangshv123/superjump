#!/usr/bin/python
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
"""
(1)p[j+1]不是'*'。情况比较简单，只要判断当前s的i和p的j上的字符是否一样（如果有p在j上的字符是'.',也是相同），如果不同，
返回false，否则，递归下一层i+1，j+1; 
(2)p[j+1]是'*'。那么此时看从s[i]开始的子串，假设s[i],s[i+1],...s[i+k]都等于p[j]那么意味着这些都有可能是合适的匹配，
那么递归对于剩下的(i,j+2),(i+1,j+2),...,(i+k,j+2)都要尝试（j+2是因为跳过当前和下一个'*'字符）。 
但因为dp，你用管
a)匹配0个
b)匹配一个->f(j, i - 1),而f(j, i - 1) 已经推过保证是正确的，所以不用再去看f(j, i - 2)。。。。
"""
#dp
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s),len(p)
        dp = [[ False for i in range(n + 1)] for j in range(m + 1)]
        for j in range(n+1):
            for i in range(m+1):
                if j == 0 and i == 0:   #dp[0][0] = True
                    dp[i][j] = True
                elif i <= m and j == 0:   #dp[i][0] = False
                    dp[i][j] == False
                elif j <= n and i == 0:  #dp[0][j] 的情况
                    if p[j-1] == "*":
                        dp[0][j] = dp[0][j-2]
                    else:
                        dp[0][j] = False
                else:
                    if p[j-1] == "*":
                        dp[i][j] |= dp[i][j-2]
                        dp[i][j] |= dp[i-1][j] and p[j-2] in [".",s[i-1]]
                    elif p[j-1] in [".",s[i-1]]:
                        dp[i][j] |= dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[m][n]
    
#滚动数组->存在覆盖:每种情况一定要赋值        
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #i:s, j:p
        len_s, len_p = len(s), len(p)
        #initilize dp
        #dp index is 1 more than string index dp[0][0]: ""~""
        dp = [[ False for i in range(len_s + 1)] for j in range(2)]
        for j in range(len_p + 1):
            for i in range(len_s + 1):
                if j == 0 and i == 0:
                    dp[j][i] = True
                elif j == 0 and i <= len_s:
                    dp[j][i] = False
                elif i == 0 and j <= len_p:
                    if p[j - 1] == "*":
                        dp[j % 2][0] = dp[(j - 2) % 2][0]
                    else:
                        dp[j % 2][0] = False
                else:
                    if p[j - 1] == "*":
                        #match 0                         
                        dp[j % 2][i] |= dp[(j - 2) % 2][i]
                        #only need to match 1, since previous will recursively check, dp must be atomic behavour
                        dp[j % 2][i] |= dp[j % 2][i - 1] and p[j - 2] in [".", s[i - 1]]
                    elif p[j - 1] in [".", s[i - 1]]:
                        dp[j % 2][i] = dp[(j - 1) % 2][i-1]
                    else:
                        dp[j % 2][i] = False
        return dp[len_p % 2][len_s]